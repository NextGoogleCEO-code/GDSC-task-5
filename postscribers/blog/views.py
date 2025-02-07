from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Postmodel
from .forms import PostModelForm,PostUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    posts = Postmodel.objects.all()
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostModelForm()    
    context = {
        'posts':posts,
        'form':form
    }

    return render(request,'blog/index.html',context)

@login_required
def post_detail(request,post_id):
    post = Postmodel.objects.get(id=post_id)
    context = {
        'post':post
    }
    return render(request,'blog/post_detail.html',context)

@login_required
def post_edit(request,post_id):
    post = Postmodel.objects.get(id=post_id)
    if request.method == "POST":
        form = PostUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post_detail',post_id=post_id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request,'blog/post_edit.html',context)


@login_required
def post_delete(request,post_id):
    post = Postmodel.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('blog-index')
    context = {
        'post':post
    }
    
    
    return render(request,'blog/post_delete.html',context)

