from django.shortcuts import render


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

