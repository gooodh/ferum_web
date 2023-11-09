
from django.urls import path
from .views import HomeGalleryView, GalleryListView


urlpatterns = [
    path('', HomeGalleryView.as_view(), name='home'),
    path('gallery', GalleryListView.as_view(), name='gallery_list'),

]
