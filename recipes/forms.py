from django import forms
from datetime import datetime
from recipes.models import Recipe


# class NewRecipeForm(ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['name', 'ingredients', 'instructions']


class NewRecipeForm(forms.Form):
    name = forms.CharField()
    ingredients = forms.CharField()
    instructions = forms.CharField()
