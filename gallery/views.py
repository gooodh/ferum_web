
from django.views.generic import TemplateView, ListView

from gallery.models import Gallery


class HomeGalleryView(TemplateView):
    template_name = 'index.html'


class GalleryListView(ListView):
    model = Gallery
    context_object_name = 'gallery_list'
    template_name = 'gallery/gallery_list.html'
