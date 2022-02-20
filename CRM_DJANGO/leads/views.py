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
    return render(request, 'details_lead.html', lead_details)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print("receiving in a post request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = form.cleaned_data['Agent']
            # lead = Lead.objects.create(first_name=first_name, last_name=last_name, age=age, Agent=agent)
            return redirect("/leads")
    context = {
        "form": form,
    }
    return render(request, 'create_lead.html', context)

def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "lead": lead,
        "form": form
    }
    return render(request, 'update_lead.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect("/leads")