from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from Blog.models import Post
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly, SAFE_METHODS, BasePermission

"""class PostUpdateWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user"""


class PostListView(generics.ListCreateAPIView):
    #permission_class = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [PostUpdateWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


