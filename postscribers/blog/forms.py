from django import forms
from .models import Postmodel
class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = Postmodel
        fields = ('title','content')