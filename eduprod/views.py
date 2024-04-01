import random
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Card
from .forms import CardCheckForm

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    template_name = "eduprod/card_list.html"

class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    template_name = "eduprod/card_form.html"
    success_url = reverse_lazy("eduprod:card-list")

class CardUpdateView(UpdateView):
    model = Card
    fields = ["question", "answer", "box"]
    template_name = "eduprod/card_form.html"
    success_url = reverse_lazy("eduprod:card-list")

class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy("eduprod:card-list")

class BoxView(ListView):
    model = Card
    template_name = "eduprod/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        return redirect(request.META.get("HTTP_REFERER"))
