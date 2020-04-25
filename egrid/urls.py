from django.urls import path

from egrid import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('<int:pk>/', views.order, name='order'),
    path('maps', views.maps, name="maps"),
    path('login', views.login, name="login"),
    path('product/<int:pk>/', views.product, name='product'),
]
