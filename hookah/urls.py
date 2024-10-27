from django.urls import path
from hookah.views import TobaccoCreate
from . import views

urlpatterns = [
    path('', views.hookahList, name='hookahList'),
    path('hookah', views.hookahList, name='hookahList'),
    path('tobaccoCreate', TobaccoCreate.as_view(), name='tobaccoCreate'),
]