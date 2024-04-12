from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CustomUserCreationForm


# Create your views here.
def inscription(resquest):
    if resquest.method == 'POST':
        form = CustomUserCreationForm(resquest.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form=CustomUserCreationForm()
    return render(resquest, 'inscription.html' , {'form': form})

def connexion(resquest):
    if resquest.method == 'POST':
        username = resquest.POST['username']
        password = resquest.POST['password']
        user = authenticate(resquest,username=username, password=password)
        if user is not None:
            login(resquest, user)
            return redirect('accueil')
        else:
            messages.error(resquest, "Nom d'utilisateur ou mot de passe incorrect." )
    return render(resquest,'connexion.html')
@login_required
def accueil(resquest):
    return render(resquest,'accueil.html')


def deconnexion(resquest):
    logout(resquest)
    return redirect('connexion')
