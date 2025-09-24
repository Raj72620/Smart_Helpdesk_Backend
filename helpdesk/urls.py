from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'tickets', TicketViewSet)  # URL will be /api/tickets/

urlpatterns = router.urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
