from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import file_size



class Video(models.Model):
    caption = models.CharField(max_length=500)
    Video = models.FileField(upload_to='playground/media/%y',validators=[file_size])

    def __str__(self):
        return self.caption


class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ("caption","Video")
