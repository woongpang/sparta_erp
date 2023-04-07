from django.urls import path
from . import views

urlpatterns = [
path("erp-in/", views.erp_in, name="erp-in"),
path("home/", views.gogohome, name='gogohome')
]