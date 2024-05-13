from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    text = models.CharField(max_length=255)
    scene_title = models.CharField(max_length=100)  # Title of the scene


class QuizAttempt(models.Model):
    user = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    passed = models.BooleanField(default=False)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
# Add this model to your models.py file
from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"