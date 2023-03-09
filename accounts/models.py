from django.db import models

class registery(models.Model):
    ROLE_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer')
    )
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phoneno = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    QUESTION_CHOICES = (
        ('nm', 'What is your favourite name ?'),
        ('no', 'What is your favourite number ?'),
        ('th', 'What is your favourtie thing ?')
    )
    question = models.CharField(max_length=100, choices=QUESTION_CHOICES)
    answer = models.CharField(max_length=100)
    role = models.CharField(max_length=11, choices=ROLE_CHOICES)
    terms = models.BooleanField(default=False)

