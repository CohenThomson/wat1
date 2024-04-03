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
from django.contrib.auth.decorators import login_required

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    template_name = "eduprod/card_list.html"
    #Displays a list of flashcards sorted by box number and creation date.

class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    template_name = "eduprod/card_form.html"
    success_url = reverse_lazy("eduprod:card-list")
    #Provides a form for creating new flashcards.

class CardUpdateView(UpdateView):
    model = Card
    fields = ["question", "answer", "box"]
    template_name = "eduprod/card_form.html"
    success_url = reverse_lazy("eduprod:card-list")
    #Provides a form for updating existing flashcards.

class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy("eduprod:card-list")
    #Deletes existing flashcards.
    
class BoxView(ListView):
    model = Card
    template_name = "eduprod/box.html"
    form_class = CardCheckForm
    #Displays flashcards belonging to a specific box and allows checking them randomly.

    def get_querysaet(self):
        return Card.objects.filter(box=self.kwargs["box_num"])
    #Retrieves flashcards belonging to the specified box number.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    #Adds the box number and a randomly chosen flashcard to the context.

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        return redirect(request.META.get("HTTP_REFERER"))
    #Handles form submission, but currently redirects to the previous page.


#Overall, this code implements views for listing, creating, updating, and deleting flashcards, as well as a specialized view for managing flashcards within specific boxes.