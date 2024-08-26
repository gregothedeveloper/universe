from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False, verbose_name= 'completed')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"Title: {self.title} \nStatus: {self.status}"