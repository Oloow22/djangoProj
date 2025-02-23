from django.urls import path,include

from . import views

app_name = "polls"

urlpatterns = [
    path("polls/",views.IndexView.as_view(),name = "index"),
    path("workouts/",views.workout_list, name = "workout_list"),
    path("<int:workout_id>", views.workout_detail, name = "workout_detail"),
    path("add-workout/",views.add_workout,name ="add_workout"),
    path("polls/<int:pk>",views.DetailView.as_view(), name = "detail"),
    path("polls/<int:pk>/results",views.ResultsView.as_view(),name = "results"),
    path("polls/<int:question_id>/vote",views.vote,name = "vote"),
]