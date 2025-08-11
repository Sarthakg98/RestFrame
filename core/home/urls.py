from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('student/', StudentListView.as_view(), name='student-list'),
    
]
