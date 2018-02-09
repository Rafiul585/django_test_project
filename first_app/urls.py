from django.urls import path
from . import  views



urlpatterns = (
    path('', views.myblog, name = 'myblog'),

)
