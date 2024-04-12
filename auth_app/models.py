from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Utilisateurs(models.Model):
    nom = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=30)

from django.db import models

class ElementGrille(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/téléchargement.png')  # Champ pour stocker l'image

# class CustomUser(AbstractUser):
#         photo = models.ImageField(upload_to='photos/', null=True, blank=True)
#
#
# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# class Group(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Permission(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class CustomUser(AbstractUser):
#     # Add your custom fields here
#     groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_groups')
#     user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_permissions')
#
#     class Meta:
#         swappable = 'AUTH_USER_MODEL'
