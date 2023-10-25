from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from .models import Category, Post
from .forms import CommentForm, PostForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from pytils.translit import slugify
from taggit.models import Tag


def post_list(request, category_slug=None, tag_slug=None):
    category = Category.objects.all().first()
    if category_slug:
        category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category=category)
    tag = None
    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        posts = Post.objects.filter(tags__in=[tag])
        category = None
    categories = Category.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'main/post_list.html',
                  {
                      'posts': posts,
                      'categories': categories,
                      'selected_category': category,
                      'tag': tag,
                  })


def post_detail(request, year, month, day, post_slug):
    post = Post.objects.get(slug=post_slug,
                            created__year=year,
                            created__month=month,
                            created__day=day)
    comments = post.comments.all()
    comment_form = CommentForm()
    return render(request,
                  'main/post_detail.html',
                  {
                      'post': post,
                      'comments': comments,
                      'comment_form': comment_form,
                  })


@require_POST
def add_comment(request, post_id):
    form = CommentForm(request.POST)
    post = Post.objects.get(id=post_id)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return redirect(post.get_absolute_url())


def about(request):
    return render(request, 'main/about.html')


def api_page(request):
    return render(request, 'main/api_page.html')


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request,
                  'main/add_post.html',
                  {
                      'form': form
                  })
