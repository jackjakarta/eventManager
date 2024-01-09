import os
import requests

from openai import OpenAI
from decouple import config
from django.conf import settings

from .utils import RandomGenerator


class ImageDallE:
    """Image Generation with the OpenAI DALL-E model."""

    def __init__(self, model="dall-e-3"):
        self.client = OpenAI(api_key=config("OPENAI_API_KEY"))
        self.model = model
        self.prompt = None
        self.response = None
        self.image_url = None
        self.image_path = None

    def generate_image(self, prompt):
        self.prompt = prompt
        self.response = self.client.images.generate(
            model=self.model,
            prompt=self.prompt,
            size="1792x1024",
            quality="standard",
            n=1,
        )
        self.image_url = self.response.data[0].url

        return self.image_url

    def save_image(self, name=RandomGenerator(6).random_string()):
        request_response = requests.get(self.image_url, stream=True)
        if request_response.status_code == 200:
            timestamp = name
            image_dir = os.path.join(settings.MEDIA_ROOT, "images")
            image_filename = f"image_dalle_{timestamp}.png"
            self.image_path = os.path.join(image_dir, image_filename)
            os.makedirs(image_dir, exist_ok=True)

            with open(self.image_path, "wb+") as f:
                for chunk in request_response.iter_content(8192):
                    f.write(chunk)
            print(f"\nImaged saved at: {self.image_path}.")
        else:
            print("\nFailed to get image!")
