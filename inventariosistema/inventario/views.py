from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "inventario/index.html")

# Si tienes otras vistas, también deben estar decoradas con `login_required`
