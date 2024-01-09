import os
import requests
import tempfile

from openai import OpenAI
from decouple import config
from django.core.files import File

from .models import DallEImage
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

    def save_image(self, name=None):
        request_response = requests.get(self.image_url, stream=True)
        if request_response.status_code == 200:
            if name is None:
                name = RandomGenerator(6).random_string()

            # Create a temporary file to store the image
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_image:
                for chunk in request_response.iter_content(8192):
                    temp_image.write(chunk)

            # Open the temporary file and save it to the DallEImage model's image field
            dalle_image = DallEImage()
            dalle_image.image.save(f"image_dalle_{name}.png", File(open(temp_image.name, 'rb')))
            dalle_image.save()

            # Delete the temporary file
            os.remove(temp_image.name)
        else:
            print("\nFailed to get image!")
