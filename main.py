from flask import Flask
from flask import request
from apoyo import  base_gestion
from apoyo import base_grabar
from flask import jsonify

app = Flask(__name__)

 
# metodo para leer por usuario
@app.route("/app/v1/leer_empresa")
def leer_empresa():

  datos = (request.form['empresa'])
  respuesta = base_gestion(1, datos)

  return  respuesta


# metodo para leer por  empresa y usuario 
@app.route("/app/v1/leer_empresa_usuario")
def leer_empresa_usuario():

  datos = (request.form['empresa'], request.form['usuario'])
  respuesta = base_gestion(2, datos)

  return  respuesta

# metodo para grabar las hectareas 
@app.route("/app/v1/grabar_registro", methods=["GET", "POST"])
def grabar_registro():


  accion = "grabar por hectareas"

  if (request.method == "GET"):
                accion = "no hace nada"
  elif (request.method ==  "POST"):
                accion = "guardar datos"
                datos = (request.form['empresa'], request.form['usuario'], request.form['cantidad_ha'])
                respuesta = base_grabar(datos)

  return ( respuesta )




app.run(debug=True)