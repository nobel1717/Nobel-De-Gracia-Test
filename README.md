# Nobel De Gracia Test
 Sistema de Automatización y Análisis de Pedidos

En esta prueba, desarrollé un script en Python para automatizar el análisis y procesamiento de pedidos a partir de un archivo JSON. Durante mi análisis, identifiqué las necesidades clave del equipo y diseñé un flujo que cumple con los siguientes objetivos:

1. Procesamiento de Pedidoss
Filtra los pedidos con estado "pendiente" para enfocarse en los más relevantes para el análisis.
Se valida que el monto del pedido coincidiera con la suma de (cantidad * precio_unitario) de los ítems. En caso de alguna excepción, se registra los id_pedido con errores en un archivo CSV llamado errores.csv.
2. Generación de Reportes
Se crea un archivo CSV, pedidos_pendientes.csv, que incluye los pedidos pendientes con columnas como id_pedido, cliente, fecha, monto, y el número total de productos.
Se agrega una fila de resumen al CSV, mostrando el monto total y el promedio de los pedidos pendientes, lo que permite un análisis rápido y conciso.
3. Análisis Avanzado
Identifica al cliente con el mayor monto acumulado en pedidos completados destacando al cliente más valioso, cuyo monto total se registra en un archivo JSON llamado cliente_destacado.json.
4. Automatización
Diseñé un flujo automatizado que:
Lee el archivo JSON original.
Procesa y analiza los datos.
Genera los archivos requeridos:
-pedidos_pendientes.csv: Reporte de pedidos pendientes.
-errores.csv: Lista de pedidos con inconsistencias en el monto.
-cliente_destacado.json: Información del cliente con el mayor monto acumulado.