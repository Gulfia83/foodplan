from django.shortcuts import render

def auth_view(request):
    return render(request, 'auth.html')


def card1_view(request):
    return render(request, 'card1.html')


def card2_view(request):
    return render(request, 'card2.html')


def card3_view(request):
    return render(request, 'card3.html')


def index_view(request):
    return render(request, 'index.html')


def order_view(request):
    return render(request, 'order.html')


def lk_view(request):
    return render(request, 'lk.html')


def registration_view(request):
    return render(request, 'registration.html')