from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views,views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alprapp.urls')),
    path("", auth_views.LoginView.as_view(template_name = "car_system/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "car_system/logout.html"), name="logout"),
]
