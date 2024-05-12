from flask import Flask, render_template, request, Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        notapromedio = (nota1 + nota2 + nota3) / 3
        if notapromedio >= 40 and asistencia >= 75:
            aprobado = 'Estas aprobado con una nota de ' + str(notapromedio) + '. Felicitaciones:)'
        else:
            aprobado = "No has alcanzado el criterio de aprobacion con un promedio de: " + str(notapromedio)
        return render_template('ejercicio1.html', notapromedio=notapromedio, aprobado=aprobado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        nombres = [nombre1, nombre2, nombre3]
        largo = max(nombres, key=len)
        cantcaract = len(largo)

        return render_template('ejercicio2.html', largo=largo, cantcaract=cantcaract)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)