from django.conf import settings
from openai import OpenAI


class ImageDallE:
    """Image Generation with the OpenAI DALL-E 3 model."""

    def __init__(self, model="dall-e-3", user_id=None):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = model
        self.prompt = None
        self.response = None
        self.image_url = None
        self.user_id = user_id

    def generate_image(self, prompt):
        self.prompt = prompt
        self.response = self.client.images.generate(
            model=self.model,
            prompt=self.prompt,
            size="1792x1024",
            quality="standard",
            style="vivid",
            n=1,
            user=self.user_id,
        )
        self.image_url = self.response.data[0].url

        return self.image_url


class GPTAssistantsApi:
    """OpenAI Assistants API Class"""

    def __init__(self, assistant_id):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.assistant_id = assistant_id
        self.thread = None
        self.prompt = None
        self.message = None
        self.run = None
        self.messages = None
        self.custom_instructions = None

    def create_thread(self):
        self.thread = self.client.beta.threads.create()

    def create_message(self, prompt):
        self.prompt = prompt
        self.message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=self.prompt
        )

    def create_run(self, custom_instructions=""):
        self.custom_instructions = custom_instructions
        self.run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id,
            instructions=self.custom_instructions
        )

    def retrieve_run(self):
        self.run = self.client.beta.threads.runs.retrieve(
            thread_id=self.thread.id,
            run_id=self.run.id
        )

    def list_messages(self):
        self.messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )
