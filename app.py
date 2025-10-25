from flask import Flask, render_template, request
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
    alumno_clas = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data

    return render_template('alumnos.html', form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)

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



if __name__ == '__main__':
    app.run(debug=True)