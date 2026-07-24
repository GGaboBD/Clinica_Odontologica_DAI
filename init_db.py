from database import obtener_conexion

# La base se crea automáticamente al ejecutar este archivo.
# El archivo ClinicaOdontologica.db ya queda listo para DBeaver.

if __name__ == '__main__':
    conexion = obtener_conexion()
    conexion.close()
    print('Base SQLite lista: ClinicaOdontologica.db')
