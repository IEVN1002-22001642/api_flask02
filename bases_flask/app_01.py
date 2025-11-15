from flask import Flask, render_template, request
from flask import make_response, jsonify, json
import math
import forms

app = Flask(__name__)

@app.route('/index')
def home():
    titulo = "Pagina de Inicio"
    listado = ['Python','Flask','Jinja2','HTML','CSS']
    return render_template("index.html",titulo=titulo, listado=listado)

@app.route('/calculo', methods = ['GET','POST'])
def about():
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        opcin = request.form['operacion']
        if opcin == 'suma':
            res = int(numero1) + int(numero2)
        if opcin == 'resta':
            res = int(numero1) - int(numero2)
        if opcin == 'multiplicacion':
            res = int(numero1) * int(numero2)
        if opcin == 'division':
            res = int(numero1) / int(numero2)
        return render_template('calculo.html', res = res, numero1 = numero1, numero2 = numero2)

    return render_template("calculo.html")

@app.route('/distancia', methods = ['GET','POST'])
def dist():
    if request.method == 'POST':
        x1 = request.form['x1']
        x2 = request.form['x2']
        y1 = request.form['y1']
        y2 = request.form['y2']

        resu = math.sqrt(math.pow(int(x2) - int(x1), 2) + math.pow(int(y2) - int(y1), 2))
        return render_template('distancia.html', resu = resu, x1 = x1, x2 = x2, y1 = y1, y2 = y2)

    return render_template("distancia.html")


@app.route("/Alumnos",methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    email=""
    tem=[]
    estudiantes=[]
    datos={}

    alumno_clas = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        if request.form.get("btnElimina")=='eliminar':
            response = make_response(render_template('Alumnos.html',))
            response.delete_cookie('usuario')

        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data

        datos={'matricula':mat,'nombre':nom.rstrip(),
               'apellido':ape.rstrip(),'email':email.rstrip()}  
        data_str = request.cookies.get("usuario")
        if not data_str:
             return "No hay cookie guardada", 404
        estudiantes = json.loads(data_str)
        estudiantes.append(datos)  
    response=make_response(render_template('Alumnos.html',
        form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email))

    if request.method!='GET':
        response.set_cookie('usuario', json.dumps(tem))
    return response

@app.route("/get_cookie")
def get_cookie():
     
    data_str = request.cookies.get("usuario")
    if not data_str:
        return "No hay cookie guardada", 404
 
    estudiantes = json.loads(data_str)
 
    return jsonify(estudiantes)

@app.route('/user/<string:user>')
def user(user):
    return f"Hello {user}!"

@app.route("/number/<int:num>")
def func(num):
    return f"El numero es {num}"

@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1, num2):
    return f"La suma de {num1} y {num2} es {num1 + num2}"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} Nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def sumn(n1,n2):
    return "la suma es: {}".format(n1+n2)

@app.route("/default/")
@app.route("/default/<string:dft>")
def func2(dft="sss"):
    return "el valor de dft es: " + dft

@app.route("/prueba")
def func4():
    return'''
        <html>
            <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                <title>Pagina de prueba</title>
            </head>
            <body>
                <h1>Hola esta es una pagina de prueba</h1>
                <p>Esta pagina es para probar el retorno de HTML en Flask</p>
            </body>
        </html>
    '''

@app.route('/pizza', methods=['GET', 'POST'])
def index():
    # Inicializar variables
    nom  = dir = telefono = fecha = ""
    cliente_data = {}
    pizzas = []

    cliente_form = forms.ClienteForm(request.form)
    pizza_form = forms.PizzaForm(request.form)

    if request.method == 'POST' and cliente_form.validate():
        # Datos del cliente
        nom = cliente_form.nombre.data
        dir = cliente_form.direccion.data
        tel = cliente_form.telefono.data
        fecha = cliente_form.fecha.data
        
        cliente_data = {'nombre': nom, 'direccion': dir, 'telefono': tel, 'fecha': fecha, 'pizzas': []}

        response = make_response(render_template('pizza.html', cliente_form=cliente_form, pizza_form=pizza_form, cliente_data=None))
        response.set_cookie('cliente_data', json.dumps(cliente_data))  # Guardar cliente en cookie
        return response

    # Si se presiona el botón de agregar pizza
    if request.method == 'POST' and pizza_form.validate():
        data_str = request.cookies.get('cliente_data')
        if data_str:
            cliente_data = json.loads(data_str)
            if 'pizzas' not in cliente_data:
                cliente_data['pizzas'] = []

            pizza = {
                'tamaño': pizza_form.tamaño.data,
                'ingredientes': pizza_form.ingredientes.data,
                'cantidad': pizza_form.cantidad.data,
                'subtotal': pizza_form.cantidad.data * 100  # Precio ejemplo
            }
            cliente_data['pizzas'].append(pizza)

            # Actualizar cookies
            response = make_response(render_template('pizza.html', cliente_form=cliente_form, pizza_form=pizza_form, cliente_data=cliente_data))
            response.set_cookie('cliente_data', json.dumps(cliente_data))  # Actualizar cliente en cookie
            return response

    return render_template('pizza.html', cliente_form=cliente_form, pizza_form=pizza_form, cliente_data=cliente_data)

@app.route('/terminar', methods=['POST'])
def terminar():
    # Extraer datos del pedido
    cliente_data = request.cookies.get('cliente_data')
    cliente_data = json.loads(cliente_data) if cliente_data else {}

    if 'pizzas' not in cliente_data:
        return redirect(url_for('index'))

    # Calcular el total
    total = sum(pizza['subtotal'] for pizza in cliente_data['pizzas'])
    cliente_data['total'] = total

    # Guardar venta en cookies
    ventas_cookie = request.cookies.get('ventas', '[]')
    ventas = json.loads(ventas_cookie)
    ventas.append({
        'nombre': cliente_data['nombre'],
        'direccion': cliente_data['direccion'],
        'telefono': cliente_data['telefono'],
        'fecha': cliente_data['fecha'],
        'total': total
    })

    response = make_response(render_template('pizza.html', cliente_form=None, pizza_form=None, cliente_data=None, ventas=ventas))
    response.set_cookie('cliente_data', '')  # Limpiar cookie cliente_data
    response.set_cookie('ventas', json.dumps(ventas))  

    return response

@app.route('/ventas', methods=['GET'])
def ventas():
    ventas_cookie = request.cookies.get('ventas', '[]')
    ventas = json.loads(ventas_cookie)
    return render_template('pizza.html', ventas=ventas)



if __name__ == '__main__':
    app.run(debug=True)