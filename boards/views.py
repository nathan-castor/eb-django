from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board
from django.shortcuts import render, get_object_or_404
# from django.http import Http404


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

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})