from app1.models import*
from django import forms
class Studentform(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'