from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movie import views

router = DefaultRouter()

# empty path URL first throwing detail not found, so keep router with the empty path at last
router.register('movie', views.MovieViewSet, basename='movie')
router.register('shows', views.ShowsViewSet, basename='shows')
router.register('booking', views.TicketBooking, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]