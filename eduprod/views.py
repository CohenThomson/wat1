from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "eduprod/index.html")

def create_card(request):
    if request.method == "POST":
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("eduprod:index") #send where urls.py?
    else:
        form = CardForm()
    return render(request, "eduprod/create_card.html", {"form": form})