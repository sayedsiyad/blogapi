from django.shortcuts import render,get_object_or_404

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from blog.serializers import UserSerializers,PostSerializer,CommentSerializer

from rest_framework import authentication,permissions

from rest_framework.response import Response

from blog.models import Post

from rest_framework.views import APIView




class UserCreateView(CreateAPIView):

    serializer_class=UserSerializers

class PostListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

class CommentCreateView(CreateAPIView):

    serializer_class=CommentSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):

        id=self.kwargs.get("pk")

        post_instance=get_object_or_404(Post,id=id)

        serializer.save(post_object=post_instance,owner=self.request.user)

class PostLikeView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        post_object=get_object_or_404(Post,id=id)

        #adding authenticated user object to liked_by many to many field
        post_object.liked_by.add(request.user) 

        #for removing a user from liked_by post_object.liked_by.remove(user_object)

        #fetching all objects in a many to many field post_object.liked_by.all()

        return Response(data={"message":"liked"})





