from django.shortcuts import render, HttpResponse, get_object_or_404
from django.conf import settings
from .forms import EmailForm, Usform
from django.core.mail import EmailMessage
from .models import Us
import json
# Create your views here.
def index(request):

    return render(request,'index.html');

def interface(request):
    return render(request,'interface.html');

def send(request):
    status="good"

    if request.method == "POST":
        name = request.POST.get('name')
        passw = request.POST.get('password')
        fil = Us.objects.filter(user=name)
        instance = get_object_or_404(Us,user=name)
        form = Usform(instance=instance)
        response_data={}
        if fil.exists():
            response_data['result']='usuario Valido'
            instance = form.save(commit=False)
            instance.valid = True
            instance.save()
        else:
            response_data['result']='usuario no Valido'
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        status = "Bad"
        ctx = {
        "status":status
        }
        return HttpResponse(json.dumps(ctx),content_type="application/json")
    
def checked(request):
    check = Us.objects.filter(valid=True)
    ctx={
        'check':check
    }
    return render(request,'check.html',ctx)
