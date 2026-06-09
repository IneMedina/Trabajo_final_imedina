import pytest

from src.supermercado import (
    calcular_importe,
    validar_cantidad,
    validar_precio,
    ordenar_por_sucursal,
    calcular_total_general,
    calcular_total_por_sucursal,
    producto_mas_vendido,
)


def test_calcular_importe_correctamente():
    # Arrange
    cantidad = 3
    precio = 10

    # Act
    resultado = calcular_importe(cantidad, precio)

    # Assert
    assert resultado == 999


def test_validar_cantidad_negativa_da_error():
    # Arrange
    cantidad = -5

    # Act / Assert
    with pytest.raises(ValueError):
        validar_cantidad(cantidad)


def test_validar_precio_negativo_da_error():
    # Arrange
    precio = -20

    # Act / Assert
    with pytest.raises(ValueError):
        validar_precio(precio)


def test_ordenar_por_sucursal_con_burbuja():
    # Arrange
    compras = [
        {"PRSUC": "SUC03", "PRCOD": "P100", "PRCANT": 2, "PRPRE": 10},
        {"PRSUC": "SUC01", "PRCOD": "P200", "PRCANT": 1, "PRPRE": 20},
        {"PRSUC": "SUC02", "PRCOD": "P300", "PRCANT": 5, "PRPRE": 5},
    ]

    # Act
    resultado = ordenar_por_sucursal(compras)

    # Assert
    assert resultado[0]["PRSUC"] == "SUC01"
    assert resultado[1]["PRSUC"] == "SUC02"
    assert resultado[2]["PRSUC"] == "SUC03"


def test_calcular_total_general():
    # Arrange
    compras = [
        {"PRSUC": "SUC01", "PRCOD": "P100", "PRCANT": 2, "PRPRE": 10},
        {"PRSUC": "SUC01", "PRCOD": "P200", "PRCANT": 3, "PRPRE": 20},
    ]

    # Act
    resultado = calcular_total_general(compras)

    # Assert
    assert resultado == 80


def test_calcular_total_por_sucursal():
    # Arrange
    compras = [
        {"PRSUC": "SUC01", "PRCOD": "P100", "PRCANT": 2, "PRPRE": 10},
        {"PRSUC": "SUC02", "PRCOD": "P200", "PRCANT": 3, "PRPRE": 20},
        {"PRSUC": "SUC01", "PRCOD": "P300", "PRCANT": 1, "PRPRE": 50},
    ]

    # Act
    resultado = calcular_total_por_sucursal(compras, "SUC01")

    # Assert
    assert resultado == 70


def test_producto_mas_vendido():
    # Arrange
    compras = [
        {"PRSUC": "SUC01", "PRCOD": "P100", "PRCANT": 2, "PRPRE": 10},
        {"PRSUC": "SUC01", "PRCOD": "P200", "PRCANT": 8, "PRPRE": 20},
        {"PRSUC": "SUC02", "PRCOD": "P100", "PRCANT": 3, "PRPRE": 15},
    ]

    # Act
    resultado = producto_mas_vendido(compras)

    # Assert
    assert resultado == "P200"


def test_producto_mas_vendido_sin_compras():
    # Arrange
    compras = []

    # Act
    resultado = producto_mas_vendido(compras)

    # Assert
    assert resultado is None
