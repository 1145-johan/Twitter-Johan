from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, PictureForm

def index(request):
    if request.method == 'POST':
         form = PostForm(request.POST, request.FILES)

         if form.is_valid():
             
             form.save()

             return HttpResponseRedirect('/')
         
         else:
             return HttpResponseRedirect(form.errors.as_json())
         



    posts = Post.objects.all()[:20]

    return render(request, 'post.html',{'posts': posts})


# Create your views here.
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


    # output = 'POST ID is ' + str(post_id)
    # return HttpResponse(output)

# def edit(request, post_id):
#     output = "Edit Page"
#     return HttpResponseRedirect(output)
# Create your views here.

def likes(request, post_id):
    post = Post.objects.get(id = post_id)
    post.like +=1
    post.save()
    return HttpResponseRedirect("/")


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post,)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    return render(request, 'edit.html', {'post': post})

