from django.shortcuts import render
from .models import Post
from users.models import Profile

def home(request):
    context = {
       'posts':  Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def resume(request):
	context1 = {
       'resumes':  Profile.objects.all()
    }
	return render(request, 'blog/resume.html',context1)


	