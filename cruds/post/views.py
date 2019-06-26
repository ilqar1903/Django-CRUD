from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import  Post
from .forms import PostForm
from django.contrib import  messages


def post_index(request):
     posts=Post.objects.all()
     return render(request,'post/index.html',{'posts':posts})

def post_detail(request,id):
     post =get_object_or_404(Post,id=id)
     context={
          'post' : post,
     }
     return render(request, 'post/details.html', context)

def post_create(request):
     if request.method=='POST':
          form = PostForm(request.POST)
          if form.is_valid():
            form.save()
            messages.success(request, "Successfully created")

     else:
         form = PostForm()

     context = {
          'form': form,
     }

     return render(request, 'post/form.html', context)

def post_update(request,id):
     post = get_object_or_404(Post, id=id)
     form = PostForm(request.POST or None, instance=post)
     if form.is_valid():
        form.save()
        messages.success(request, "Successfully Updated")

     context = {
          'form': form,
     }

     return render(request, 'post/form.html', context)

def post_delete(request,id):
     post = get_object_or_404(Post, id=id)
     post.delete()
     return redirect("post:index")