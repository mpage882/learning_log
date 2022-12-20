from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Models are classes in Django
class Topic(models.Model):
    # A topic the user is learning about - listing 2 attributes

    # "Use CharField when wanting to store a small amount of text (ex. name, city, text)"
    text = models.CharField(max_length=200)

    # "Records date and time and 'auto_now_add' automatically sets date/tie to current"
    date_added = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # "Returns a string representation of the model"
        return self.text

class Entry(models.Model):

    """Something specific learned about a topic"""
    # ForeignKey connects each entry to a specific topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #When a topic is deleted, all entries are too
    # Instance of TextField
    text = models.TextField()
    # Allows entries to list in order
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # Tells Django to show the first 50 characters
        return f"{self.text[:50]}..."