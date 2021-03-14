from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

# Create your views here.

def index(request):
    context = {"dojo_list": Dojos.objects.all()}
    return render(request, "main.html", context)

def process_dojo(request):
    if request.method == "POST":
        name = request.POST["name"]
        city = request.POST["city"]
        state = request.POST["state"]
        des = request.POST["desc"]

        Dojos.objects.create(name=name, city=city, state=state, desc=des)
    return redirect ('/')

def process_ninja(request):
    if request.method == "POST":
        first = request.POST["first"]
        last = request.POST["last"]
        dojo_id = request.POST["dojo"]

        Ninjas.objects.create(first_name=first, last_name=last, dojo=Dojos.objects.get(id=dojo_id))
    return redirect ('/')
