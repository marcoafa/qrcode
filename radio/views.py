from django.shortcuts import render
from django.conf import settings
from .forms import EmailForm
from django.core.mail import EmailMessage
# Create your views here.
def index(request):
    return render(request,'index.html');

def interface(request):
    return render(request,'interface.html');

def send_email(request):
    if request.method != 'POST':
        form = EmailForm()
        context = {
            "form": form
        }
        return render(request,'email.html', context)

    form = EmailForm(request.POST, request.FILES)

    if form.is_valid():
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        email   = form.cleaned_data.get("email")
        a  = request.FILES['attach']


        mail = EmailMessage(subject,
            message,
            settings.EMAIL_HOST_USER,
            [email])
        #mail.attach_file(a.name, a.read(), a.content_type)
        mail.send()
        context ={
            "message": 'Sent email to %s' % email
        }
        return render(request,'email.html',context)



    return render(request,'email.html', {'message': 'Unable to send email. Please try again later'})
