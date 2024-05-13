# admin.py

from django.contrib import admin
from .models import Question, Option, Score, QuizAttempt,Feedback

# Custom admin class for Question model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)

# Register your models with custom admin classes
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Score)
admin.site.register(QuizAttempt)
admin.site.register(Feedback)