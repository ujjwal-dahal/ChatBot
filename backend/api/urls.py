from django.urls import path
from . import views

urlpatterns = [
    path("", views.CompanyInformationAPI.as_view(), name="company_info_api"),
    path('train-bot/', views.TrainBotAPI.as_view(), name="train_bot"),
]
