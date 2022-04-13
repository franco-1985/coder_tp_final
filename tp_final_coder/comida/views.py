from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

from tp_final_coder.comida.models import Comida
from tp_final_coder.comida.forms import FormularioComida

class ComidaView(TemplateView):

    def get(request, status=None):
        template_comida = 'comida/get_comidas.html'
        comidas = Comida.objects.all()
        context={'lista_comidas':comidas}
        return render(request=request, template_name=template_comida, context=context)

    def index(request):
        template_comida = 'comida/add_comida.html'
        comida  = FormularioComida()
        context = {'form': comida}
        return render(request, template_comida, context)

    def post(request):
        template_comida = 'comida/add_comida.html'
        comida  = FormularioComida(request.POST)
        if comida.is_valid():
            comida.save()
            comida = FormularioComida()
        return render(request=request, template_name=template_comida, context={'form': comida, 'mensaje': 'OK'})
