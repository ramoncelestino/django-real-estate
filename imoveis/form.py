from django import forms
from .models import Imovel

class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = ['nome', 'description', 'tipo_imovel', 'rua', 'aluguel_compra', 'bairro',
                  'price', 'quartos', 'banheiros', 'sqft', 'photo_main', 'photo_1', 'photo_2']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 120}),
            'price': forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
            'quartos': forms.NumberInput(attrs={'min': '0', 'class': 'form-control'}),
            'banheiros': forms.NumberInput(attrs={'min': '0', 'class': 'form-control', 'value': 0}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),

        }