import imp
from django.shortcuts import render
from .models import Blogpost

# Create your views here.
def blogHome(request):
    posts = Blogpost.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def blogPost(request,id):
    post = Blogpost.objects.filter(postId=id)
    return render(request,'blog/blogPost.html',{'post':post[0]})