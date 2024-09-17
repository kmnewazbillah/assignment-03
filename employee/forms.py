from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    DESIGNATION_CHOICES = [
        ('Programmer', 'Programmer'),
        ('Designer', 'Designer'),
        ('Web Designer', 'Web Designer'),
        ('Other', 'Other'),
    ]

    designation = forms.ChoiceField(choices=DESIGNATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'short_description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateEmployeeForm(forms.ModelForm):
    DESIGNATION_CHOICES = [
        ('Programmer', 'Programmer'),
        ('Designer', 'Designer'),
        ('Web Designer', 'Web Designer'),
        ('Other', 'Other'),
    ]

    designation = forms.ChoiceField(choices=DESIGNATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['salary', 'designation']
        widgets = {
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
        }
