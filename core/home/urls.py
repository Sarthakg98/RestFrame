from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    #path('student/', StudentListCreateView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentUpdateView.as_view(),name='student_update'),
]
