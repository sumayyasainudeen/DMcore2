
from django import template
from os.path import splitext

register = template.Library()


@register.filter
def file_extension_is_image(file_name):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    file_extension = splitext(file_name)[1].lower()
    return file_extension in image_extensions