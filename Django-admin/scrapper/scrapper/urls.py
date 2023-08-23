# myapp/urls.py

from django.urls import path
from myapp import views

urlpatterns = [
    path('jobs/', views.job_list, name='job_list'),
    path('search/', views.search_jobs, name='search_jobs'),
]
