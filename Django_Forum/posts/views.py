from http.client import HTTPS_PORT, HTTPResponse
from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # If the form is valid
        if form.is_valid():
            # Yes, SAVE
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

            # No, Show Error
            return HttpResponseRedirect(form.erros.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]

    # Show
    return render(request, 'post.html', {'posts': posts})

    def delete(request, post_id):
        output = 'POST ID is ' + str(post_id)
        return HTTPResponse(output)