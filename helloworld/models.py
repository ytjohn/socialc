from django.db import models

# Create your models here.

class Greetings(models.Model):
    greeting = models.CharField(max_length=50)

    def __unicode__(self):
	return self.greeting


