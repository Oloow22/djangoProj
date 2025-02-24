from django import forms
from .models import Workout,Exercise,Set

class WorkoutForm(forms.ModelForm):
    class Meta: 
        model = Workout
        fields = ['name','description','date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise','sets']

class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['reps','weight']