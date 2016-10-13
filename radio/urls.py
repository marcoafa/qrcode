from django.conf.urls import url
from . import views
from .views import index, interface

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^interface/$', views.interface, name='interface'),

)
