import sqlite3

DATABASE = 'ClinicaOdontologica.db'

def obtener_conexion():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion
