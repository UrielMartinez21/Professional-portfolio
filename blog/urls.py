from django.urls import path
from blog.views import post, posts

# --> Variable para referenciar a todo lo de urlpatters
app_name = 'blog'

urlpatterns = [
    path('', posts, name='posts'),
    path('<int:post_id>/', post, name='post_detail'),
]