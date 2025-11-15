from wtforms import Form 
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField("Matricula",[
        validators.DataRequired(message = 'El campo es requerido')
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message = 'El campo es requerido')
    ])
    apellido = StringField("Apellido",[
        validators.DataRequired(message = 'El campo es requerido')
    ])
    correo = EmailField("Correo",[
        validators.Email(message = 'Ingrese correo valido')
    ])

class ClienteForm(Form):
    nombre = StringField('Nombre Completo', [validators.DataRequired(message = 'El campo es requerido')])
    direccion = StringField('Dirección', [validators.DataRequired(message = 'El campo es requerido')])
    telefono = StringField('Teléfono', [validators.DataRequired(message = 'El campo es requerido')])
    fecha = StringField('Fecha de Compra (dd-mm-aaaa)', [validators.DataRequired(message = 'El campo es requerido')])
    submit = SubmitField('Registrar Cliente')


class PizzaForm(Form):
    tamaño = SelectField('Tamaño', choices=[('S', 'Pequeña'), ('M', 'Mediana'), ('L', 'Grande')])
    ingredientes = SelectField('Ingredientes', choices=[('Queso', 'Queso'), ('Pepperoni', 'Pepperoni'), ('Hawaiana', 'Hawaiana')])
    cantidad = IntegerField('Número de Pizzas')
    submit = SubmitField('Agregar Pizza')