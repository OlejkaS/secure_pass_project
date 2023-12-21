from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('password_generate/', views.password_generate, name='generator'),
    path('pass/<slug:pass_slug>/', views.show_post, name='pass'),
    
]
