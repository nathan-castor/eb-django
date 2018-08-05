from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import SignUpForm

from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('*********HERE IS THE USER!**********: \n',user.username)

            # username = user.username
            # password = user.password
            # user = authenticate(username=username, password=password)

            # user.backend = 'django.core.cache.backends.filebased.FileBasedCache'

            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

