from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads" : leads
    }
   # return HttpResponse("Hello world!!")
    return render(request, "Leads/leads_list.html", context)

def lead_detail(request, pk): 
    lead = Lead.objects.get(id=pk)
    context = {
        "leads" : lead
    }
    return render(request, "Leads/lead_detail.html", context)