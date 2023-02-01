from django.urls import path
from module import views

app_name = 'module'
urlpatterns = [
    path('', views.index, name='index'),
]