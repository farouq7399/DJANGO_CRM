from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Agent, Lead
from .forms import LeadForm, LeadModelForm

def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    print(context)
    return render(request, 'home_page.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    lead_details = {
        "lead_details": lead
    }
    print(pk)
    return render(request, 'lead_details.html', lead_details)

def create_lead(request):
    form = LeadModelForm()
    if request.method == "POST":
        print("receiving in a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            lead = Lead.objects.create(first_name=first_name, last_name=last_name, age=age, Agent=agent)
            redirect("/")
    context = {
        "form": form,
    }
    return render(request, 'create_lead.html', context)
