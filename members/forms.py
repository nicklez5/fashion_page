from django.forms import ModelForm
from django import forms
from .models import Men_Shirt,Men_Jacket,Men_Pants
class UploadForm(ModelForm):
    size = forms.CharField()
    price = forms.FloatField()
    color = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Men_Shirt
        fields = ['size','price','color','image']
class UploadForm(ModelForm):
    size = forms.CharField()
    price = forms.FloatField()
    color = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Men_Jacket
        fields = ['size','price','color','image']
class UploadForm(ModelForm):
    waist_size = forms.CharField()
    price = forms.FloatField()
    color = forms.CharField()
    image =  forms.ImageField()
    class Meta:
        model = Men_Pants
        fields = ['waist_size','price','color','image']

#class UploadForm():