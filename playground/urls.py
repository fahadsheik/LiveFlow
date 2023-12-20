from django.urls import path
from . import views

urlpatterns = [
    path("", views.empty),
    path("playground/online/", views.sayhello),
    path("playground/contact/", views.don),
    path("playground/online/animation.html", views.animation),
    path("playground/online/music.html", views.music),
    path("playground/online/cinema.html", views.cinema),
    path("playground/online/drama.html", views.drama),
    path("playground/online/popwin.html", views.popwin),
    path("playground/online/test.html", views.test),
    path("playground/online/add/", views.index),
    path("playground/online/success.html", views.success)
    ]