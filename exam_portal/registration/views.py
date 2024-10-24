from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import User, Member, Unit, ExamRegistration, State, District
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import User, Member, Unit, ExamRegistration
from .forms import MemberForm, ExamRegistrationForm


# User List View
class UserListView(ListView):
    model = User
    template_name = 'registration/user_list.html'  # Create this template
    context_object_name = 'users'


# User Detail View
class UserDetailView(DetailView):
    model = User
    template_name = 'registration/user_detail.html'  # Create this template
    context_object_name = 'user'
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import User, Member, Unit, ExamRegistration, State, District
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .forms import MemberForm, ExamRegistrationForm

# User List View
class UserListView(ListView):
    model = User
    template_name = 'registration/user_list.html'  # Create this template
    context_object_name = 'users'


# User Detail View
class UserDetailView(DetailView):
    model = User
    template_name = 'registration/user_detail.html'  # Create this template
    context_object_name = 'user'


# Member List View
class MemberListView(ListView):
    model = Member
    template_name = 'registration/member_list.html'  # Create this template
    context_object_name = 'members'


# Create Member View
class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm  # Use the form class instead of fields
    template_name = 'registration/member_form.html'  # Create this template
    success_url = reverse_lazy('member-list')

    def form_valid(self, form):
        form.instance.registered_by = self.request.user  # Set the current user as the registrant
        return super().form_valid(form)


# Exam Registration View
class ExamRegistrationView(CreateView):
    model = ExamRegistration
    form_class = ExamRegistrationForm  # Use the form class instead of fields
    template_name = 'registration/exam_registration.html'  # Create this template
    success_url = reverse_lazy('exam-registration')  # Redirect after successful registration

    def form_valid(self, form):
        form.instance.registered_by = self.request.user  # Set the current user as the registrant
        return super().form_valid(form)


# Unit List View
class UnitListView(ListView):
    model = Unit
    template_name = 'registration/unit_list.html'  # Create this template
    context_object_name = 'units'


# Unit Detail View
class UnitDetailView(DetailView):
    model = Unit
    template_name = 'registration/unit_detail.html'  # Create this template
    context_object_name = 'unit'


# State List View
class StateListView(ListView):
    model = State
    template_name = 'registration/state_list.html'  # Create this template
    context_object_name = 'states'


# District List View
class DistrictListView(ListView):
    model = District
    template_name = 'registration/district_list.html'  # Create this template
    context_object_name = 'districts'


# Member List View
class MemberListView(ListView):
    model = Member
    template_name = 'registration/member_list.html'  # Create this template
    context_object_name = 'members'


# Create Member View
class MemberCreateView(CreateView):
    model = Member
    template_name = 'registration/member_form.html'  # Create this template
    fields = ['first_name', 'last_name', 'member_type', 'unit']  # Define fields here
    success_url = reverse_lazy('member-list')

    def form_valid(self, form):
        form.instance.registered_by = self.request.user  # Set the current user as the registrant
        return super().form_valid(form)


# Exam Registration View
class ExamRegistrationView(CreateView):
    model = ExamRegistration
    template_name = 'registration/exam_registration.html'  # Create this template
    fields = ['member', 'exam_name']  # Define fields here
    success_url = reverse_lazy('exam-registration')  # Redirect after successful registration

    def form_valid(self, form):
        form.instance.registered_by = self.request.user  # Set the current user as the registrant
        return super().form_valid(form)


# Unit List View
class UnitListView(ListView):
    model = Unit
    template_name = 'registration/unit_list.html'  # Create this template
    context_object_name = 'units'


# Unit Detail View
class UnitDetailView(DetailView):
    model = Unit
    template_name = 'registration/unit_detail.html'  # Create this template
    context_object_name = 'unit'


# State List View
class StateListView(ListView):
    model = State
    template_name = 'registration/state_list.html'  # Create this template
    context_object_name = 'states'


# District List View
class DistrictListView(ListView):
    model = District
    template_name = 'registration/district_list.html'  # Create this template
    context_object_name = 'districts'

class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'registration/member_form.html'
    success_url = reverse_lazy('member-list')

    def form_valid(self, form):
        form.instance.registered_by = self.request.user  # Set the current user as the registrant
        return super().form_valid(form)

class ExamRegistrationView(CreateView):
    model = ExamRegistration
    form_class = ExamRegistrationForm
    template_name = 'registration/exam_registration.html'
    success_url = reverse_lazy('exam-registration')

    def form_valid(self, form):
        form.instance.registered_by = self.request.user  # Set the current user as the registrant
        return super().form_valid(form)

# Optionally, you can add ListView or DetailView classes here as needed for your application
   