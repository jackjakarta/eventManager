from decouple import config
from openai import OpenAI

OPENAI_API_KEY = config("OPENAI_API_KEY")


def check_moderate(input_text: str) -> bool:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.moderations.create(input=input_text)
    categories_object = response.results[0].categories

    if any(getattr(categories_object, attr) for attr in categories_object.__dict__):
        return True
    else:
        return False
