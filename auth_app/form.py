from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nom de l'ulisateur",
        strip=False,
        required=True,

    )
    Email = forms.EmailField(
        label="Adresse Email",
        required=True,

    )
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplate': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Mot de Passe de Confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplate': 'new-password'}),
    )


    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("username","Email","password1", "password1")
