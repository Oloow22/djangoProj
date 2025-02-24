from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import loader
from .models import Question,Choice,Workout,Exercise,Set
from django.shortcuts import get_object_or_404,render,redirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import WorkoutForm,ExerciseForm,SetForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def workout_list(request):
    workouts = Workout.objects.order_by("-date")
    context = {
        "workouts":workouts
    }
    return render(request,"polls/workouts.html",context)

@login_required
def workout_detail(request,workout_id):
    workout = get_object_or_404(Workout, pk = workout_id)
    return render(request, "polls/workout_detail.html",{"workout":workout})

@login_required
def add_workout(request):
    if request.method == "POST":
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save()

            exercises = request.POST.getlist('exercise[]')
            reps_list = request.POST.getlist('reps[]')
            weights_list = request.POST.getlist('weight[]')
            sets_list = request.POST.getlist('sets[]')

            for i, exercise_name in enumerate(exercises):
                if exercise_name.strip():
                    sets = sets_list[i] if i < len(sets_list) else None
                    exercise = Exercise.objects.create(workout=workout,exercise=exercise_name,sets=sets)
                    reps = reps_list[i] if i < len(reps_list) else None
                    sets = sets_list[i] if i < len(sets_list) else None
                    weight = weights_list[i] if i < len(weights_list) else None
                    if reps:
                        try:
                            weight_value = float(weight) if weight else None
                        except ValueError:
                            weightht_value = None
                        Set.objects.create(exercise = exercise,reps = int(reps), weight=float(weight) if weight else None)
            
            return redirect(reverse('polls:workout_list'))

    else:
        workout_form = WorkoutForm()
    
    return render(request, 'polls/add_workout.html', {'workout_form':workout_form})



def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"You did not select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save() 

        return HttpResponseRedirect(reverse("polls:results",args = (question.id,)))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("polls:workout_list")
        else:
            messages.error(request,"Invalid username or password")
    
    return render(request,"polls/login.html")

def logout_view(request):
    logout(request)
    return redirect("polls:login")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request,"Passwords do not match")
            return redirect("polls:signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"User name already exists")
            return redirect("polls:signup")
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already in use")
            return redirect("polls:signup")
        
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save

        login(request,user)
        return redirect("polls:workout_list")
    
    return render(request,"polls/signup.html")