from django import forms

from tp_final_coder.paciente.models import Paciente

class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        #widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}
