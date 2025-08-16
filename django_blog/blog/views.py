from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    context = {
        'posts': posts,  # Pass the posts to the template
    }
    return render(request, 'blog/index.html', context)


def post(request):
    pass

def login(request):
    pass

def register(request):
    pass