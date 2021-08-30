
from django.shortcuts import render,HttpResponse,redirect
from . models import Post

def index(request):
    posts=Post.objects.all()
    return render(request,"index.html",{"posts":posts})

def create(request):
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        newpost=Post.objects.create(title=title,description=description)
        newpost.save()
        return redirect("homepage")
    return render(request,"create.html")

def update(request,id):
    post=Post.objects.get(id=id)
    if request.method=='POST':
        post.title=request.POST['title']
        post.description=request.POST['description']
        post.save()
        return redirect("homepage")
    context={
        'post':post
    }
    return render(request,"update.html",context)

def delete(request,id):
    Post.objects.get(id=id).delete()
    return redirect("homepage")
