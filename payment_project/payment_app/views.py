import stripe

from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=10000,
            currency='inr',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        print(charge)
        return render(request, 'charge.html')
