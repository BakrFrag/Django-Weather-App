from django import forms
from myapp.models import City;
class Cform(forms.ModelForm):
    class Meta:
        model=City;
        fields=['name',];
        widgets={'name':forms.TextInput(attrs={
            "class":"input","placeholder":"preferred city,country like cairo,egypt"
        })};
        