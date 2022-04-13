from django import forms

from tp_final_coder.transaccional.models import PesoXPaciente
from tp_final_coder.transaccional.models import ComidaXPaciente

class FormularioPesoPaciente(forms.ModelForm):
    class Meta:
        model = PesoXPaciente
        fields = '__all__'
        widgets = {'fecha_registro': forms.DateInput(attrs={'type': 'date'})}

class FormularioComidaPaciente(forms.ModelForm):
    class Meta:
        model = ComidaXPaciente
        fields = '__all__'
