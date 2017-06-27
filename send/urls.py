from django.conf.urls import url
from send import views

urlpatterns =[
    url(r'^$', views.send_sms, name='send_sms')
]