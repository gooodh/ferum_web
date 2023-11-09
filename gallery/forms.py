from .models import Gallery
from django.forms import ModelForm, TextInput, NumberInput


class GalleryForm(ModelForm):

    class Meta:
        # Название модели на основе
        # которой создается форма
        model = Gallery
        # Включаем все поля с модели в форму
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
                }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор',
                }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость',
                }),
        }
