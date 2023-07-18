from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.view_contacts, name='view_contacts'),
    path('T6xyzeducation/', views.view_education, name='view_education'),
    path('aboutme/', views.view_aboutme, name='view_aboutme'),
    path('resume/', views.view_resume, name='view_resume' )
]