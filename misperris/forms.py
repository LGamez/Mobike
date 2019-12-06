from django import forms
from mysite import settings

class check(forms.Form):
    select=forms.CheckboxInput()

class EstadoP(forms.Form):
    CHOICES = (('Rescatados', 'Rescatados'),('Disponibles', 'Disponibles'),
    ('Adoptados','Adoptados')
    )

    estado=forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class' : 'estado_perro'}))

class FormPerro(forms.Form):
    CHOICES = (('Rescatados', 'Rescatados'),('Disponibles', 'Disponibles'),
    ('Adoptados','Adoptados')
    )

    nombre=forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'form-control'})) 
    raza=forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'form-control'})) 
    descripcion=forms.CharField(max_length=70,widget=forms.Textarea(attrs={'class' : 'form-control'})) 
    estado=forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class' : 'form-control'}))
    foto=forms.FileField()

class Login(forms.Form):
    usuario=forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'input100','placeholder':'Nombre'}))
    contraseña=forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'input100','placeholder':'Contraseña','type':'password'}))

class Registro(forms.Form):
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField(max_length=100)
    myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'campos nombres'}))

class Dueño(forms.Form):
    CHOICES = (('Casa con Patio Grande', 'Casa con Patio Grande'),('Casa con patio Pequeño', 'Casa con patio Pequeño'),
    ('Casa sin patio','Casa sin patio'),('Departamento','Departamento')
    )

    REGION= (('I de Tarapacá', 'I de Tarapacá'),('II de Antofagasta', 'II de Antofagasta'),
    ('III de Atacama','III de Atacama'),
    ('IV de Coquimbo','IV de Coquimbo')
    ,('V de Valparaíso','V de Valparaíso')
    ,('VI del Libertador General Bernardo O’Higgins','VI del Libertador General Bernardo O’Higgins'),
    ('VII del Maule','VII del Maule'),('VIII de Concepción','VIII de Concepción'),('IX de la Araucanía','IX de la Araucanía'),('X de Los Lagos','X de Los Lagos'),('XI de Aysén del General Carlos Ibañez del Campo','XI de Aysén del General Carlos Ibañez del Campo'),('XII de Magallanes y de la Antártica Chilena','XII de Magallanes y de la Antártica Chilena'),('Metropolitana de Santiago','Metropolitana de Santiago'),('XIV de Los Ríos','XIV de Los Ríos'),('XV de Arica y Parinacota','XV de Arica y Parinacota'),('XVI del Ñuble','XVI del Ñuble'))

    COMUNA =(('Santiago', 'Santiago'),('Iquique', 'Iquique'),
    ('Valdivia','Valdivia'),
    ('Concepción','Concepción')
    ,('Temuco','Temuco')
    ,('La Serena','La Serena'),
    ('Puerto Montt','Puerto Montt'),('Chillán','Chillán'),('Rancagua','Rancagua'),('Punta Arenas','Punta Arenas'),('Talca','Talca'),('Viña del Mar','Viña del Mar'),('Arica','Arica'),('Calama','Calama'),('Copiapó','Copiapó'),('Osorno','Osorno'),('Coyhaique','Coyhaique'),('Curicó','Curicó'),('Antofagasta','Antofagasta'),('Los Angeles','Los Angeles'),('Ovalle','Ovalle'),('San Pedro de Atacama','San Pedro de Atacama'),('Pucón','Pucón'),('Castro','Castro'),('La Ligua','La Ligua'),('San Fernando','San Fernando'),('Puerto Varas','Puerto Varas'),('Talcahuano','Talcahuano'),('Valparaiso','Valparaiso'),('Quilpué','Quilpué'),('Melipilla','Melipilla'),('Quillota','Quillota'),('San Felipe','San Felipe'),('Angol','Angol'),('Cauquenes','Cauquenes'),('Villa Rica','Villa Rica'),('Linares','Linares'),('Illapel','Illapel'),('Concón','Concón'),('Constitución','Constitución'),('San Bernardo','San Bernardo'),('San Antonio','San Antonio'),('Coronel','Coronel'),('Pichilemu','Pichilemu'),('Santa Cruz','Santa Cruz'),('Vallenar','Vallenar'),('Cañete','Cañete'),('Yumbel','Yumbel'))
        
    email=forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'input100'}))    
    run= forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'input100'}))
    nombre = forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'input100'}))
    apellido = forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class' : 'input100'}))
    fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,widget=forms.TextInput(attrs={'class' : 'input100'}))
    telefono = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'input100'}))
    region = forms.ChoiceField(choices=REGION,widget=forms.Select(attrs={'class' : 'selection-2'}))
    ciudad = forms.ChoiceField(choices=COMUNA,widget=forms.Select(attrs={'class' : 'selection-2'}))
    tipo = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class' : 'selection-2'}))

class Estado(forms.Form):
    CHOICES = (('Rescatados', 'Rescatados'),('Disponibles', 'Disponibles'),
    ('Adoptados','Adoptados')
    )

    estado = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class' : 'selection-2'}))
    
