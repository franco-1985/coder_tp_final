# TP Final Coder

## Consideraciones

Funcionalidades realizadas: (entrega parial)
 - Se agrega formulario para registro y login de usurios. 
 - Se agrega formulario para indicar que aun no esta realizada la funcionalidad. 

Problemas:
 - No puedo hacer generar una lista seleccionable en un formulario ya que necesito para poder registrar datos en una tabla transaccional.
 - Se pueden agregar correctamente usuarios a la plataforma pero no se puede loguear, solo puedo hacer que el login se haga con los usuarios creados con el administrador de Django.
 - Requiero, por favor, 7 dias para poder realizar una nueva entrega.
 - Por falta de tiempo, no se realizo la parte de testing.
 - Por falta de tiempo, no se realizo el video.

Funcionalidades realizadas:
 - Formulario de listado de comidas cargadas: mostrar las comidas que tiene cargada el sistema
 - Formulario de registro de comidas: permitir registrar una comida
 - Formulario de listado de momentos de comidas: mostrar los momentos de comidas cargados
 - Formulario de registro de pacientes: registrar nuevos pacientes
 - Formulario de listado de pacientes: mostrar el listado de pacientes, permitiendo editar cada registro. Tambien permite registar (falta desarrollar) y visualizar registro de comidas y medidas para cada paciente.

Trabajo final del curso de coderhouse

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy tp_final_coder

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.
