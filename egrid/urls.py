from django.urls import path

from egrid import views

urlpatterns = [
    path('', views.index, name='index'),

]