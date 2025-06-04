clientes = {}
ultimo_id = 0

def generar_id():
    global ultimo_id
    ultimo_id += 1
    return ultimo_id

def agregar_cliente():
    razon_social = input("Ingrese Razón Social: ").strip()
    cuit = input("Ingrese CUIT: ").strip()
    email = input("Ingrese Email: ").strip()

    if not razon_social or not cuit or not email:
        print("❌ Todos los campos son obligatorios.")
        return

    # Verificamos que no haya otro cliente con ese CUIT
    for cliente in clientes.values():
        if cliente["CUIT"] == cuit:
            print("❌ Ya existe un cliente con ese CUIT.")
            return

    nuevo_id = generar_id()
    clientes[nuevo_id] = {
        "Razon Social": razon_social,
        "CUIT": cuit,
        "Email": email,
    }
    print(f"✅ Cliente agregado con ID: {nuevo_id}")

def modificar_cliente():
    print("=== Modificar cliente ===")
    id_cliente = int(input("Ingrese el ID del cliente a modificar: "))
    if id_cliente in clientes:
        cliente = clientes[id_cliente]
        print(f"Cliente actual: {cliente}")

        nueva_razon = input("Nueva Razón Social (dejar vacío para mantener): ").strip()
        nuevo_email = input("Nuevo Email (dejar vacío para mantener): ").strip()

        if nueva_razon:
            cliente["Razon Social"] = nueva_razon
        if nuevo_email:
            cliente["Email"] = nuevo_email

        print("✅ Cliente modificado con éxito.")
    else:
        print("❌ No se encontró un cliente con ese ID.")

def eliminar_cliente():
    print("=== Eliminar cliente ===")
    id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
    if id_cliente in clientes:
        confirmacion = input(f"¿Está seguro de eliminar a {clientes[id_cliente]['Razon Social']}? (s/n): ").lower()
        if confirmacion == 's':
            del clientes[id_cliente]
            print("✅ Cliente eliminado.")
        else:
            print("❎ Operación cancelada.")
    else:
        print("❌ No se encontró un cliente con ese ID.")

def ver_clientes():
    print("=== Lista de Clientes ===")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for id_cliente, datos in sorted(clientes.items()):
            print(f"ID: {id_cliente} | CUIT: {datos['CUIT']} | Razón Social: {datos['Razon Social']} | Email: {datos['Email']}")
