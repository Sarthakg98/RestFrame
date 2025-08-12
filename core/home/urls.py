from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

#create the router and register the CourseViewSet
router =DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    #path('student/', StudentListCreateView.as_view(), name='student-list'),
    #path('student/<int:pk>/', StudentUpdateView.as_view(),name='student_update'),
    path('students/', student_list_create, name='student-list-create'),
    path('students/<uuid:pk>/',student_detail, name='student-detail'),
    
    #include CourseViewSet routes
    path('', include(router.urls)),
]



