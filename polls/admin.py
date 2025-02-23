from django.contrib import admin


from .models import Question,Choice,Workout,Exercise,Set

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Set)
