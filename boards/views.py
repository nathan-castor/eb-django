# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
# # from .models import Board
# # from django.shortcuts import render, get_object_or_404
# # from django.http import Http404
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Board, Topic, Post

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Board, Topic, Post

def index(request):
    return render(request, 'index.html', {'message':'success'})
def serverless(request):
    return render(request, 'serverless.html', {'message':'success'})
def metabase(request):
    return render(request, 'metabase.html', {'message':'success'})

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


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})