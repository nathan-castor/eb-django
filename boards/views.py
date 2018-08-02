from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board

def home(request):
    board, created = Board.objects.update_or_create(
        name='Python',
        defaults = {
            'description' : 'General discussion about Python.'
        }
    )
    board, created = Board.objects.update_or_create(
        name='Django',
        defaults = {
            'description' : 'Lovely discussion about Django.'
        }
    )

    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})