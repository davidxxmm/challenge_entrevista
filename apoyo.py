import psycopg2
from flask import jsonify
from datetime import datetime


def base_gestion(i, parametros_sql):  # Función que calcula la raíz cuadrada de un número


    connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='mysecretpassword',
            database='postgres'

    )

    cursor = connection.cursor()

    if i == 1:
        accion = "lectura por empresa"

        sql_string = "SELECT sql_movimientos.id_movimiento, sql_movimientos.id_usuario, sql_usuarios.nombre, sql_movimientos.cantidad_ha, sql_movimientos.creacion2, sql_usuarios.id_empresa, sql_empresas.nombre_empresa"
        sql_string = sql_string + " FROM sql_movimientos inner"
        sql_string = sql_string + " join sql_usuarios on sql_movimientos.id_usuario = sql_usuarios.id_usuario"
        sql_string = sql_string + " inner join sql_empresas on sql_empresas.id_empresa = sql_usuarios.id_empresa"
        sql_string = sql_string + " where sql_usuarios.id_empresa = " + parametros_sql


#        sql_string = "SELECT * FROM sql_movimientos WHERE id_empresa=" + parametros_sql
#        cursor.execute( "SELECT * FROM sql_movimientos WHERE id_empresa=%s", parametros_sql)
#        no pude encontrar el porque de TypeError: not all arguments converted during string formatting        
    elif i==2:

        accion = "lectura por empresa y usuario"


        sql_string = "SELECT sql_movimientos.id_movimiento, sql_movimientos.id_usuario, sql_usuarios.nombre, sql_movimientos.cantidad_ha, sql_movimientos.creacion2, sql_usuarios.id_empresa, sql_empresas.nombre_empresa"
        sql_string = sql_string + " FROM sql_movimientos inner"
        sql_string = sql_string + " join sql_usuarios on sql_movimientos.id_usuario = sql_usuarios.id_usuario"
        sql_string = sql_string + " inner join sql_empresas on sql_empresas.id_empresa = sql_usuarios.id_empresa"
        sql_string = sql_string + " where sql_usuarios.id_empresa = " + parametros_sql[0]
        sql_string = sql_string + " AND sql_usuarios.id_usuario = " +  parametros_sql[1]

#        sql_string = "SELECT * FROM sql_movimientos WHERE id_empresa=" + parametros_sql[0]
#        sql_string = sql_string + "AND id_usuario =" +  parametros_sql[1]

    cursor.execute(sql_string )
    rows=cursor.fetchall()

    respuesta = []
    for fila in rows:
        resp = {'Id Movimiento': fila[0],
                'Id Usuario': fila[1],
                'Nombre Usuario': fila[2],
                'Cantidad Hectareas': fila[3],
                'Creacion del registro': fila[4],
                'Empresa': fila[5],
                'Nombre de empresa': fila[6]}
        respuesta.append(resp)

    if len(respuesta) == 0:
        resp = {accion: 'Sin registro'}
        respuesta.append(resp)


    return jsonify(respuesta)

#    return (rows)

def base_grabar(parametros_sql):

    connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='mysecretpassword',
            database='postgres'

    )
# si   la empresa no estan dada de alta, hago insert del registro.

    cursor2 = connection.cursor()
    sql_empresa = "SELECT * from sql_empresas WHERE id_empresa = " + parametros_sql[0]
    cursor2.execute(sql_empresa)
    rows = cursor2.fetchall()
    if len(rows) == 0:
        print ( "hacer insert de empresa")
        datos_insert_empresa = (parametros_sql[0], "Empresa " + parametros_sql[0])

        sql_insert_empresa = "INSERT INTO sql_empresas ( id_empresa, nombre_empresa) "
        sql_insert_empresa =  sql_insert_empresa + "VALUES (%s, %s) "

        cursor3 = connection.cursor()
        cursor3.execute(sql_insert_empresa, datos_insert_empresa)
        connection.commit()

# si   el usuario no existe, no estan dada de alta, hago insert del registro.

    cursor5 = connection.cursor()
    sql_empresa = "SELECT * from sql_usuarios WHERE id_usuario = " + parametros_sql[1]
    cursor5.execute(sql_empresa)
    rows = cursor5.fetchall()
    if len(rows) == 0:
        print ( "hacer insert de usuario")
        datos_insert_usuario = (parametros_sql[1], parametros_sql[0], "Usuario " + parametros_sql[1])

        sql_insert_usuario = "INSERT INTO sql_usuarios ( id_usuario, id_empresa, nombre) "
        sql_insert_usuario =  sql_insert_usuario + "VALUES (%s, %s, %s) "

        cursor6 = connection.cursor()
        cursor6.execute(sql_insert_usuario, datos_insert_usuario)
        connection.commit()


    cursor = connection.cursor()
    fechahora =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datos_internos=( parametros_sql[1],parametros_sql[2], fechahora)
    sql_inserx = "INSERT INTO public.sql_movimientos ( id_usuario, cantidad_ha, creacion2) VALUES (%s, %s, %s)"

    cursor.execute(sql_inserx, datos_internos)
    connection.commit()

    respuesta = []
    resp = {'Registro Agregado': fechahora,
            'Id Usuario': parametros_sql[1],
            'Cantidad de Hectareas': parametros_sql[2]}
    respuesta.append(resp)

    return jsonify(respuesta)