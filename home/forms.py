from django import forms
from django.contrib.auth.models import User
from .models import Note

class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' ,'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            }
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title' , 'description']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            }