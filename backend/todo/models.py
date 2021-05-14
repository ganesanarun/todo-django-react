from django.db import models

# Create your models here.


class Todo(models.Model):
    title: str = models.CharField(max_length=120)
    description: str = models.TextField()
    completed: bool = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
