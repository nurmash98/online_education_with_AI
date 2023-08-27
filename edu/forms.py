from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Атыңызды жазыңыз'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тегіңізді жазыңыз'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон номеріңіз', 'id': 'phone'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин енгізіңіз'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Құпиясөз жазыңыз'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Құпиясөзді қайталап жазыңыз'}))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'username', 'password1', 'password2']


class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False  # Make username not required
    
    # Declare the fields after the __init__ method
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон номеріңіз', 'id': 'phone'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Құпиясөз енгізіңіз'}))

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')

        if phone_number and password:
            self.user_cache = authenticate(self.request, phone_number=phone_number, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Please enter a correct phone number and password. Note that both fields may be case-sensitive.",
                    code='invalid_login'
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
    
    
