#from django.contrib import admin
from django.urls import path
from Leads.views import lead_list, lead_detail

app_name = "Leads"

urlpatterns = [
    path('', lead_list),
    path('<pk>/', lead_detail )
]