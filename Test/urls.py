from django.urls import path, include
from Test import views

urlpatterns = [
    path('get_html', views.return_html, name='http')
]