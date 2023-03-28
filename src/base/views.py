
from django.shortcuts import redirect


def home(request):
    """Home page"""
    return redirect('cours_list')


