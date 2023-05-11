from django.urls import path
from .views import ProviderViewSet,IncomeViewSet,IncomeItemViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('provider', ProviderViewSet)
router.register('income', IncomeViewSet)
router.register('incomeitem', IncomeItemViewSet)


urlpatterns = [
    
]