from django.urls import path
from .import views
urlpatterns = [
    path('blog/',views.index,name = 'blog-index'),
    path('post_detail/<int:post_id>/',views.post_detail,name = 'blog-post_detail'),
    path('post_edit/<int:post_id>/',views.post_edit,name = 'blog-post_edit'),
    path('post_delete/<int:post_id>/',views.post_delete,name = 'blog-post_delete'),
    
]

