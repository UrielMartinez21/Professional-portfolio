from django.shortcuts import get_object_or_404, render
from blog.models import Post

# Create your views here.
def posts(request):
    """
    Render the posts.html template with all the posts
    """
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "posts.html", {"posts": posts, "total_posts": total_posts})



def post(request, post_id):
    """
    Render the post_detail.html template with the post that matches the post_id
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})