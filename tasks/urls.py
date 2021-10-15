from django.urls import path
from . import views

# For setting up an URL Patterns/Routing

urlpatterns = [
    # For Index/ Home Page 
    path('', views.index, name="list"),
    
    # For UpdateTask
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    
    # For DeleteTask
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]