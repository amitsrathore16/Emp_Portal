from django import forms
from .models import Employee


class AddEmpForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ["name", "designation", "email", "phone", "address"]

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
            'designation' : forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control mr-sm-2'}),
            'phone' : forms.NumberInput(attrs={'class': "form-control mr-sm-2"}),
            'address' : forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
        }
