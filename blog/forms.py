from django import forms
from django.forms import ModelForm
from blog.models import Mensaje
from captcha.fields import CaptchaField

class MensajeForm(ModelForm):
    
    # captcha = CaptchaField()

    class Meta:
        model = Mensaje
        fields = [
            'nombre',
            'email',
            'asunto',
            'mensaje',
        ]
    def __init__(self, *args, **kwargs):
        super(MensajeForm,self).__init__(*args,**kwargs)

    def send_email(self):
        nombre = self.cleaned_data['nombre']
        descripcion = self.cleaned_data['email']
        mail = self.cleaned_data['asunto']
        telefono = self.cleaned_data['mensaje']

        ## A partir de acá genero la logica de envio de mail