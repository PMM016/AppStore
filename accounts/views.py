from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account  # Your Account model

@login_required
def view_account(request):
    """
    Display the current user's Account info.
    Only works if the logged-in user has an Account object linked.
    """
    try:
        account = Account.objects.get(user=request.user)
    except Account.DoesNotExist:
        account = None

    context = {
        "account": account,
    }
    return render(request, "accounts/view_account.html", context)
