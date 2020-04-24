from django.urls import path

from egrid import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us.html', views.about_us, name='about_us'),
    path('order.html', views.order, name='order')

]