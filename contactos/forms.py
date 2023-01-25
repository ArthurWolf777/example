from django import forms
from .models import all_states, phones_types, Phone


########## OPCIÓNES DE ESTADOS EN EL FORM DE DIRECCIÓN
class states_options(forms.Form):
    
    options = all_states()

    states = forms.TypedChoiceField(
        label='Estado*',
        choices=options,
    )

############ FORMULARIO DE TELÉFONO   
class phone_form(forms.Form):
    options = phones_types
    types = forms.TypedChoiceField(
        label='Tipo',
        choices=options,
        required=True
    )
    alias = forms.CharField(
        label='Alias',
        max_length=255,
        required=True
        )
    
    number = forms.CharField(
        label='Número*',
        max_length=50,
        widget=forms.NumberInput(),
        required=True
        )