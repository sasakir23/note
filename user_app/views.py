from typing import Sized
from django.shortcuts import redirect, render, get_object_or_404 
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from blog_app .models import Post
from django.contrib.auth.models import User





from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from blog_app .models import Post

# Create your views here.
def signup(request):
  signup_form = SignUpForm(request.POST or None)
  if request.method == "POST" and signup_form.is_valid():
      user = signup_form.save()
      input_username = signup_form.cleaned_data['username']
      input_email = signup_form.cleaned_data['email']
      input_password = signup_form.cleaned_data['password1']
      user = authenticate(username=input_username, email=input_email, password=input_password)
      login(request, user)
      return redirect('blog_app:index')
  context = {
      "signup_form": signup_form,
  }
  return render(request, 'user_app/signup.html', context)

def detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = user.post_set.all().order_by('-created_at')
    return render(request, 'user_app/detail.html', {'user': user, 'posts': posts})  


def edit(request, user_id):
   user = get_object_or_404(User, id=user_id)
   if request.method == "POST":
       form = SignUpForm(request.POST, instance=request.user)
       if form.is_valid():
           form.save()
           return redirect('user_app:detail', user_id=user.id)
   else:
       form = SignUpForm(instance=user)
   return render(request, 'user_app/edit.html', {'form': form, 'user':user })

def delete(request, user_id):
   user = get_object_or_404(User, id=user_id)
   user.delete()
   return redirect('blog_app:index')
