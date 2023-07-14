
from django.urls import path
from .views import HomeGalleryView


urlpatterns = [
    path('', HomeGalleryView.as_view(), name='home'),
]
