from django.shortcuts import render


# Fonction to render homepage
def home(request):
    return render(request, 'home.html')


# Fonction to render opportunities
def opportunities(request):
    return render(request, 'opportunities.html')
