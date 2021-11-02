from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import Post, User, Comment
from django.views import View
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator





class PostsList(LoginRequiredMixin, View):
    def get(self, request, slug=None):
        if slug is not None:
            post_list = Post.objects.filter(group__slug=slug)
            template = 'posts/group.html'
        else:
            post_list = Post.objects.order_by("-pub_date").all()
            template = 'posts/index.html'
        paginator = Paginator(post_list, 10)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, template, {"page": page, "paginator": paginator})


class NewPost(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'posts/new_post.html', {"form": form, "mode": "add"})
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            return render(request, 'posts/new_post.html', {'form': form, "mode": "add"})

class Profile(View):
    def get(self, request, username):
        profile = get_object_or_404(User, username=username)
        post_list = Post.objects.filter(author=profile).order_by("-pub_date")
        print(post_list)
        paginator = Paginator(post_list, 10)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'posts/profile.html', {'profile': profile,
                                                      'page': page,
                                                      "paginator": "paginator",
                                                      'post_count': post_list.count(),
                                                      }
                      )

class Post_View(View):
    def get(self, request, username, post_id):
        post = get_object_or_404(Post, id=post_id)
        post_list = Post.objects.filter(author__username=username)
        comments = Comment.objects.filter(post=post).order_by("-created").select_related(
            'post').prefetch_related(
            'author').all()
        form = CommentForm()
        return render(request, 'posts/post_detail.html', {'profile': post.author,
                                                        'post': post,
                                                        'post_count': post_list.count(),
                                                        'comments': comments,
                                                        'form': form,
                                                      }
                      )
class Post_Edit(LoginRequiredMixin, View):
    def get(self, request, username, post_id):
        if request.user.username != username:
           return redirect('post', username=username, post_id=post_id)
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(instance=post, files=request.FILES or None)
        return render(request, 'posts/new_post.html', {'form': form, 'mode': 'edit'})

    def post(self, request, username, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST, instance=post, files=request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('post', username=username, post_id=post_id)
        return render(request, 'new_post', {'form': form})

class AddComment(LoginRequiredMixin, View):
    def get(self, request, username, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm()
        return render(request, 'posts/comments.html', {"form": form, "post": post})
    def post(self, request, username, post_id):
        post = get_object_or_404(Post, id=post_id)
        print(post)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post', username=username, post_id=post_id)
        else:
            return render(request, 'posts/comments.html', {'form': form, 'post': post})
