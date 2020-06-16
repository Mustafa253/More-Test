from django import forms
from .models import TechType, Product, Review

class ProductForm(forms.ModelForm):
    
    class Meta:
        model=Product
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'