from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.conf import settings
from .models import regiester_page,Question, Option,UserResponse
import os
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError

# Create your views here.

def regiester(request):
    if request.method=='POST':
        # userid=request.POST['userid']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password!=confirm_password:
            messages.error(request,'Password does not match')
            return redirect('signup')
        
        if regiester_page.objects.filter(email=email).exists():
            messages.error(request,'Email already exits')
            return redirect('login')
        database_store = regiester_page(username=username,email=email,password=password)
        database_store.save()
        messages.success(request,'Regiester Successfully')
        return redirect('login')
    
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        try:
            take_data=regiester_page.objects.get(email=email)
            if take_data.password==password:
                request.session['email']=email
                request.session['username']=take_data.username
                request.session['is_logged_in']=True
                return redirect('student')
            else:
                messages.error(request,'Incorrect Password')
        except:
            messages.error(request,'Incorrect Email')

    return render(request,'login.html')

def loggout(request):
    request.session.flush()
    return redirect('index1')

def admin(request):
    return render(request,'admin1.html')

def index(request):
    return render(request,'index1.html')

def out(request):
    return render(request,'out.html')

def ques(request):
    return render(request,'ques.html')

def quiz(request):
    return render(request,'quiz.html')

def result(request):
    return render(request,'result.html')

def student(request):
    return render(request,'student.html')

def economics(request):
    questions = Question.objects.filter(page='economic')
    return render(request, 'eco.html', {'questions': questions})

def sci(request):
    questions = Question.objects.filter(page='science')
    return render(request, 'science.html', {'questions': questions})

def art(request):
    questions = Question.objects.filter(page='arts')
    return render(request, 'arts.html', {'questions': questions})

def politic(request):
    questions = Question.objects.filter(page='politics')
    return render(request, 'politics.html', {'questions': questions})

def clutures(request):
    questions = Question.objects.filter(page='cluture')
    return render(request, 'cluture.html', {'questions': questions})

def his(request):
    questions = Question.objects.filter(page='history')
    return render(request, 'history.html', {'questions': questions})

def quiz_form(request):
    questions = Question.objects.filter(page='history')
    return render(request, 'quiz_form.html', {'questions': questions})

def quiz_submission(request):
    if request.method == 'POST':
        questions = Question.objects.all()
        correct_count = 0
        total_questions = questions.count()
        email = request.session.get('email')  # Get email from session

        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                selected_option = get_object_or_404(Option, id=selected_option_id)
                is_correct = selected_option.is_correct

                try:
                    # Create or update the UserResponse for this user and question
                    user_response, created = UserResponse.objects.update_or_create(
                        email=email,
                        question=question,
                        defaults={
                            'selected_option': selected_option,
                            'is_correct': is_correct
                        }
                    )
                    
                    if is_correct:
                        correct_count += 1
                        
                except IntegrityError:
                    # Handle unique constraint violation gracefully
                    pass

        # Calculate average score
        average_score = round((correct_count / total_questions) * 100, 2) if total_questions > 0 else 0
        messages.success(request, "Your Quiz question  submitted successfully! Try the other topic questions.")
        return redirect('quiz')

        # return render(request, 'results.html', {
        #     'correct_count': correct_count,
        #     'total_questions': total_questions,
        #     'average_score': average_score
        # })

    return render(request, 'quiz_form.html', {'questions': Question.objects.all()})

def per(request):
    user_email = request.session.get('email')  # Get the email from session
    if user_email:  # Ensure the user is logged in
        # Filter UserResponse by the session email
        user_responses = UserResponse.objects.filter(email=user_email)
        total_attempts = user_responses.count()  # Total responses recorded by this user
        correct_answers = user_responses.filter(is_correct=True).count()  # Count of correct answers by this user

        # Calculate average score percentage
        average_score = round((correct_answers / total_attempts) * 100, 2) if total_attempts > 0 else 0
    else:
        total_attempts = 0
        correct_answers = 0
        average_score = 0

    return render(request, 'per.html', {
        'correct_answers': correct_answers,
        'total_attempts': total_attempts,
        'average_score': average_score,
    })



