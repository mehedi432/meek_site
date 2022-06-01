from django.urls import path
from .views import HomePageView, ProfilePageView, MeekPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('meek-sweater-ltd/', MeekPageView.as_view(), name='meek-sweater'),
]