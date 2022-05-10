from django import forms

from tp_final_coder.transaccional.models import PesoXPaciente
from tp_final_coder.transaccional.models import ComidaXPaciente

from tp_final_coder.comida.models import Comida
from tp_final_coder.momento_comida.models import MomentoComida

class FormularioPesoPaciente(forms.ModelForm):
    class Meta:
        model = PesoXPaciente
        # fields = '__all__'
        fields = ('peso','estatura', 'fecha_registro')
        widgets = {'fecha_registro': forms.DateInput(attrs={'type': 'date'})}

# class FormularioComidaPaciente(forms.ModelForm):
#     class Meta:
#         model = ComidaXPaciente
#         fields = '__all__'

class FormularioComidaPaciente(forms.Form):

    id_comida = forms.ModelChoiceField(queryset=Comida.objects.order_by('id_comida').values_list('nombre_comida', flat= True).distinct(), empty_label= None, label=None, required=True)
    id_momento = forms.ModelChoiceField(queryset=MomentoComida.objects.order_by('id_momento').values_list('nombre_momento', flat= True).distinct(), empty_label= None, label=None, required=True)
    descripcion = forms.CharField(max_length=100)

    class Meta:
        model = ComidaXPaciente
        fields = '__all__'



   #nameequipo = forms.ModelChoiceField (queryset=DatosEquipo.objects.order_by('ideq').values_list('nombreequipo', flat=True).distinct(), empty_label=None, label=None, required=True)
