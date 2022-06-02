from django.urls import path
from user import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()


router.register('user', views.UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginView.as_view(), name='login'),
   
]