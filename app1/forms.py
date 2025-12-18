from django import forms
from .models import *
from datetime import date
from django.core.exceptions import ValidationError

class TipoMascotaForm(forms.ModelForm):
    class Meta:
        model = TipoMascota
        fields = ['nombre', 'descripcion']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Perro'
            }),
            'descripcion': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Ej. Mascotas caninas de todas las razas',
                'rows':3
            }) 
        }

        labels = {
            'nombre':'Nombre del tipo',
            'descripcion': 'Descripcion'
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre or nombre.strip() == '':
            raise forms.ValidationError("El nombre no puede estar vacio")
        if TipoMascota.objects.filter(nombre__iexact=nombre.strip()).exists():
            raise forms.ValidationError("Este tipo de mascota ya existe")
        return nombre.strip()
    
    def clean(self):
        cleaned = super().clean()
        nombre = cleaned.get('nombre')
        descripcion = cleaned.get('descripcion')
        if nombre and descripcion and nombre.strip().lower() == descripcion.strip().lower():
            raise forms.ValidationError("El nombre y la descripcion no pueden ser iguales")
        return cleaned
    
    
class PostMascotaForm(forms.ModelForm):
    class Meta:
        model = PostMascota
        fields = ['titulo', 'descripcion', 'fecha', 'foto']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Balto jugando en el parque',
                'label': 'Título del post'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe este momento especial de la mascota...',
                'rows': 4,
                'label': 'Descripción'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',  # Muestra el calendario nativo del navegador
                'label': 'Fecha del momento'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'label': 'Fotografía'
            }),
        }
        labels = {
            'titulo': 'Título del post',
            'descripcion': 'Descripción',
            'fecha': 'Fecha del momento',
            'foto': 'Fotografía',
        }

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) < 20:
            raise ValidationError('La descripción debe tener al menos 20 caracteres.')
        return descripcion

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha > date.today():
            raise ValidationError('No se puede registrar una publicación con fecha futura.')
        return fecha