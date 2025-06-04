from datetime import datetime
ventas = []

def crear_venta(clientes, destinos):
    print("=== Crear Venta ===")
    id_venta = len(ventas) + 1

    if not clientes:
        print("❌ No hay clientes registrados.")
        return
    if not destinos:
        print("❌ No hay destinos registrados.")
        return

    print("Clientes disponibles:")
    for id_cliente, datos in clientes.items():
        print(f"ID: {id_cliente} | CUIT: {datos['CUIT']} | Razón Social: {datos['Razon Social']}")

    id_cliente = int(input("Ingrese el ID del cliente: "))
    if id_cliente not in clientes:
        print("❌ Cliente no encontrado.")
        return
    cliente = clientes[id_cliente]

    print("Destinos disponibles:")
    for id_destino, datos in destinos.items():
        print(f"ID: {id_destino} | País: {datos['Pais']} | Ciudad: {datos['Ciudad']} | Costo Base: {datos['Costo Base']}")

    id_destino = int(input("Ingrese el ID del destino: "))
    if id_destino not in destinos:
        print("❌ Destino no encontrado.")
    destino = destinos[id_destino]
    
    fecha_venta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nueva_venta = {
        'ID': id_venta,
        'Cliente_ID': id_cliente,
        'CUIT': cliente['CUIT'],
        'Razon Social': cliente['Razon Social'],
        'Destino': f"{destino['Ciudad']}, {destino['Pais']}, $ {destino['Costo Base']}",
        'Fecha': fecha_venta,
        'Estado': 'Activa'
    }

    ventas.append(nueva_venta)
    print("✅ Venta registrada con éxito.")

def consultar_ventas():
    print("=== Ventas Registradas ===")
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            estado = venta['Estado']
            info_anulacion = f" | Fecha de Anulación: {venta['Fecha_Anulacion']}" if estado == 'Anulada' else ""
            print(
                f"ID: {venta['ID']} | Cliente: {venta['Razon Social']} "
                f"(ID: {venta['Cliente_ID']}, CUIT: {venta['CUIT']}) | "
                f"Destino: {venta['Destino']} | Fecha: {venta['Fecha']} | Estado: {estado}{info_anulacion}"
            )
def boton_arrepentimiento():
    print("=== Botón de Arrepentimiento ===")
    print("Usted posee la posibilidad de reembolsar su viaje. Tiene 5 minutos para realizarlo (solo se puede anular).")

    if not ventas:
        print("❌ No hay ventas registradas.")
        return

    ventas_activas = [v for v in ventas if v['Estado'] == 'Activa']
    if not ventas_activas:
        print("⚠️ No hay ventas activas para anular.")
        return

    for venta in ventas_activas:
        print(f"ID: {venta['ID']} | Cliente: {venta['Razon Social']} (ID Cliente: {venta['Cliente_ID']}) | Destino: {venta['Destino']}")

    id_a_anular = int(input("Ingrese el ID de la venta que desea anular (o 0 para cancelar): "))
    if id_a_anular == 0:
        print("❎ Operación cancelada.")
        return
    for venta in ventas_activas:
        if venta['ID'] == id_a_anular:
            confirmacion = input(f"¿Está seguro de anular la venta de {venta['Razon Social']} al destino {venta['Destino']}? (s/n): ").lower()
            if confirmacion == 's':
                venta['Estado'] = 'Anulada'
                venta['Fecha_Anulacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"✅ Venta anulada con éxito en {venta['Fecha_Anulacion']}.")
            else:
                print("❎ Anulación cancelada.")
            return
    print("❌ No se encontró una venta activa con ese ID.")