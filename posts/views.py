from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.http import Http404
from .models import Post
from django.urls import reverse
from .forms import PostForm

# Create your views here.
class PostList(generic.ListView):
    model = Post
    # context_object_name
    template_name = 'posts/_posts.html'



@login_required()
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.slug = slugify(post.title)
            post.user = request.user
            if 'featured_image' in request.FILES:
                post.featured_image = request.FILES['featured_image']
            post.save()
        return HttpResponseRedirect(reverse('posts:detail', kwargs={'slug':post.slug}))
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form':form, 'title':'New Post'})

class PostDetail(generic.DetailView):
    model = Post

class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'
