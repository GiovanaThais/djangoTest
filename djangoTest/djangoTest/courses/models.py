from django.db import models

class Course(models.Model):

    name = models.CharField( max_length=100)
    numero = models.CharField(max_length=10) #duração do curso
    description = models.TextField(max_length=200)


