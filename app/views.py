from django.shortcuts import render, redirect, get_object_or_404
from collection.forms import PostForm
from django.views.decorators.http import require_POST
from django.utils import timezone
#from django.contrib.auth.views import login_required
from collection.models import Post, Comment, Vote
from django.db.models import Count
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# grabs objects and passes to the template

def index(request):
    page = request.GET.get('page', 1)
    sort_pub_date = request.GET.get('sort_pub_date', "desc")
    sort_votes = request.GET.get('sort_votes', "desc")

    order_pub_date="-published_date"
    if(sort_pub_date == "asc"):
        order_pub_date="published_date"
    
    order_votes="-vote_count"
    if(sort_votes == "asc"):
        order_votes="vote_count"

    postList=Post.objects.all().annotate(
        vote_count=Count('vote')).annotate(
            comment_count=Count('comment')
            ).order_by(order_votes, order_pub_date)
    paginator = Paginator(postList, 20)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {
        'posts': posts,
        'sort_votes': sort_votes,
        'sort_pub_date': sort_pub_date
    })

def post_detail(request, postid):
    post = get_object_or_404(Post, pk=postid)
    vote_count=Vote.objects.filter(post=post).count()
    comment_count=Comment.objects.filter(post=post).count()
    comments = Comment.objects.filter(post=post)
    is_voted = Vote.objects.filter(post=post, author=request.user)
    return render(request, 'posts/post_detail.html', {
        'post': post, 
        'comments': comments,
        'is_voted': is_voted,
        'vote_count': vote_count,
        'comment_count': comment_count
    })


def vote_post(request, postid):
    postobj=Post.objects.filter(pk=postid).first()
    vote = Vote()
    vote.author = request.user
    vote.post = postobj
    vote.save()
    return redirect('post_detail', postid=postid)
    
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', postid=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', { 'form': form })

def edit_post(request, postid):
    post = get_object_or_404(Post, pk=postid)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', postid=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', { 'form': form })


# DJANGO GIRLS to be edited from above
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})


# def create_post(request):
#     form = PostForm
#     if request.method == 'POST':
#         form = PostForm
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.slug = slugify(post.name)
#             post.save()
#             return redirect('post_detail', slug=post.slug)
#     else:
#         form = form(instance=post)

#     return render(request, 'posts/create_post.html'), {
#         'form': form,
#     }

# @login_required
# def edit_post(request, slug):
#     post = Post.objects.get(slug=slug)
#     if post.user != request.user:
#         raise Http404
#     form_class = PostForm
#     if request.method == 'POST':
#         form = form_class(data=request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', slug=post.slug)

#     else:
#         form = form_class(instance=post)

#     return render(request, 'posts/edit_post.html', {
#         'post': post,
#         'form': form,
#     })

# def render_post_list(request, header, posts):
#     """want this to render if user is authenticated with title, link, description """

# posts = posts.annotate(num_of_favorites=Count('favorites'))
# favorite_posts = []
# if request.user.is_authenticated:
#     favorite_posts = request.user.favorite_posts.all()
# posts = posts.order_by('-created_at')
# return render(
#     request, "collection/index.html", {
#         "title": title,
#         "link": link,
#         "description": description
#     }
# )
