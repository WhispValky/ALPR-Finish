from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('HomePage/', views.HomePage, name='homepage'),
    path('HomePage/CarList/', views.thirdpage, name='Search'),
    path('HomePage/register/', views.register, name='register'),
    path("per_car/<int:pk>", views.per_car_view, name="per_car"),
    path("delete/<int:pk>", views.delete_car, name="delete"),
    path("update/<int:pk>", views.update_car, name="update"),
]