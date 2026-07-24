import sqlite3

DATABASE = 'ClinicaOdontologica.db'

def obtener_conexion():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion

def convertir_fila_a_diccionario(fila):
    if fila is None:
        return None
    return dict(fila)