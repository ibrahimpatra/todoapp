from django.db import models

# Create your models here.

class Task(models.Model):
  # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
  # category = models.CharField(max_length=10)
  
  
      
  def __str__(self):
    return self.title