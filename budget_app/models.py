from django.db import models

# Create your models here.


class People(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    number = models.CharField(max_length = 20)

def __str__(self):
    return self.username

class Budget(models.Model):
    budget_amt = models.FloatField()
    date = models.DateField()
    category = models.CharField(max_length=15)

class Expense(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    desc = models.CharField(max_length=20)
    category = models.CharField(max_length=20)