from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .registrationForm import RegistrationForm  # Importar correctamente el formulario de registro
from .models import Question

# Vista de inicio de preguntas
def index(request):
    # Obtener las preguntas desde la base de datos
    questions = Question.objects.all()  # Aquí puedes filtrar las preguntas según lo necesites
    return render(request, 'index.html', {'questions': questions})

# Vista para iniciar sesión o registrarse
def login_view(request):
    # Inicializamos los formularios
    form_login = AuthenticationForm(request)  # Formulario de login
    form_register = RegistrationForm()  # Formulario de registro

    if request.method == 'POST':
        # Procesar el formulario de login
        if 'login' in request.POST:
            form_login = AuthenticationForm(request, data=request.POST)
            if form_login.is_valid():  # Valida los datos
                username = form_login.cleaned_data['username']
                password = form_login.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)  # Inicia sesión
                    return redirect('index')  # Redirige a la página principal
                else:
                    form_login.add_error(None, "Las credenciales no son correctas.")
        # Procesar el formulario de registro
        elif 'register' in request.POST:
            form_register = RegistrationForm(request.POST)  # Formulario de registro con los datos POST
            if form_register.is_valid():
                user = form_register.save()  # Crea el usuario
                login(request, user)  # Inicia sesión automáticamente
                return redirect('index')  # Redirige a la página principal

    # Si el formulario no es válido o es un GET, renderiza la página de login
    return render(request, 'ligin.html', {
        'form_login': form_login,  # Pasa el formulario de login
        'form_register': form_register,  # Pasa el formulario de registro
    })