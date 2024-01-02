from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
   
   #This class here is created to avoid name conflicts from djangos built in library AbstractUser
    class Meta(AbstractUser.Meta):
        db_table = 'leads_user'
        permissions = [('can_view_leads', 'Can view leads')]
    
    # Override groups and user_permissions fields with unique related names
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='leads_user_groups'  # Set a custom related_name for groups
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='leads_user_permissions'  # Set a custom related_name for user_permissions
    )

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
  

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.user.username