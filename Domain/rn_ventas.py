# Reglas de negocio - Venta
from datetime import datetime
import re


class VentaRules:
    @staticmethod
    def validar_creacion(datos):
        # 1. Validar existencia del diccionario
        if not datos:
            raise ValueError("Debe enviar información sobre la venta")

        # 2. Validar presencia de campos requeridos
        campos_requeridos = ["fecha_venta", "monto_venta", "id_sucursal"]
        for campo in campos_requeridos:
            if campo not in datos or datos[campo] is None:
                raise ValueError("Los campos fecha_venta, monto_venta e id_sucursal son requeridos")

        # 3. Validar que la fecha no sea una cadena vacía
        fecha_str = str(datos["fecha_venta"]).strip()
        if not fecha_str:
            raise ValueError("La fecha de venta no puede estar vacía")

        # 4. Validar formato y coherencia de la fecha (YYYY-MM-DD)
        try:
            fecha_venta = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha de venta debe tener el formato YYYY-MM-DD")

        if fecha_venta > datetime.now():
            raise ValueError("La fecha de venta no puede ser futura")

        # 5. Validar monto
        try:
            monto = float(datos["monto_venta"])
            if monto <= 0:
                raise ValueError("El monto de venta debe ser mayor a cero")
        except (ValueError, TypeError):
            raise ValueError("El monto de venta debe ser un número válido")

    @staticmethod
    def validar_identificador(valor, nombre_campo="identificador"):
        if valor is None or not str(valor).strip():
            raise ValueError(f"El {nombre_campo} no puede estar vacío")
        if not re.fullmatch(r"[A-Za-z0-9]+", str(valor)):
            raise ValueError(f"El {nombre_campo} solo puede tener letras y números")