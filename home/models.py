from django.db import models

# Create your models here.
class Client (models.Model):

    CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    )


    client=models.CharField(max_length=64)
    project=models.CharField(max_length=64)
    value=models.BigIntegerField(default=0)
    status=models.CharField(max_length=64, default="pending", choices=CHOICES)
    mail=models.CharField(max_length=64)
    
