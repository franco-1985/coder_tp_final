from django import forms

from tp_final_coder.momento_comida.models import MomentoComida

class FormularioMomentoComida(forms.ModelForm):
    class Meta:
        model = MomentoComida
        fields = '__all__'
