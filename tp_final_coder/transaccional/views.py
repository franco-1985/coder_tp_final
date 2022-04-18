import json

from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
from django.core import serializers

from tp_final_coder.transaccional.models import ComidaXPaciente
from tp_final_coder.transaccional.models import PesoXPaciente
from tp_final_coder.transaccional.forms import FormularioPesoPaciente
from tp_final_coder.transaccional.forms import FormularioComidaPaciente

from tp_final_coder.comida.views import ComidaView

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
        # comida_paciente = ComidaXPaciente.objects.filter(dni=paciente)
        comida_paciente = ComidaXPaciente.objects.filter(dni=paciente).select_related('id_comida', 'id_momento')
        print(comida_paciente.query)
        #comida_paciente = PesoXPaciente.objects.filter(dni=paciente,id_comida=comida, id_momento=momento )
        form = FormularioComidaPaciente()
        #lista = list(comida_paciente)
        #ComidaPacienteView.mostrar_lista(lista)
        context = {'form':form, 'lista_comidas':comida_paciente}
        return render(request, template_buscar_paciente, context=context)

    def mostrar_lista(lista):

        txt = serializers.serialize('json',ComidaView.get_listado_comidas())
        jtext= json.loads(txt)
        tupla_comida = []
        for item in jtext:
            item_comida = (item["pk"], item["fields"]["nombre_comida"])
            tupla_comida.append(item_comida)

        # for item in tupla_comida:
        #     if item[0] == res_opc:
        #         print(item[1])

        print('primer for')
        i = 0
        for item_id_comida in lista:
            # print(item_id_comida.id_comida)
            if item_id_comida.id_comida == tupla_comida[i][0]:
                print(tupla_comida[i][1])



        # print('segundo for')
        # for item in tupla_comida:
        #     print(f'{item[0]} - {item[1]}')

class PesoPacienteView(TemplateView):


    def get(request, status=None):
        template_peso_paciente = 'transaccional/historial_peso.html'
        peso_paciente = PesoXPaciente.objects.all()
        context={'lista_peso_paciente':peso_paciente}
        return render(request=request, template_name=template_peso_paciente, context=context)


    def buscar_medidas(request, paciente):
        print('buscar medidas')
        template_buscar_paciente = 'transaccional/historial_peso.html'
        pesos_paciente = PesoXPaciente.objects.filter(dni=paciente)
        form = FormularioPesoPaciente()
        context = {'form':form, 'lista_pesos':pesos_paciente}
        return render(request, template_buscar_paciente, context=context)


