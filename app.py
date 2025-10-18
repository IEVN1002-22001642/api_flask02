from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def home():
    titulo = "Pagina de Inicio"
    listado = ['Python','Flask','Jinja2','HTML','CSS']
    return render_template("index.html",titulo=titulo, listado=listado)

@app.route('/OPB')
def about():
    return render_template("calculo.html")

@app.route('/distancia')
def dist():
    return render_template("distancia.html")

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