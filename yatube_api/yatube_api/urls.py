from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from posts.views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet
from rest_framework import routers
from rest_framework.authtoken import views as rf_view

router = routers.DefaultRouter()
router.register(r'api/v1/posts', PostViewSet, basename='posts')
router.register(r'api/v1/users', UserViewSet)
router.register(r'api/v1/groups', GroupViewSet)
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', rf_view.obtain_auth_token),
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
