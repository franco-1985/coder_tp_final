from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from tp_final_coder.users.models import User

from django.contrib import auth

from tp_final_coder.login.forms import FormRegistro


class UserCreationFormCustom(FormRegistro):
    def save(self, commit: bool= True) -> User:
        print(self.__dict__)
        self.data
        user = User.objects.create(username= self.data['username'] )
        return user


class RegisterView(TemplateView):
    template_name = "v2_login/register.html";

    def get(self, request):
        context = {
            'form': UserCreationFormCustom()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationFormCustom(request.POST)
        if form:
            form.save()
            return render(request, self.template_name, context={'message': 'Usuario creado'})
        else:
            return render(request, self.template_name, context={'message': 'Error'})

class LoginView (TemplateView):
    template_name= "v2_login/login.html"

    def get(self, request):
        context = {
            'form': AuthenticationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):

        form = AuthenticationForm(request, data=request.POST)
        if form:
            user = request.POST.get('username')
            passw = request.POST.get('password')
            # print(f'---->{user} - {passw}')

            user_auth = auth.authenticate(username=user, password = passw)
            # print(user_auth)
            if user_auth:
                auth.login(request, user_auth)
                return render(request, self.template_name, context={'message': f'Bienvenido {user}'})
            else:
                return render(request, self.template_name, context={'message': f'El usuario {user} no existe'})

        else:
            return render(request, self.template_name, context={'message':'Formulario errado'})
