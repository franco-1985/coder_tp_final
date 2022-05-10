from django.shortcuts import render
from django.views.generic import TemplateView
from tp_final_coder.paciente.forms import FormularioPaciente
from tp_final_coder.paciente.models import Paciente


class PacienteView(TemplateView):

    def get(request, status=None):
        template_paciente = 'pacientes/get_pacientes.html'
        pacientes = Paciente.objects.all()
        context = {'lista_pacientes': pacientes}
        return render(request=request, template_name=template_paciente, context=context)

    def index(request):
        template_paciente = 'pacientes/add_pacientes.html'
        paciente = FormularioPaciente()
        context = {'form': paciente}
        return render(request, template_paciente, context)

    def post(request):
        template_paciente = 'pacientes/add_pacientes.html'
        paciente = FormularioPaciente(request.POST)
        if paciente.is_valid():
            paciente.save()
            paciente = FormularioPaciente()
        return render(request=request, template_name=template_paciente, context={'form': paciente, 'mensaje': 'OK'})

    def edit(request, paciente):
        template_paciente = 'pacientes/get_paciente.html'
        res_paciente = Paciente.objects.filter(dni=paciente).first()
        # print(f'---> edit - {res_paciente.fecha_nacimiento}')
        form = FormularioPaciente(instance=res_paciente)
        context = {'form': form, 'paciente': res_paciente}
        return render(request, template_paciente, context)

    def actualizar(request, paciente):
        res_paciente = Paciente.objects.get(dni=paciente)
        # print(f'---> actualizar - {res_paciente.fecha_nacimiento}')
        form = FormularioPaciente(request.POST, instance=res_paciente)
        if form.is_valid():
            form.save()
        pacientes = Paciente.objects.all()
        context = {'lista_pacientes': pacientes}
        return render(request, 'pacientes/get_pacientes.html', context)

    def buscarPaciente(request, paciente):
        template_paciente = 'pacientes/get_pacientes.html'
        pacientes = Paciente.objects.filter(dni=paciente)
        context = {'lista_pacientes': pacientes}
        return render(request=request, template_name=template_paciente, context=context)

    def getPaciente(dni):
        res = Paciente.objects.filter(dni=dni).first()
        return res

