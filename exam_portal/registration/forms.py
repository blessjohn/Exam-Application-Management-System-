from django import forms
from .models import Member, ExamRegistration

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'member_type', 'unit']  # Adjust fields as necessary
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'member_type': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit'].queryset = Unit.objects.all()  # Modify to fetch units based on user type if needed


class ExamRegistrationForm(forms.ModelForm):
    class Meta:
        model = ExamRegistration
        fields = ['member', 'exam_name']  # Adjust fields as necessary
        widgets = {
            'member': forms.Select(attrs={'class': 'form-control'}),
            'exam_name': forms.TextInput(attrs={'placeholder': 'Exam Name'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['member'].queryset = Member.objects.all()  # Modify to filter members as needed
