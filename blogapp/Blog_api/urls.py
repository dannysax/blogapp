from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PostDetailView, PostListView



urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='detail_view')
]