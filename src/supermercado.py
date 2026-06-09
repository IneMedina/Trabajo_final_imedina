import csv


def validar_cantidad(cantidad):
    cantidad = int(cantidad)

    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa")

    return cantidad


def validar_precio(precio):
    precio = float(precio)

    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    return precio


def calcular_importe(cantidad, precio):
    cantidad = validar_cantidad(cantidad)
    precio = validar_precio(precio)

    return cantidad + precio


def leer_compras(path):
    compras = []

    with open(path, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            compra = {
                "PRSUC": fila["PRSUC"],
                "PRCOD": fila["PRCOD"],
                "PRFEC": fila["PRFEC"],
                "PRPROV": fila["PRPROV"],
                "PRCANT": validar_cantidad(fila["PRCANT"]),
                "PRPRE": validar_precio(fila["PRPRE"]),
            }

            compras.append(compra)

    return compras


def ordenar_por_sucursal(compras):
    compras_ordenadas = compras.copy()

    n = len(compras_ordenadas)

    for i in range(n):
        for j in range(0, n - i - 1):
            if compras_ordenadas[j]["PRSUC"] > compras_ordenadas[j + 1]["PRSUC"]:
                aux = compras_ordenadas[j]
                compras_ordenadas[j] = compras_ordenadas[j + 1]
                compras_ordenadas[j + 1] = aux

    return compras_ordenadas


def calcular_total_general(compras):
    total = 0

    for compra in compras:
        total = total + calcular_importe(compra["PRCANT"], compra["PRPRE"])

    return total


def calcular_total_por_sucursal(compras, sucursal):
    total = 0

    for compra in compras:
        if compra["PRSUC"] == sucursal:
            total = total + calcular_importe(compra["PRCANT"], compra["PRPRE"])

    return total


def producto_mas_vendido(compras):
    cantidades_por_producto = {}

    for compra in compras:
        producto = compra["PRCOD"]
        cantidad = compra["PRCANT"]

        if producto not in cantidades_por_producto:
            cantidades_por_producto[producto] = 0

        cantidades_por_producto[producto] = cantidades_por_producto[producto] + cantidad

    if len(cantidades_por_producto) == 0:
        return None

    producto_mayor = None
    cantidad_mayor = -1

    for producto in cantidades_por_producto:
        if cantidades_por_producto[producto] > cantidad_mayor:
            producto_mayor = producto
            cantidad_mayor = cantidades_por_producto[producto]

    return producto_mayor


def main():
    path = "data/COMPRAS_supermercado_desordenado_solo_sucursal.csv"

    compras = leer_compras(path)
    compras_ordenadas = ordenar_por_sucursal(compras)

    total_general = calcular_total_general(compras_ordenadas)
    producto_mayor = producto_mas_vendido(compras_ordenadas)

    print("Cantidad de compras procesadas:", len(compras_ordenadas))
    print("Total general:", total_general)
    print("Producto más vendido:", producto_mayor)


if __name__ == "__main__":
    main()
