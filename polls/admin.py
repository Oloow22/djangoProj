from django.contrib import admin


from .models import Question,Choice,Workout,Excercise,Set

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Workout)
admin.site.register(Excercise)
admin.site.register(Set)
