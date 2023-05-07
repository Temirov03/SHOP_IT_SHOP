from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet,ProductViewSet


router = SimpleRouter()

router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)


urlpatterns = [

]
