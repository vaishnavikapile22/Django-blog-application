from django.urls import path
from .views import PostListCreateView, PostDetailView,CommentDetailView, CommentListCreateView, UserRegistrationView, ObtainTokenView, RefreshTokenView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/posts/<int:post_pk>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('token/', ObtainTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
]
 