from rest_framework.routers import DefaultRouter
from .views_api import PostAdminViewSet, CommentModerationViewSet

router = DefaultRouter()
router.register(r'posts', PostAdminViewSet)
router.register(r'comments', CommentModerationViewSet)

urlpatterns = router.urls
