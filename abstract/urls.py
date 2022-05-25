from rest_framework.routers import DefaultRouter
from abstract.views import AuthorViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet, basename='authors')

urlpatterns = router.urls