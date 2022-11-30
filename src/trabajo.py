import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': '',
  'host': 'db',
  'database': 'mysql',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx._execute_query("CREATE DATABASE curso_docker")
cnx._execute_query("USE curso_docker")

cnx._execute_query("CREATE TABLE usuario (nombre VARCHAR(255) PRIMARY KEY, actividad VARCHAR(255), edad INT)")
cnx._execute_query("CREATE TABLE objeto (objeto_id INT AUTO_INCREMENT PRIMARY KEY, usuario_nombre VARCHAR(255), nombre VARCHAR(255), cantidad INT)")
#print(str(cnx._execute_query("SELECT * FROM usuario")))

#print(cnx)

class Usuario:
    """Prueba Curso de Docker"""
    def __init__(self, nombre, edad, actividad):
        self.nombre = nombre
        self.actividad = actividad
        self.edad = edad
        self.objetos = []
        query = "INSERT INTO usuario (nombre, actividad, edad) VALUES ('" + nombre + "', '" + actividad +"', " + str(edad) + ")"
        #print(query)
        cnx._execute_query(query)
    def oficio(self):
        return f"{self.nombre} trabaja en {self.actividad}"
    def cumple(self):
        self.edad += 1
        return f"Cumplirá {self.edad} años."
    def agregar(self, objeto):
        self.objetos.extend([objeto])
        query = "INSERT INTO objeto (usuario_nombre, nombre, cantidad) VALUES ('" + self.nombre + "', '" + objeto.nombre + "', " + str(objeto.cantidad) + ")"
        #print(query)
        cnx._execute_query(query)
    def cantidad(self):
        return f"Posee {len(self.objetos)} diferentes clases de objetos"
    def elementos(self):
        for objeto in self.objetos:
            print(f"{objeto.nombre} -> {objeto.cantidad} un.")
        return 1

class Objeto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    def cuantos(self):
        return f"Tiene {self.cantidad} de clase {self.nombre}"

raul = Usuario("Rulo", 49, "sistemas")
print(raul.__doc__)
print(raul.oficio())
print(raul.cumple())

libro = Objeto("Libro", 3)
raul.agregar(libro)
telefono = Objeto("Teléfono", 1)
raul.agregar(telefono)
print(raul.cantidad())
raul.elementos()

cnx._execute_query("DROP TABLE usuario")
cnx._execute_query("DROP TABLE objeto")
cnx._execute_query("DROP DATABASE curso_docker")
cnx.close()