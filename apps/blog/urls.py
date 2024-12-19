from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet
from .views import CommentViewSet
from .views import PostViewSet

router = DefaultRouter()

router.register(r"categories", CategoryViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"posts", PostViewSet)

urlpatterns = router.urls
