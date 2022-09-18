from operator import imod
from .models import student
from django import forms


class stdreg(forms.ModelForm):
    class Meta:
        model=student
        fields = ['name','email','password']
        widgets = {'password':forms.PasswordInput(render_value=True)}