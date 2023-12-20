from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize>1000000000:
        raise ValidationError("maximum size is 1000 mb")