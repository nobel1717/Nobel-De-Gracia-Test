import json
import csv
from collections import defaultdict

# Lectura del archivo JSON
with open('pedidos.json', 'r') as file:
    pedidos = json.load(file)

archivo_errores = 'errores.csv'
archivo_pendientes = 'pedidos_pendientes.csv'
archivo_cliente_destacado = 'cliente_destacado.json'

pedidos_pendientes = []
errores = []
clientes_acumulados = defaultdict(float)

# Procesamiento de pedidos
for pedido in pedidos:
    id_pedido = pedido["id_pedido"]
    cliente = pedido["cliente"]
    estado = pedido["estado"]
    monto = pedido["monto"]
    items = pedido["items"]
    
    # Validación de monto
    monto_calculado = sum(item["cantidad"] * item["precio_unitario"] for item in items)
    if monto != monto_calculado:
        errores.append({"id_pedido": id_pedido})
        continue  
    
    # Acumular monto por cliente
    if estado == "completado":
        clientes_acumulados[cliente] += monto
    
    # Filtrar pedidos pendientes
    if estado == "pendiente":
        total_items = sum(item["cantidad"] for item in items)
        pedidos_pendientes.append({
            "id_pedido": id_pedido,
            "cliente": cliente,
            "fecha": pedido["fecha"],
            "monto": monto,
            "total_items": total_items
        })

#  archivo de errores
with open(archivo_errores, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id_pedido"])
    writer.writeheader()
    writer.writerows(errores)

# archivo CSV de pedidos pendientes
monto_total = sum(p["monto"] for p in pedidos_pendientes)
promedio_monto = monto_total / len(pedidos_pendientes) if pedidos_pendientes else 0

with open(archivo_pendientes, 'w', newline='') as file:
    fieldnames = ["id_pedido", "cliente", "fecha", "monto", "total_items"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(pedidos_pendientes)
    
    writer.writerow({
        "id_pedido": "TOTAL",
        "cliente": "",
        "fecha": "",
        "monto": monto_total,
        "total_items": promedio_monto
    })

# Identificar cliente destacado
cliente_destacado = max(clientes_acumulados.items(), key=lambda x: x[1], default=(None, 0))

if cliente_destacado[0]:
    cliente_info = {
        "cliente": cliente_destacado[0],
        "monto_acumulado": cliente_destacado[1]
    }
    with open(archivo_cliente_destacado, 'w') as file:
        json.dump(cliente_info, file, indent=4)

print("Archivos generados:")
print(f"- {archivo_errores}")
print(f"- {archivo_pendientes}")
print(f"- {archivo_cliente_destacado}")
