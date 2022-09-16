from django.forms import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
#create user registration form 
class UserSignUp(UserCreationForm):
    mobile_number = PhoneNumberField()
    class Meta:
        model = User
        fields = ("username", "first_name","last_name", "email")
