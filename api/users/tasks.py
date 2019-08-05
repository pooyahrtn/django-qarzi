from celery import shared_task

from stdimage.utils import render_variations


@shared_task
def process_photo_image(file_name, variations):
    render_variations(file_name, variations, replace=True)
