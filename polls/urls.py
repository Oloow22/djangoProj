from django.urls import path,include

from . import views

app_name = "polls"

urlpatterns = [
    path("", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("workouts/",views.workout_list, name = "workout_list"),
    path("<int:workout_id>", views.workout_detail, name = "workout_detail"),
    path("add-workout/",views.add_workout,name ="add_workout"),
   
]