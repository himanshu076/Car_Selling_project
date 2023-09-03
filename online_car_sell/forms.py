from django import forms
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from online_car_sell.models import RegisterVehicle
from django.utils.translation import gettext_lazy as _


# class ImagePreviewWidget(forms.widgets.FileInput):
#     def render(self, name, value, attrs=None, **kwargs):
#         input_html = super().render(name, value, attrs=None, **kwargs)
#         img_html = mark_safe(f'<br><br><img src="{value.url}"/>')
#         return f'{input_html}{img_html}'

class CarRegisterForm(ModelForm):

    class Meta:
        model = RegisterVehicle
        fields = ['car_title', 'username', 'mobile_no', 'images', 'images_1',
                'images_2', 'images_3', 'images_4', 'make', 'model',
                'registration_number', 'year', 'condition', 'vehicle_price']
