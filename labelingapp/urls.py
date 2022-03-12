from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views


app_name = 'labelingapp'

urlpatterns = [

    path('work/', views.labeling_work, name='work'),
    path('inspect/', views.labeling_inspect, name='inspect')

]
