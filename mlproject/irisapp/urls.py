from django.urls import path
from irisapp import views

urlpatterns=[
    path('',views.predict , name='predict'),
    path('result',views.forminfo,name='result')
]