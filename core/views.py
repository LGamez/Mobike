from django.shortcuts import render, HttpResponse
from .forms import PortafolioForm
from .models import Portafolio

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    
    user = request.user
    
    if user.has_perm('core.profesor'):
        
        portafolios = Portafolio.objects.all()
        
        return render(request, "core/portfolio.html", {'portafolios':portafolios})
    else:
        return render(request, "core/portfolio.html")
        
def contact(request):
    return render(request, "core/contact.html")

def coontacto2(request):
    form = PortafolioForm()
    return render(request, "core/editar.html", {'form': form})