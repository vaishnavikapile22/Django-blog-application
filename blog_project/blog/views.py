# blog/views.py
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer, TokenSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ObtainTokenView(generics.GenericAPIView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.authenticate_user(serializer.validated_data)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

    def authenticate_user(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            return user
        raise serializers.ValidationError('Invalid credentials.')

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        try:
            post = Post.objects.get(id=self.kwargs['post_pk'])
        except Post.DoesNotExist:
            raise serializers.ValidationError("Post not found.")
        
        serializer.save(author=self.request.user, post=post)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user != comment.author and not request.user.is_staff:
            return Response({'detail': 'You do not have permission to delete this comment.'}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

class RefreshTokenView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'detail': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            access_token = token.access_token
            return Response({
                'access': str(access_token),
                'refresh': str(token),
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
