from flask import Flask, redirect, render_template, request
from flask import *
from flask_mysqldb import MySQL



app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_DB'] = 'proyectowebflask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql.init_app(app)

@app.route('/')
def index():
    sql = "SELECT * FROM equipos "
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql)
    equipos = cursor.fetchall()
    conexion.commit()
    return render_template('sitio/index.html', equipos=equipos)


@app.route('/sitio/guardar', methods = ['POST'])
def guardar():
    descripcion = request.form['descripcion']
    email = request.form['email']
    sql = "INSERT INTO equipos(descripcion, email) VALUES (%s,%s)"
    datos = (descripcion, email)
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/')

@app.route('/sitio/borrar/<int:codigo>')
def borrar(codigo):
    sql = "DELETE FROM equipos WHERE codigo = %s"
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, (codigo,))
    conexion.commit()
    return redirect('/')

@app.route('/sitio/editar/<int:codigo>')
def ediatar(codigo):
    sql = "SELECT * FROM equipos WHERE codigo = %s"
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, (codigo,))
    equipo = cursor.fetchone()
    conexion.commit()
    return render_template('/sitio/editar.html', equipo=equipo)

@app.route('/sitio/actualizar', methods = ['POST'])
def actualizar():
    descripcion = request.form['descripcion']
    email = request.form['email']
    codigo = request.form['codigo']
    sql = "UPDATE equipos set descripcion= %s, email=%s WHERE codigo= %s"
    datos = (descripcion, email, codigo)
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/')

#PARTE PARCIAL CORTE 1

@app.route('/usuario')
def usuarios():
    sql = "SELECT * FROM usuarios "
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    conexion.commit()
    return render_template('/sitio/amd_usuario.html', usuarios = usuarios)

@app.route('/sitio/actualizar_user', methods = ['POST'])
def actualizar_user():
    username = request.form['Username']
    password = request.form['Password']
    id = request.form['ID']
    sql = "UPDATE usuarios set username= %s, password=%s WHERE id= %s"
    datos = (username, password, id)
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/usuario')

@app.route('/sitio/borrarUsuario/<int:codigo>')
def borrarUsusario(codigo):
    sql = "DELETE FROM usuarios WHERE ID = %s"
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, (codigo,))
    conexion.commit()
    return redirect('/usuario')

@app.route('/sitio/editarUsuario/<int:id>')
def editarUsuario(id):
    sql = "SELECT * FROM usuarios WHERE ID = %s"
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, (id,))
    usuario = cursor.fetchone()
    conexion.commit()
    return render_template('/sitio/editarUsuario.html', usuario = usuario)

@app.route('/sitio/guardarUsuario', methods = ['POST'])
def guardarUsuario():
    username = request.form['username']
    password = request.form['password']
    sql = "INSERT INTO usuarios(Username, Password) VALUES (%s,%s)"
    datos = (username, password)
    conexion = mysql.connection
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect('/usuario')

if __name__ == '__main__':
    app.run(debug = True)