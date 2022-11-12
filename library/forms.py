from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import BookOutLoan, UserProfile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
        field_classes = {'username': UsernameField}
        
      
class LoanBookForm(forms.ModelForm):
    # return_date = forms.DateField()
    class Meta:
        model = BookOutLoan
        fields = ["check_out_book"]


class UserProfileModelForm(forms.ModelForm):
    # return_date = forms.DateField()
    class Meta:
        model = UserProfile
        fields = ["phone_number", "date_of_birth", "profile_photo"]

