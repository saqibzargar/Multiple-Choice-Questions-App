from django.db import models

# Create your models here.


class Question(models.Model):
    questionText = models.CharField(max_length=500)
    opt1 =models.CharField(max_length=50)
    opt2 =models.CharField(max_length=50)
    opt3 =models.CharField(max_length=50)
    opt4 =models.CharField(max_length=50)
    answer =models.CharField(max_length=50)


class Qno:
    value = 1

class marksObtained:
    value = 0