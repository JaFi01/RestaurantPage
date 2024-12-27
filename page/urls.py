from smok.page import views
from django.urls import path


urlpatterns = [
    path('/', views.smok, name='mainpage'),
    path('menu/', views.menu, name='menu'),
    path('kontakt/', views.kontakt, name='kontakt'),

]
