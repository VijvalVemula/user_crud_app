from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.middleware.csrf import get_token
from django.http import JsonResponse

# API ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Template Views
def index(request):
    return render(request, 'users/index.html', {'csrf_token': get_token(request)})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users, 'csrf_token': get_token(request)})

def user_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        User.objects.create(first_name=first_name, last_name=last_name, email=email)
        return redirect('user_list')
    return render(request, 'users/user_create.html', {'csrf_token': get_token(request)})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('user_list')
    return render(request, 'users/user_update.html', {'user': user, 'csrf_token': get_token(request)})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_delete.html', {'user': user, 'csrf_token': get_token(request)})

# CSRF Token Endpoint for API
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})