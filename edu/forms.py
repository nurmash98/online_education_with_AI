from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Атыңызды жазыңыз'})
        
        )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тегіңізді жазыңыз'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон номеріңіз', 'id': 'phone'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Құпиясөз жазыңыз'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Құпиясөзді қайталап жазыңыз'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'password1', 'password2']

        
class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False  # Make username not required
    
    # Declare the fields after the __init__ method
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон номеріңіз', 'id': 'phone'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Құпиясөз енгізіңіз'}))

    