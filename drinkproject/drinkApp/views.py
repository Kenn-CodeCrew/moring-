from django.shortcuts import render

from django.http import HttpResponse

# gunctions that are called or rendered on HTMl page
# Create your views here.
def index(request):
    context = "Hello Kenn"
    return render(request, "drinkApp/index.html")


def page2(request):
    context = "Hello Page2"
    return render(request, "drinkApp/page2.html" )

def page3(request):
    context = "Hello Page3"
    return render(request, "drinkApp/page3.html" )


def page4(request):
    context = "Hello Page4"
    return render(request, "drinkApp/page4.html" )

def page5(request):
    context = "Hello Page5"
    return render(request, "drinkApp/page5.html" )