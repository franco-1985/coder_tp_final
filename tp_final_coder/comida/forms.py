from django import forms

from tp_final_coder.comida.models import Comida

class FormularioComida(forms.ModelForm):
    class Meta:
        model = Comida
        fields = '__all__'
        # fields = ('nombre','id_comida')
