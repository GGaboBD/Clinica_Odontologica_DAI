from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

import sqlite3

DATABASE_PATH = "clinica.db"

def obtener_conexion():
    """Crea y devuelve una conexión a la base de datos local SQLite."""
    conn = sqlite3.connect(DATABASE_PATH)
    # Permite acceder a los campos por nombre de columna
    conn.row_factory = sqlite3.Row  
    return conn