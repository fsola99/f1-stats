from django.shortcuts import render
from .models import Circuit, Constructor, Driver, Standing

# Home (Index)
def home(request):
    return render(request, 'index.html')

# Circuits
def circuits_view(request):
    circuits = Circuit.objects.all()
    return render(request, 'circuits.html', {'circuits': circuits})

# Constructors
def constructors_view(request):
    constructors = Constructor.objects.all()
    return render(request, 'constructors.html', {'constructors': constructors})

# Drivers
def drivers_view(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers.html', {'drivers': drivers})

# Standings
def standings_view(request):
    current_season = 2023  # Por ejemplo, o puede ser dinámico
    season = request.GET.get('season', current_season)  # Permitir cambiar de temporada
    standings = Standing.objects.filter(season=season)
    return render(request, 'standings.html', {'standings': standings, 'season': season})
