
# Trabajo Final Imedina- Supermercado CI

Alumno: Inés Medina  
Carrera: Licenciatura en Ciencia de Datos (LCD)


Este repositorio corresponde al trabajo práctico integrador de Git, GitHub, testing automatizado e integración continua.

## Objetivo

Implementar un sistema en Python para procesar compras de un supermercado, aplicar pruebas unitarias y automatizar la ejecución de tests mediante GitHub Actions.

## Dataset

El proyecto utiliza un archivo CSV de compras de supermercado.

Columnas principales:

- PRSUC: sucursal
- PRCOD: código de producto
- PRFEC: fecha
- PRPROV: proveedor
- PRCANT: cantidad comprada
- PRPRE: precio unitario

## Funcionalidades implementadas

El sistema permite:

- Leer compras desde un archivo CSV.
- Validar cantidades.
- Validar precios.
- Calcular importes.
- Ordenar compras por sucursal usando Burbuja.
- Calcular el total general.
- Calcular el total por sucursal.
- Identificar el producto más vendido.

## Tests

El proyecto incluye pruebas unitarias para validar las funciones principales del sistema.

Para ejecutar los tests:

```bash
pytest
