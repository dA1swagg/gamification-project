from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Question, Score
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('/')
def index(request):
    return render(request, 'quiz_game/index.html')
def contact(request):
    return render(request, "quiz_game/contact.html")
def about(request):
    return render(request, "quiz_game/about.html")
def guidelines(request):
    return render(request, "quiz_game/guidelines.html")
def testimonial(request):
    return render(request, "quiz_game/testimonial.html")
def view_scoreboard(request):
    # Retrieve the scoreboard data from the database
    scoreboard = Score.objects.order_by('-score')[:10]  # Assuming you want the top 10 scores
    
    # Pass the scoreboard data to the template
    return render(request, 'quiz_game/scoreboard.html', {'scoreboard': enumerate(scoreboard, start=1)})

from django.db.models import F

def home(request):
    # Fetch the top 10 scores in descending order
    scoreboard = Score.objects.order_by('-score')[:10]
    # Add rank to each score
    for index, score in enumerate(scoreboard, start=1):
        score.rank = index
    context = {
        'scoreboard': scoreboard
    }
    return render(request, 'quiz_game/home.html', context)

@login_required
def quiz(request):
    if request.method == 'POST':
        # Handle form submission here if needed
        pass
    # Get all questions from the database
    questions = Question.objects.all()
    
    # If there are no questions, redirect to the score page
    if not questions:
        return redirect('score')
    
    # Otherwise, render the quiz page with the questions
    context = {'questions': questions}
    return render(request, 'quiz_game/quiz.html', context)

@login_required
def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = int(key.replace('question', ''))
                selected_option_id = int(value)
                question = Question.objects.get(id=question_id)
                correct_option = question.option_set.filter(is_correct=True).first()
                if correct_option and selected_option_id == correct_option.id:
                    score += 100
        # Save the score associated with the authenticated user
        Score.objects.create(user=request.user, score=score)
        return redirect('score')
    return redirect('home')

from .forms import FeedbackForm

@login_required
def score(request):
    # Retrieve the user's latest score
    user_score = Score.objects.filter(user=request.user).latest('id')
    score = user_score.score
    
    # Calculate the number of correct answers
    correct_answers = score // 100

    # Determine if the user passed the quiz
    passed = correct_answers >= 3

    # Create an instance of the feedback form
    feedback_form = FeedbackForm()

    if request.method == 'POST':
        # If the form is submitted, bind the POST data to the form
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            # If the form is valid, save the feedback along with the user details
            feedback = feedback_form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            # Optionally, you can add a success message here
            messages.success(request, 'Thank you for your feedback!')

            # Redirect the user to a relevant page
            return redirect('home')  # Change 'home' to the URL name of your home page

    context = {
        'score': score,
        'correct_answers': correct_answers,
        'passed': passed,
        'feedback_form': feedback_form
    }
    return render(request, 'quiz_game/score.html', context)

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('video')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def video(request):
    # Here you can render the video watching page
    return render(request, 'quiz_game/video.html')

from django.http import JsonResponse
from .models import Score

def save_score(request):
    if request.method == 'POST' and request.is_ajax():
        username = request.POST.get('username')
        score = int(request.POST.get('score'))
        Score.objects.create(user__username=username, score=score)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

from .models import Feedback

def view_feedbacks(request):
    # Fetch all feedback from the database
    feedbacks = Feedback.objects.all()
    context = {'feedbacks': feedbacks}
    return render(request, 'quiz_game/view_feedbacks.html', context)