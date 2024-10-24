from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    MemberCreateView,
    MemberListView,
    ExamRegistrationView,
    UnitListView,
    StateListView,
    DistrictListView,
    UnitDetailView,
)

urlpatterns = [
    # User Management
    path('users/', UserListView.as_view(), name='user-list'),  # List all users
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Detail view for a user

    # Member Management
    path('members/', MemberListView.as_view(), name='member-list'),  # List all members
    path('members/create/', MemberCreateView.as_view(), name='member-create'),  # Create a new member

    # Exam Registration
    path('exams/register/', ExamRegistrationView.as_view(), name='exam-registration'),  # Exam registration

    # Units Management
    path('units/', UnitListView.as_view(), name='unit-list'),  # List all units
    path('units/<int:pk>/', UnitDetailView.as_view(), name='unit-detail'),  # Detail view for a unit

    # State and District Management
    path('states/', StateListView.as_view(), name='state-list'),  # List all states
    path('districts/', DistrictListView.as_view(), name='district-list'),  # List all districts
]
