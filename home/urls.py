from django.urls import path

from home.views import *


urlpatterns=[
    path("",Index),
    path('search', search,name='search'),
    path('<int:flight_id>', delete,name='delete'),
    path('inv/<int:invoice_id>', invoice,name='invoice'),
    path('inv/mail/<int:mail_id>', mail,name='mail')
    ]