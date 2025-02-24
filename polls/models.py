import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=2000)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

class Workout(models.Model):
    name = models.CharField(max_length = 1000)
    description = models.CharField(max_length = 3000)
    date = models.DateTimeField("workout date")

    def __str__(self):
        return self.name

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=2000)
    sets = models.CharField(max_length=100)

    def __str__(self):
        return self.exercise

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    reps = models.IntegerField()
    weight = models.FloatField(null = True,blank = True)

