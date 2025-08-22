from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from blog.models import Post, Comment
from .forms import PostForm
from bot.models import CounsellorRequest
from django.views.generic import TemplateView
# Create your views here.

@staff_member_required
def cms_dashboard(request):
    return render(request, 'cms/admin_dashboard.html')


@staff_member_required
def post_list(request):
    user = request.user
    # Show all published posts
    published_posts = Post.objects.filter(is_draft=False).order_by('-date_published')
    # Show drafts only created by this user
    draft_posts = Post.objects.filter(author=user, is_draft=True).order_by('-date_published')
    
    return render(request, 'cms/admin_post_list.html', {
        'published_posts': published_posts,
        'draft_posts': draft_posts,
    })



@staff_member_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('cms:admin_post_list')
    else:
        form = PostForm()
    return render(request, 'cms/admin_post_form.html', {'form': form, 'is_create': True})


@staff_member_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('cms:admin_post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'cms/admin_post_form.html', {'form': form, 'is_create': False})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.delete()
    return redirect('cms:admin_post_list')


@staff_member_required
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'cms/admin_comment_list.html', {'comments': comments})


@staff_member_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('cms:admin_comment_list')


@staff_member_required
def manage_requests(request):
    requests = CounsellorRequest.objects.all().order_by('-created_at')
    return render(request, 'cms/manage_requests.html', {'requests': requests})


class restfulAPIView(TemplateView):
    template_name = 'restAPI.html'
    