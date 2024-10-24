from django.db import models
from accounts.models import Member, UnitLeader    
class Exam(models.Model): 
    name = models.CharField(max_length=100) 


# Exam Registration Model
class ExamRegistration(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='exam_registrations')
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    registered_by = models.ForeignKey(UnitLeader, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.member} - {self.exam_name} on {self.registration_date.strftime('%Y-%m-%d')}"
