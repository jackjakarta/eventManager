import urllib.request
from secrets import token_urlsafe

from django.core.files import File

from website.models import UserGeneratedImage


def save_image_to_db(ai_user, image_url):
    if ai_user:
        # Create a new DallEImage instance
        new_image = UserGeneratedImage.objects.create(
            title=f"{ai_user.first_name} {ai_user.last_name} - ID: {token_urlsafe(8)}",
            manager=ai_user
        )

        # Open the image URL and create a Django File object
        with urllib.request.urlopen(image_url) as response:
            django_file = File(response, name=f'dall_e_{ai_user.last_name}_{token_urlsafe(8)}.png')

            # Save the image content to the model field
            new_image.image.save(
                django_file.name,
                django_file,
                save=True
            )
