from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from .models import Lead
from .forms import LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# sign up class
class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')


#Class Based views CRUD+L using django.view.generic
class LandingPageView(TemplateView):
    template_name = 'landing.html'

class LeadListView(ListView):
    template_name = 'home_page.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'

class LeadDetailsView(DetailView):
    template_name = 'details_lead.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead_details'

class LeadCreateView(CreateView):
    template_name = 'create_lead.html'
    form_class = LeadModelForm
    context_object_name = "leads"

    def get_success_url(self):
        return reverse("home_page")

    def form_valid(self, form):
        # TODO SEND EMAIL
        send_mail(
            subject="A lead has been created",
            message="Go to the site to find the new lead!",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(UpdateView):
    template_name = 'update_lead.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name = 'lead'

    def get_success_url(self):
        return reverse('home_page')

class LeadDeleteView(DeleteView):
    template_name = 'delete_lead.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return redirect("home_page")


# Function Based Views
def landing_page(request):
    return render(request, 'landing.html')

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



