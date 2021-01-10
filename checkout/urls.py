from django.urls import path

from checkout.views import *
 
urlpatterns=[
    path("<int:pay_id>",main,name="pay"),
    path("pay/<int:charge_id>",charge,name="charge")
    
    ]
