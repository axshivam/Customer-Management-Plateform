from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name= "home"),
    path('products/',views.product,name="products"),
    path('customer/<str:pk_test>/',views.customer,name="customer")

]
