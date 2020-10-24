from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

# CLASS BASED VIEWS URLS

urlpatterns = [
    path('', BlogListView.as_view(), name='post_list'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<str:slug>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<str:slug>/update/',
         BlogUpdateView.as_view(), name='post_update'),
]

# FUNCTION BASED VIEWS URLS

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('post/new/', views.post_new, name='post_new'),
#     path('post/<int:pk>/comment/', views.add_comment_to_post,
#          name='add_comment_to_post'),
# ]
