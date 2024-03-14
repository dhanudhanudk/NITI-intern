from django.db import models



# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=200,null=True)
    class Meta:
        db_table = "registration"
