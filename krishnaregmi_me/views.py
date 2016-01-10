from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "krishnaregmi_me/index.html")
    #return HttpResponse("Hello World")