from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Extend the built-in User model to create custom user types
class User(AbstractUser):
    bsg_uid = models.CharField(max_length=20)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class StateAdmin(User):
    designation = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'State Admin'
        verbose_name_plural = 'State Admins'

    def __str__(self):
        return self.username
    
class DistrictAdmin(User):
    designation = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'District Admin'
        verbose_name_plural = 'District Admins'

    def __str__(self):
        return self.username
    
class UnitLeader(User):
    warrant_number = models.CharField(max_length=200) 
    date_of_issue = models.DateField()
    validity = models.DateField()
    unit_address = models.TextField()
    charter_number = models.CharField(max_length=200)
    date_of_charter_issue = models.DateField()
    class Meta:
        verbose_name = 'Unit Leader'
        verbose_name_plural = 'Unit Leaders'
    def __str__(self):
        return self.username
    
# State Model
class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# District Model
class District(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return f"{self.name} ({self.state.name})"


# Unit Model (Represents a Unit Leader's group)
class Unit(models.Model):
    name = models.CharField(max_length=100)
    leader = models.OneToOneField(User, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return f"{self.name} - {self.leader.username}"


# Member Model (For Scout/Guide member registrations)
class Member(models.Model):

    MEMBER_TYPES = [
        ('scout', 'Scout'),
        ('guide', 'Guide'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPES)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='members')
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_member_type_display()})"