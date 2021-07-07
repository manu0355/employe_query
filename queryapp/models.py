from django.db import models
from datetime import date

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    founder= models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_at = models.DateField()

    def __str__(self):
        return self.name

class Language(models.Model):
    l_name = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    date_created = models.DateField()

    def __str__(self):
        return self.l_name

class Programmer(models.Model):
    p_name = models.CharField(max_length=50)
    age = models.IntegerField()
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return self.p_name