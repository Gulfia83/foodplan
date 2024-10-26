from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View

from accounts.models import Like
from recipeapp.models import Dish
from .forms import RegistrationForm, AvatarForm


User = get_user_model()


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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Неверный пароль.')
        except User.DoesNotExist:
            messages.error(request, 'Пользователь с таким email не найден.')

    return render(request, 'auth.html')


@login_required
def lk_view(request):
    user = request.user
    context = {'name': user.username, 'email': user.email}
    return render(request, 'lk.html', context)


@login_required
def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.avatar = form.cleaned_data['avatar']
            user.save()
            return redirect('accounts:lk')
    else:
        form = AvatarForm()
    return render(request, 'upload_avatar.html', {'form': form})


@login_required
def create_like(request, pk):
    if request.method == 'POST':
        dish = get_object_or_404(Dish, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, dish=dish)

        if created:
            message = 'Лайк добавлен!'
        else:
            message = 'Вы уже лайкнули это блюдо.'

        return JsonResponse({'message': message})

    return JsonResponse({'message': 'Неверный метод.'}, status=405)