from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.firstView),
    path('now_date/', views.datetimeView),
    path('goodbye/', views.goodbyeView),
]