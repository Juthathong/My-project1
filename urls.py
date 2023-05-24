from django.urls import path
from myhotel import views

urlpatterns = [
    path('',views.index),
    path('accommodation',views.accommodation),
    path('form',views.form)
]