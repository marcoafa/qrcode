from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html');

def interface(request):
    return render(request,'interface.html');
