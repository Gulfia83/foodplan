from django.shortcuts import redirect, render
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:auth')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration.html', {'form': form})


def auth_view(request):
    return render(request, 'auth.html')


def lk_view(request):
    return render(request, 'lk.html')