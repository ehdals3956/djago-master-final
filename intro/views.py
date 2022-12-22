from django.shortcuts import render


def index(req):
    return render(req, "intro/index.html")

def page(req):
    return render(req, "intro/page.html")
# Create your views here.
