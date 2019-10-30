from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            confirm_password = form.cleaned_data.get("password1")

            if password != confirm_password:
                form.add_error('password1', 'Passwords must match!')
            else:
                user = form.save()
                user.set_password(user.password)
                user.save()
                return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form':form, 'title':'User Signup'})
