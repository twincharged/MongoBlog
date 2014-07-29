from django.shortcuts import render
from django.template import RequestContext
import models


def main(request):
    context = {}
    return render(request, 'main.html', context)

def user_index(request):
    users = models.User.objects
    context = {'users': users}
    return render(request, 'users.html', context)

def blog_index(request):
    blogs = models.Blog.objects
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)

def user(request, user_id):
    user = models.User.objects(id=user_id)
    context = {'user': user}
    return render(request, 'user.html', context)

def blog(request, blog_id):
    blog = models.Blog.objects(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blog.html', context)

def create_blog(request):
    if request.method is 'POST':
        req = request.POST
        blog = models.Post(title=req['title'],
              content=req['content'],
              image_path=req['image_path'],
              link_url=req['link_url'],
              author=req['author'],
              tags=req['tags'],
              comments=req['comments'])
        blog.save()
    blogs = models.Blog.objects
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)

def create_or_update_user(request):
    if request.method is 'POST':
        req = request.POST
        user = models.User(email=req['email'],
              user_name=req['user_name'],
              full_name=req['full_name'])
    elif request.method is 'PUT'
        req = request.PUT
        user = models.User.objects(id=req['id'])[0]
        user['email'] = req['email']
        user['user_name'] = req['user_name']
        user['full_name'] = req['full_name']
    user.save()
    users = models.User.objects
    context = {'users': users}
    return render(request, 'users.html', context)
