"""
URL configuration for project_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView, ProjectListCreateAPIView, ProjectListUserAPIView,  ClientDeleteAPIView

urlpatterns = [
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),
    path('clients/<int:pk>/projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/', ProjectListUserAPIView.as_view(), name='project-list-user'),
    path('clients/<int:pk>/delete/', ClientDeleteAPIView.as_view(), name='client-delete'),
]