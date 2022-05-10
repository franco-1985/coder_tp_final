from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

from tp_final_coder.comida.views import ComidaView
from tp_final_coder.paciente.views import PacienteView
from tp_final_coder.momento_comida.views import MomentoComidaView
from tp_final_coder.transaccional.views import ComidaPacienteView
from tp_final_coder.transaccional.views import PesoPacienteView

from tp_final_coder.login.views import LoginView, RegisterView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="base_v2.html"), name="home"),
    # referido a pacientes
    path("pacientes/", PacienteView.get, name="get_pacientes"),
    path("editarPacientes/<int:paciente>", PacienteView.edit, name="get_paciente"),
    path("actuPaciente/<int:paciente>", PacienteView.actualizar, name="actu_paciente"),
    path("agregarPaciente/", PacienteView.post, name="add_pacientes"),
    path("registrarPaciente/", PacienteView.index, name="registrar_pacientes"),
    path("buscarPaciente/<int:paciente>", PacienteView.buscarPaciente,name="bus_paciente"), # no funciona
    # verificar pantalla de abajo
    path("registrarPesoPaciente/<int:paciente>", PesoPacienteView.index , name="registrar_medidas"),
    path("addMedidaPaciente/", PesoPacienteView.post, name="add_medidas"),
    # path("addMedidaPaciente/<int:paciente>", PesoPacienteView.post, name="add_medidas"), # url vieja que andaba a media
    path("historialPesoPaciente/<int:paciente>", PesoPacienteView.buscar_medidas, name="historial_medidas"),
    path("historialComidaPaciente/<int:paciente>", ComidaPacienteView.buscar_comidas, name="historial_comida"),
    path("registrarComidaPaciente/<int:paciente>", ComidaPacienteView.registrar_comida_paciente, name="registrar_comida_paciente"),

    #REPETIR ESTO PARA REGISTRAR LA COMIDA, PERO TENER EN CUENTA LA ANTERIOR.
    #path("registrarPesoPaciente/<int:paciente>", PesoPacienteView.index, name="registrar_medidas"),
    #path("addMedidaPaciente/", PesoPacienteView.post, name="add_medidas"),

    # referido a comidas
    path("comida/", ComidaView.get, name="get_comidas"),
    path("momentosComida/", MomentoComidaView.get, name="get_momentos"),
    path("addMomentosComida/", MomentoComidaView.post, name="add_momentos"),
    path("registrarMomentosComida/", MomentoComidaView.index, name="registrar_momentos"),
    path("agregarComida/", ComidaView.post, name="add_comidas"),
    path("registrarComida/", ComidaView.index, name="registrar_comidas"),

    path("login/",LoginView.as_view(),name="login"),
    path("registro/",RegisterView.as_view(),name="registro"),


    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
