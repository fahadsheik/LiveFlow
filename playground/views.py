from django.shortcuts import render
from django.http import HttpResponse
from .models import Video_form
from .models import Video
# Create your views here.
def index(request):
    print("Hello Ramesh")
    all_video=Video.objects.all()
    if request.method=="POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Uploaded successfully</h1>")
        #to satisfy the viewer's interest
       # return HttpResponse("<h1> Uploaded successfully your content will be added after review by the admin</h1>")
    else:
        form=Video_form()
    return render(request,"online.html",{"form":form, "all":all_video})

def sayhello(request):
    print("Hello world")
    if "avengers" in request.META['QUERY_STRING']:
        return render(request, "avengers.html")
    elif "justice+league" in request.META['QUERY_STRING']:
        return render(request, "justiceleague.html")
    elif "ironman" in request.META['QUERY_STRING']:
        return render(request, "ironman.html")
    elif "captain+america" in request.META['QUERY_STRING']:
        return render(request, "captain.html")
    elif "thor" in request.META['QUERY_STRING']:
        return render(request, "thor.html")
    elif "superman" in request.META['QUERY_STRING']:
        return render(request, "superman.html")
    elif "batman" in request.META['QUERY_STRING']:
        return render(request, "batman.html")
    elif "flash" in request.META['QUERY_STRING']:
        return render(request, "flash.html")
    elif "wonderwoman" in request.META['QUERY_STRING']:
        return render(request, "wonderwoman.html")
    else:
        return render(request, "online.html")


def empty(request):
    return render(request, "home.html")

def don(request):
    return render(request, "contact.html")

def animation(request):
    return render(request, "animation.html")

def music(request):
    return render(request, "music.html")

def drama(request):
    return render(request, "drama.html")

def cinema(request):
    return render(request, "cinema.html")

def popwin(request):
    return render(request, "popwin.html")


def test(request):
    return render(request, "test.html")


def index(request):
    video=Video.objects.all()
    return render(request, "upload.html", {"video": video})

def success(request):
    return render(request, "success.html")