from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import UserProfile

# Create your views here.

def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    win_percentage = profile.win_percentage()
    context = {
        'games_played': profile.games_played,
        'games_won': profile.games_won,
        'games_lost': profile.games_lost,
        'win_percentage': win_percentage
    }
    return render(request, 'user/profile.html', context)
    
class CustomLoginView(LoginView):
    template_name = 'user/login.html'

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'user/register.html', {'form': form})