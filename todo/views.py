from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        "posts" : Post.objects.all()
    }
    return render(request, 'todo/all_members.html', context)

def details(request, id):
    posts = Post.objects.get(id=id)
    context = {
        "posts" : posts,
    }
    return render(request, 'todo/details.html', context)

def main(request):
    return render(request, "todo/main.html")

def testing(request):
    context = {
        'fruits' : ['Apple', 'Banana', 'Cherry']
    }

    return render(request, "todo/template.html",context)