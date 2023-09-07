from django.shortcuts import render
from .models import Team

# Create your views here.
def about(request):
    team=Team.objects.all()
    return render(request,"about/about.html",{'team': team})



