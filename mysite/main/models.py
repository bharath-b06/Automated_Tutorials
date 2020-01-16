from django.db import models
from datetime import datetime
# Create your models here.
class Tutorial(models.Model,Question):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published",default=datetime.now)

    def __str__(self):
        return self.tutorial_title

class Question(models.Model):
    question = models.CharField(...)

class Choice(models.Model):
    question = models.ForeignKey("Question", related_name="choices")
    choice = modelsCharField("Choice", max_length=50)
    position = models.IntegerField("position")

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"), 
            # no duplicated position per question 
            ("question", "position") 
        ]
        ordering = ("position",)