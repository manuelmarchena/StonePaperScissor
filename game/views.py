from django.shortcuts import render, redirect
from django.contrib import messages
import random
from user.models import UserProfile
# Create your views here.

def index(request):
    return render(request, 'game/index.html')
    
def result(request):
    user_choice = request.GET.get('choice')
    
    
    if not user_choice:
        messages.error(request, "You must select an option.")
        return redirect('index')
    
    choices = ['Stone', 'Paper', 'Scissor']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        profile.games_played += 1
        if result == 'You Win':
            profile.games_won += 1
        elif result == 'You Loose':
            profile.games_lost += 1
        profile.save()
    
    context = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    }
    return render(request, 'game/result.html', context)


def determine_winner(user, computer):
    if user == computer:
        return 'Draw'
    elif(user == 'Stone' and computer == 'Scissor') or \
        (user == 'Paper' and computer == 'Stone') or \
        (user == 'Scissor' and computer == 'Paper'):
        return 'You Win'
    else:
        return 'You Loose'