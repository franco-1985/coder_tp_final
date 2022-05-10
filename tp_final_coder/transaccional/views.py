import json

from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView
from django.core import serializers

from tp_final_coder.transaccional.models import ComidaXPaciente
from tp_final_coder.transaccional.models import PesoXPaciente
from tp_final_coder.paciente.models import Paciente

from tp_final_coder.transaccional.forms import FormularioPesoPaciente
from tp_final_coder.transaccional.forms import FormularioComidaPaciente

from tp_final_coder.comida.views import ComidaView
from tp_final_coder.paciente.views import PacienteView

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
        # print(comida_paciente.query)
        #comida_paciente = PesoXPaciente.objects.filter(dni=paciente,id_comida=comida, id_momento=momento )
        form = FormularioComidaPaciente()
        #lista = list(comida_paciente)
        #ComidaPacienteView.mostrar_lista(lista)
        context = {'form':form, 'lista_comidas':comida_paciente}
        return render(request, template_buscar_paciente, context=context)

    def registrar_comida_paciente(request, paciente=None):
        template_registrar_comida = 'transaccional/reg_comidas.html'
        if request.method == 'POST':
            comida_paciente= ComidaXPaciente(dni=request.POST['dni_paciente'])
            comida_paciente.save()
            return render(request=request, template_name='base_v2.html')
        return render(request=request, template_name=template_registrar_comida)

            # form = FormularioComidaPaciente()

    def mostrar_lista_(lista):
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
        template_peso_paciente = 'transaccional/historial_medidas.html'
        peso_paciente = PesoXPaciente.objects.all()
        context={'lista_peso_paciente':peso_paciente}
        return render(request=request, template_name=template_peso_paciente, context=context)


    def buscar_medidas(request, paciente):
        # print('buscar medidas')
        template_buscar_paciente = 'transaccional/historial_medidas.html'
        medidas_paciente = PesoXPaciente.objects.filter(dni=paciente)
        form = FormularioPesoPaciente()

        res_paciente = PacienteView.getPaciente(dni=paciente)

        # res_paciente = Paciente.objects.filter(dni=paciente).first()

        # context = {'form':form, 'lista_medidas':medidas_paciente}
        context = {'form':form, 'lista_medidas':medidas_paciente,'paciente': res_paciente}

        return render(request, template_buscar_paciente, context=context)

    def index(request, paciente):
        template_registrar_medida = 'transaccional/reg_medidas.html'
        peso_paciente = FormularioPesoPaciente()
        # print('Antes de la asignacion',peso_paciente.fields)
        peso_paciente.dni=request.POST.get('dni')
        # print('Despues de la asignacion', peso_paciente.dni)
        # res_paciente = Paciente.objects.filter(dni=paciente).first()
        res_paciente = PacienteView.getPaciente(dni=paciente)
        # for rp in res_paciente:
        #     print(rp.nombre)
        context = {'form': peso_paciente, 'paciente': res_paciente}
        return render(request, template_registrar_medida, context)

    # def post(request, paciente):
    #     template_registrar_medida = 'transaccional/registrar_medidas.html'
    #     peso_paciente  = FormularioPesoPaciente(request.POST)
    #     peso_paciente.dni=paciente
    #     # no anda la asignacion del dni
    #     # print('----> ', peso_paciente.dni)
    #     if peso_paciente.is_valid():
    #         peso_paciente.save()
    #         peso_paciente = FormularioPesoPaciente()
    #     return render(request=request, template_name=template_registrar_medida, context={'form': peso_paciente, 'mensaje': 'OK'})

    def post(request):
        template_registrar_medida = 'transaccional/reg_medidas.html'
        if request.method == 'POST':
            medida_paciente = PesoXPaciente(dni=request.POST['dni_paciente'], peso=request.POST['peso_paciente'], estatura=request.POST['estatura_paciente'], fecha_registro=request.POST['fecha_paciente'])
        # no anda la asignacion del dni
        # print('----> ', peso_paciente.dni)
        # if peso_paciente.is_valid():
            medida_paciente.save()
        #     peso_paciente = FormularioPesoPaciente()
            return render(request=request, template_name='base_v2.html')
        return render(request=request, template_name=template_registrar_medida)

