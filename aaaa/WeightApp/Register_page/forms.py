from django.forms import ModelForm, TextInput
from .models import UserData


class DataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ["login", "password"]
        widgets = {
            'login': TextInput(attrs={   # login
             'class': 'form-control',
             'placeholder': 'login',
            }),
            'password': TextInput(attrs={  # password
                'class': 'form-control',
                'type': 'password',
                'placeholder': 'password',
            }),
        }