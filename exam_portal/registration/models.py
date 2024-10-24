from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Extend the built-in User model to create custom user types
class User(AbstractUser):
    SUPER_ADMIN = 'super_admin'
    STATE_ADMIN = 'state_admin'
    DISTRICT_ADMIN = 'district_admin'
    UNIT_LEADER = 'unit_leader'
    MEMBER = 'member'

    USER_TYPES = [
        (SUPER_ADMIN, 'Super Admin'),
        (STATE_ADMIN, 'State Admin'),
        (DISTRICT_ADMIN, 'District Admin'),
        (UNIT_LEADER, 'Unit Leader'),
        (MEMBER, 'Member'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=MEMBER)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


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
    leader = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'user_type': User.UNIT_LEADER})
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return f"{self.name} - {self.leader.username}"


# Member Model (For Scout/Guide member registrations)
class Member(models.Model):
    SCOUT = 'scout'
    GUIDE = 'guide'
    
    MEMBER_TYPES = [
        (SCOUT, 'Scout'),
        (GUIDE, 'Guide'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPES)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='members')
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_member_type_display()})"


# Exam Registration Model
class ExamRegistration(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='exam_registrations')
    exam_name = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.member} - {self.exam_name} on {self.registration_date.strftime('%Y-%m-%d')}"

# Example of Custom Permissions
class MyPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.permission.name}"
