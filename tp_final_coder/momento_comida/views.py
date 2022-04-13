from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

from tp_final_coder.momento_comida.models import MomentoComida

class MomentoComidaView(TemplateView):

    def get(request, status=None):
        template_momento_comida = 'momentos/get_momentos.html'
        momentos = MomentoComida.objects.all()
        context={'lista_momentos':momentos}
        return render(request=request, template_name=template_momento_comida, context=context)
