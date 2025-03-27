from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator
import datetime
# Create your models here.
class regiester_page(models.Model):
    # userid = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(6)],
        default="defaultpass123"  # Add a default password
    )


class Question(models.Model):
    text = models.TextField()
    page = models.CharField(max_length=100,null=True)  # Different quiz topics

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255,null=True)
    is_correct = models.BooleanField(default=False)  # Marks the correct answer

class UserResponse(models.Model):
    user = models.ForeignKey(regiester_page, null=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    selected_option = models.ForeignKey(Option, null=True, on_delete=models.CASCADE)  # Allow NULL temporarily
    is_correct = models.BooleanField(default=False)
    email = models.EmailField(max_length=50, null=True)

  # Allow NULL temporarily



