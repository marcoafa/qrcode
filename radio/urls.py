from django.conf.urls import url
from . import views
from .views import index, interface, send_email

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^interface/$', views.interface, name='interface'),
    url(r'^send/$', views.send_email, name='send'),

)
