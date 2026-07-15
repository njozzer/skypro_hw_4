from django import forms
from django.core.validators import ValidationError
from catalog import models

bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'picture', 'category', 'price']

        def clean_name(self):
            name = self.cleaned_data.get('name')
            for bad_word in bad_words:
                if bad_word in name.lower():
                    raise ValidationError('Имя не должно содержать запрещенных слов!')
            return name

        def clean_description(self):
            description = self.cleaned_data.get('description')
            for bad_word in bad_words:
                if bad_word in description.lower():
                    raise ValidationError('Описание не должно содержать запрещенных слов!')
            return description

        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price <= 0:
                raise ValidationError('Цена не может быть отрицательной, или нулевой')
            return price

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)

            self.fields['name'].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Введите название'
            })
