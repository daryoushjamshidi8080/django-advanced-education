from django import forms
from django.core.exceptions import ValidationError
from .models import User


class CustomUserCreationForm(forms.ModelForm):
    """
    forms for add new user
    """

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords are not the same")
        return password2

    def save(self, commit=True):
        """save user with hash password"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user