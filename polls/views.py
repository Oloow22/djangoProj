from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import loader
from .models import Question,Choice,Workout,Exercise,Set
from django.shortcuts import get_object_or_404,render,redirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import WorkoutForm,ExerciseForm,SetForm


def workout_list(request):
    workouts = Workout.objects.order_by("-date")
    context = {
        "workouts":workouts
    }
    return render(request,"polls/workouts.html",context)

def workout_detail(request,workout_id):
    workout = get_object_or_404(Workout, pk = workout_id)
    return render(request, "polls/workout_detail.html",{"workout":workout})

def add_workout(request):
    if request.method == "POST":
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save()

            exercises = request.POST.getlist('exercise[]')
            reps_list = request.POST.getlist('reps[]')
            weights_list = request.POST.getlist('weight[]')

            for i, exercise_name in enumerate(exercises):
                if exercise_name.strip():
                    exercise = Exercise.objects.create(workout=workout,exercise=exercise_name)
                    reps = reps_list[i] if i < len(reps_list) else None
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

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

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
