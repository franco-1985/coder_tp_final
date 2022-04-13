from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

from tp_final_coder.momento_comida.models import MomentoComida
from tp_final_coder.momento_comida.forms import FormularioMomentoComida

class MomentoComidaView(TemplateView):

    def get(request, status=None):
        template_momento_comida = 'momentos/get_momentos.html'
        momentos = MomentoComida.objects.all()
        context={'lista_momentos':momentos}
        return render(request=request, template_name=template_momento_comida, context=context)

    def index(request):
        template_momento = 'momentos/add_momentos.html'
        momento  = FormularioMomentoComida()
        context = {'form': momento}
        return render(request, template_momento, context)

    def post(request):
        template_momento = 'momentos/add_momentos.html'
        momento  = FormularioMomentoComida(request.POST)
        if momento.is_valid():
            momento.save()
            momento = FormularioMomentoComida()
        return render(request=request, template_name=template_momento, context={'form': momento, 'mensaje': 'OK'})
