from django import forms
from .models import Tarea

class FormularioTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200',
                'placeholder': '¿Qué necesitas hacer?',
                'autocomplete': 'off'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200',
                'placeholder': 'Describe los detalles de la tarea...',
                'rows': 4,
                'autocomplete': 'off'
            }),
        }
        labels = {
            'titulo': 'Título de la tarea',
            'descripcion': 'Descripción',
        }
        help_texts = {
            'titulo': 'Escribe un título claro y descriptivo',
            'descripcion': 'Opcional - Puedes agregar más detalles aquí',
        }

class FormularioEditarTarea(FormularioTarea):
    class Meta(FormularioTarea.Meta):
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'Título de la tarea',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition duration-200',
                'placeholder': 'Descripción de la tarea...',
                'rows': 4
            }),
        }