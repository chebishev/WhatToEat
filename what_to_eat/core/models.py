from django.db import models
from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    calories = models.IntegerField(null=True, blank=True)
    
    is_breakfast = models.BooleanField(default=False)
    is_lunch = models.BooleanField(default=False)
    is_dinner = models.BooleanField(default=False)

    usage_count = models.PositiveIntegerField(default=0)  # Tracks how often this meal was suggested

    def __str__(self):
        return f"{self.name} for {self.user.username}"
    
    def increment_usage(self):
        self.usage_count += 1
        self.save()

