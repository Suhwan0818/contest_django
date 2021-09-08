from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checks:index')
        else:
            form = UserCreationForm()
        context = {
            'form':form
        }
        return Response("ok", status = 200)

def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk = pk)
    context = {
        'user' = user
    }
    return Response("ok", status = 200)