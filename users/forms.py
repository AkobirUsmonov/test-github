from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User


class NewsUserForm(BaseUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(NewsUserForm, self).save(commit=False)
        email = self.cleaned_data['email']
        user.email = email
        if commit:
            user.save()
        return user