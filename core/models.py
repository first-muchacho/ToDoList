from django.db import models
from users.models import CustomUser


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
