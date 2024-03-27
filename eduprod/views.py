from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Flashcard
from .forms import CardForm


@login_required
def index(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect("index")
    else:
        form = SubjectForm()
    
    subjects = Subject.objects.filter(user=request.user)
    context = {
        'subjects': subjects,
        'form': form,
    }
    return render(request, "eduprod/index.html", context)

@login_required
def create_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect("eduprod:index")
    else:
        form = SubjectForm()
    return render(request, "eduprod/create_subject.html", {"form": form})

@login_required
def study_subject(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    flashcards = Flashcard.objects.filter(subject=subject, user=request.user)
    
    # Handle user responses
    if request.method == 'POST':
        flashcard_id = request.POST.get('flashcard_id')
        flashcard = Flashcard.objects.get(pk=flashcard_id)
        user_response = request.POST.get('user_response')  # 'correct' or 'incorrect'
        
        if user_response == 'correct':
            flashcard.correct_count += 1
        elif user_response == 'incorrect':
            flashcard.incorrect_count += 1
        flashcard.save()
    
    context = {"subject": subject, "flashcards": flashcards}
    return render(request, "eduprod/study_subject.html", context)


@login_required
def create_card(request):
    if request.method == "POST":
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.user = request.user
            flashcard.save()
            return redirect("eduprod:index")  # Redirect to the appropriate page
    else:
        form = CardForm()
    return render(request, "eduprod/create_card.html", {"form": form})
