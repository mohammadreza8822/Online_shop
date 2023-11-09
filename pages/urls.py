from django.urls import path

from .views import HomePageView, AboutUsPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('aboutus/', AboutUsPage.as_view(), name='aboutus')
]