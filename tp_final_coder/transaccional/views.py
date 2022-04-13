from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

from tp_final_coder.transaccional.models import ComidaXPaciente
from tp_final_coder.transaccional.models import PesoXPaciente
from tp_final_coder.transaccional.forms import FormularioPesoPaciente
from tp_final_coder.transaccional.forms import FormularioComidaPaciente

class ComidaPacienteView(TemplateView):

    def get(request, status=None):
        template_comida_paciente = ''
        comidas_paciente = ComidaXPaciente.objects.all()
        context={'lista_comidas_paciente':comidas_paciente}
        return render(request=request, template_name=template_comida_paciente, context=context)

   #def buscar_comidas(request, paciente, comida, momento):
    # resta hacer la parte para que se muestre los valores de los id
    def buscar_comidas(request, paciente):
        template_buscar_paciente = 'transaccional/historial_comida.html'
        comida_paciente = ComidaXPaciente.objects.filter(dni=paciente)
        #comida_paciente = PesoXPaciente.objects.filter(dni=paciente,id_comida=comida, id_momento=momento )
        form = FormularioComidaPaciente()
        print(comida_paciente)
        context = {'form':form, 'lista_comidas':comida_paciente}
        return render(request, template_buscar_paciente, context=context)

class PesoPacienteView(TemplateView):


    def get(request, status=None):
        template_peso_paciente = 'transaccional/historial_peso.html'
        peso_paciente = PesoXPaciente.objects.all()
        context={'lista_peso_paciente':peso_paciente}
        return render(request=request, template_name=template_peso_paciente, context=context)


    def buscar_medidas(request, paciente):
        template_buscar_paciente = 'transaccional/historial_peso.html'
        pesos_paciente = PesoXPaciente.objects.filter(dni=paciente)
        form = FormularioPesoPaciente()
        context = {'form':form, 'lista_pesos':pesos_paciente}
        return render(request, template_buscar_paciente, context=context)


