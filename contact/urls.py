
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.acceuil,name='acceuil'),
    path('contact/<str:pk>/',views.liste_contact,name='details'),
    path('contact/ajouter_contact/',views.ajouter_contact,name='ajouter_contact'),
    path('contact/modifier_contact/<str:pk>/',views.modifier_contact,name='modifier_contact'),
]
