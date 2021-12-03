# challenge_entrevista
Challenge que me hicieron para una entrevista. Muy copado, me permitio aprender flask, conexion a base de datos, manipulacion de json, apis, dockers.

Challengue realizada para una entrevista. Mi primera en este mundo Python. Hay bastante para mejorar, que me fui dando cuenta luego. Esto me lo pidieron un martes, y para el miercoles a la tarde ya lo tenia terminado.

Puntos importantes en el aprendizaje:
       - Manejo de dockers, los conocia pero no habia utilziado en profundidad. Ahora me queda super claro. Como bajar y configurar.
       - Flask: era nuevo para mi, y lo entendi 100%. Me permitio entender en detalle como funcionan las APIs. 
       - Conexion a base de datos: era la tipica "luego las aprendo", y me toco aprenderla sobre la marcha. De 10, fue natural, y lo entendi al momento.

En que batalle / renegue ?
        - Parece mentira, pero en el SELECT me hizo problema con el %s, no asi en el insert. Con lo cual arme el SELECT dinamico.
        - Configure YAML para levantar el contenedor configurado, pero no logre crear las tablas en automatico. Decidi aprenderlo para mas adelante, asi no sacaba el foco a python.
        

Plantearon esto:

Montar una API con Flask (python) que tenga tres métodos: un POST para enviar registros
y dos GET para descargar el balance por empresa y por (empresa, usuario).
● Suponer que el usuario final enviará los registros por Postman (No se requiere Frontend).
● Montar una Base de datos relacional con el modelo de datos necesario.
● Cada registro consiste de :
○ el ID de la empresa
○ el ID del usuario
○ la cantidad de HA (+/-)
● Al recibir un registro, si la empresa y/o el usuario no existen en la BBDD, se registran en el
mismo momento.
● Cada usuario pertenece a una única empresa.
● La descarga de los balances puede ser un JSON, no hace falta formatearla.
