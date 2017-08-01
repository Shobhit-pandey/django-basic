from django.shortcuts import redirect
from django.shortcuts import reverse

def login_redirect(request):
    return redirect(reverse('accounts:login'))