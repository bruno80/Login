from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('list/', views.list),
  path('delete/<int:user_id>/', views.user_delete)
]