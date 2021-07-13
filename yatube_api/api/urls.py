from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as rf_view

from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(r'v1/users', UserViewSet)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', rf_view.obtain_auth_token),
    path('', include(router.urls)),
]
