from django.db import models

# Create your models here.
class studs(models.Model):
    name=models.CharField(max_length=400)
    roll=models.IntegerField(primary_key=True,unique=True)
    email=models.EmailField(max_length=300,null=True,unique=True)
    def __str__(self):
        return f"{self.roll},{self.name}"