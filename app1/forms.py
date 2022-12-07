from django import forms
from . models import Table1,Gallery

class RegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=16,min_length=6)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=16,min_length=6)
    class Meta():
        model=Table1
        fields='__all__'

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=16,min_length=6)
    class Meta():
        model=Table1
        fields=('Email','Password')

class UpdateForm(forms.ModelForm):
    class Meta():
        model=Table1
        fields=('Name','Age','Place','Email')


class ChangePassword(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=16,min_length=6)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=16,min_length=6)
    ConfirmNewPassword=forms.CharField(widget=forms.PasswordInput,max_length=16,min_length=6)
