from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from display import map

def index(req):
    if req.method == "GET":
        map.returnMap()
        return render(req, "display/map.html")
    elif req.method == "POST":
        return 0
    print(req.method)

# Create your views here.
