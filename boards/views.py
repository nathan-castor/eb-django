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

    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)