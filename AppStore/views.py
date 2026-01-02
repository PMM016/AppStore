#views.py
from django.shortcuts import render, redirect
from accounts.models import Account
from django.contrib.auth import get_user_model


def load_nav(request):
    User = get_user_model()
    account = get_user_model()
    return render(request, "nav.html", {"accounts": account})

def go_back(request):
    return redirect(request.META.get('HTTP_REFERER', '/'))