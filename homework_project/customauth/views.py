from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


### see => https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('learning:courses_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

