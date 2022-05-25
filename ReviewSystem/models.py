from django.db import models


# Create your models here.
class Candidate(models.Model):
    STATUS_CHOICES = (('applied', 'applied'), ('accepted', 'accepted'), ('rejected', 'rejected'))
    name = models.CharField(max_length=50)
    gmail = models.EmailField(max_length=50)
    experience = models.IntegerField()
    previous_company = models.CharField(max_length=60)
    college_name = models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="applied",choices=STATUS_CHOICES)
