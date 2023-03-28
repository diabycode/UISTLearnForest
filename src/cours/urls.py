
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CoursList.as_view(), name='cours_list'),
    path('<str:slug>/details', views.CoursDetail.as_view(), name='cours_details'),
    path('<str:slug>/learn', views.CoursLearn.as_view(), name='cours_learn'),
    path('get/', views.get, name='get-courses'),
    path('items/<str:pk>/<str:type>/', views.get_item, name='get-item'),

]

