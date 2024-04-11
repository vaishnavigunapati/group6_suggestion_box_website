from django.urls import path
from suggestions import views

urlpatterns = [
    path('', views.suggestion_list, name='suggestion_list'),
    path('submit/', views.suggestion_submit, name='suggestion_submit'),
]
