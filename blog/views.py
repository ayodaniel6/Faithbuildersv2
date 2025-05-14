from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.views import View
from django.db.models import Q


@cache_page(60 * 15)
def post_list(request):
    post_list = Post.objects.filter(is_draft=False).order_by('-date_published')
    paginator = Paginator(post_list, 10)  # Show 10 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})



def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })



@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({'liked': liked, 'like_count': post.likes.count()})



@require_POST
@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()

        return JsonResponse({
            'message': 'Comment added successfully',
            'comment': {
                'username': request.user.username,
                'content': comment.content,
                'timestamp': comment.created_at.strftime('%Y-%m-%d %H:%M'),
            }
        })
    else:
        return JsonResponse({'errors': form.errors}, status=400)



@login_required
def toggle_bookmark(request, pk):
    post = get_object_or_404(Post, id=pk)
    user = request.user

    if user in post.bookmarks.all():
        post.bookmarks.remove(user)
        bookmarked = False
    else:
        post.bookmarks.add(user)
        bookmarked = True

    return JsonResponse({'bookmarked': bookmarked})


# search for post based on keywords
class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '').strip()
        if not query:
            return JsonResponse([], safe=False)

        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query),
            is_draft=False
        ).distinct()

        data = [{"slug": post.slug, "title": post.title} for post in results]
        return JsonResponse(data, safe=False)