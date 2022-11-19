from django.db import models

# Create your models here.
class contact(models.Model):
    nom=models.CharField(max_length=40,null=True)
    prenom=models.CharField(max_length=60,null=True)
    numéro=models.CharField(max_length=40,null=True)
    email=models.EmailField(max_length=100,null=True)
    date_creation=models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.nom