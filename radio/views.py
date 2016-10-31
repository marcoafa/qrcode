from django.shortcuts import render, HttpResponse
from django.conf import settings
from .forms import EmailForm
from django.core.mail import EmailMessage
from .models import Us
import json
# Create your views here.
def index(request):

    return render(request,'index.html');

def interface(request):
    return render(request,'interface.html');

def send(request):
    if request.method == "POST":
        name = request.POST.get('name')
        passw = request.POST.get('password')
        status = "Good"
        response_data={}
        response_data['result']='exito'
        ctx = {
        "status":status
        }
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        status = "Bad"
        ctx = {
        "status":status
        }
        return HttpResponse(json.dumps(ctx),content_type="application/json")
