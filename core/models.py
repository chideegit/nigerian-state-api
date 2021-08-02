from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def __str__(self):
        return self.state_name

class Governor(models.Model):
    state = models.OneToOneField(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    