from django import forms
from .models import Goods

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = [
            "title",
            "price",
            "image1",
            "image2",
            "image3",
            "content",
        ]
        
        widgets = {
            "price": forms.RadioSelect,
        }