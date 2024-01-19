import time

from decouple import config
from django.shortcuts import render, redirect
from django.contrib import messages

from website.forms import GPTAssistantsApiForm, DallEImageForm
from website.ai import GPTAssistantsApi, ImageDallE

OPENAI_ASSISTANT_ID = config("OPENAI_ASSISTANT_ID")


# AI API Call Views
def ai_assistant_event(request):
    if request.user.is_authenticated:
        ai = GPTAssistantsApi(OPENAI_ASSISTANT_ID)

        if request.method == "POST":
            form = GPTAssistantsApiForm(request.POST)

            if form.is_valid():
                prompt = form.cleaned_data["prompt"]
                # custom_instructions = form.cleaned_data["custom_instructions"]

                ai.create_thread()
                ai.create_message(prompt)
                ai.create_run()

                while True:
                    ai.retrieve_run()

                    if ai.run.status == "completed":
                        ai.list_messages()

                        m_list = [x.content[0].text.value for x in reversed(ai.messages.data)]
                        user_prompt = m_list[0]
                        event_info = m_list[1]

                        # Split the string to extract Event Name, Event Flyer, and Event Description
                        event_name_start = event_info.find('Event Name: ')
                        event_flyer_start = event_info.find('Event Flyer: ')
                        event_description_start = event_info.find('Event Description: ')

                        event_name = event_info[event_name_start + len('Event Name: '):event_flyer_start].strip()
                        event_flyer = event_info[
                                      event_flyer_start + len('Event Flyer: '):event_description_start].strip()
                        event_description = event_info[event_description_start + len('Event Description: '):].strip()

                        return render(request, "website/assistant/ai_page.html", {
                            "user_prompt": user_prompt,
                            "event_name": event_name,
                            "event_flyer": event_flyer,
                            "event_description": event_description,
                        })
                    elif ai.run.status == "failed":
                        messages.error(request, "Something went wrong. Please try again...")
                        return redirect("website:api_calls:assistant")
                    else:
                        time.sleep(3)
                        continue
        else:
            form = GPTAssistantsApiForm()
            return render(request, "website/assistant/ai_page.html", {
                "form": form,
            })
    else:
        messages.error(request, "You have to be logged in to use this feature!")
        return redirect("website:user_auth:login")


def ai_assistant_image(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = DallEImageForm(request.POST)
            if form.is_valid():
                user_prompt = form.cleaned_data["image_prompt"]
                prompt_for_model = (f"Generate an event flyer based on this description:\n\n{user_prompt}.\n\n"
                                    f"Follow the description precisely.")

                img_ai = ImageDallE()
                img_ai.generate_image(prompt_for_model)
                img_url = img_ai.image_url

                return render(request, "website/assistant/ai_image_page.html", {
                    "image": img_url,
                })
        else:
            form = DallEImageForm()
            return render(request, "website/assistant/ai_image_page.html", {
                "form": form,
            })
