from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistrationForm(forms.Form):
    # Personalizando mensaje para el campo obligatorio de 'username'
    username = forms.CharField(
        max_length=30, 
        required=True,
        error_messages={
            'required': 'Por favor, ingresa un nombre de usuario.',  # Mensaje para el campo vacío
        }
    )
    
    # Personalizando mensaje para el campo obligatorio de 'email'
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'Por favor, ingresa un correo electrónico.',
        }
    )
    
    # Personalizando mensaje para el campo obligatorio de 'password'
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            'required': 'Por favor, ingresa una contraseña.',
        }
    )
    
    # Personalizando mensaje para el campo obligatorio de 'password_confirm'
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            'required': 'Por favor, confirma tu contraseña.',
        }
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        
        # Verifica que el nombre de usuario solo contenga letras
        if not username.isalpha():
            print("Error: El nombre de usuario contiene caracteres no alfabéticos.") 
            raise ValidationError("El nombre de usuario debe contener solo letras.")
        
        # Verifica si el nombre de usuario ya está registrado
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está registrado.")
        
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        # Verificación del dominio del correo electrónico
        valid_domains = ['@sena.edu.co', '@gmail.com']
        if not any(email.endswith(domain) for domain in valid_domains):
            raise ValidationError("El correo electrónico debe tener un dominio válido.")
        
        # Verifica si el correo ya está registrado
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        return user
