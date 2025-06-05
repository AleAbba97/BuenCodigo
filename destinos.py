ultimo_id = 0
destinos = {}

def agregar_destino():
    global ultimo_id
    pais = input("Agregue el país al cual quiere ir: ").strip()
    ciudad = input("Agregue la ciudad a la cual quiere ir: ").strip()
    
    try:
        costo_base = int(input("Agregue el precio de su viaje: "))
    except ValueError:
        print("❌ El costo debe ser un número entero.")
        return

    if not pais or not ciudad:
        print("❌ Todos los campos son obligatorios.")
        return

    ultimo_id += 1
    destinos[ultimo_id] = {
        "Pais": pais,
        "Ciudad": ciudad,
        "Costo Base": costo_base
    }
    print(f"✅ Destino agregado con ID {ultimo_id}")

def modificar_destino():
    print("--- Modificar Destino ---")
    try:
        n_id = int(input("Ingrese el ID del destino a modificar: "))
    except ValueError:
        print("❌ El ID debe ser un número.")
        return

    if n_id in destinos:
        destino = destinos[n_id]
        print(f"Destino actual: País: {destino['Pais']} | Ciudad: {destino['Ciudad']} | Costo Base: {destino['Costo Base']}")

        nuevo_pais = input("Nuevo País (dejar vacío para mantener): ").strip()
        nueva_ciudad = input("Nueva Ciudad (dejar vacío para mantener): ").strip()
        nuevo_costo_input = input("Nuevo costo del viaje (dejar vacío para mantener): ").strip()

        if nuevo_pais:
            destino['Pais'] = nuevo_pais
        if nueva_ciudad:
            destino['Ciudad'] = nueva_ciudad
        if nuevo_costo_input:
            try:
                nuevo_costo = int(nuevo_costo_input)
                destino['Costo Base'] = nuevo_costo
            except ValueError:
                print("❌ El costo debe ser un número. No se modificó el valor.")

        print("✅ Destino modificado con éxito.")
    else: 
        print("❌ No se encontró el destino.")

def eliminar_destino():
    print("=== Eliminar Destino ===")
    try:
        n_id = int(input("Ingrese el ID del destino a eliminar: "))
    except ValueError:
        print("❌ El ID debe ser un número.")
        return

    if n_id in destinos:
        confirmacion = input(f"¿Está seguro de eliminar el destino {destinos[n_id]['Ciudad']}, {destinos[n_id]['Pais']} (Costo: {destinos[n_id]['Costo Base']})? (s/n): ").lower()
        if confirmacion == 's':
            del destinos[n_id]
            print("✅ Destino eliminado.")
        else:
            print("❎ Operación cancelada.")
    else:
        print("❌ No se encontró un destino con ese ID.")

def ver_destinos():
    print("=== Lista de Destinos ===")
    if not destinos:
        print("No hay destinos registrados.")
    else:
        for n_id, datos in sorted(destinos.items()):
            pais = datos.get('Pais', '[Sin País]')
            ciudad = datos.get('Ciudad', '[Sin Ciudad]')
            costo_base = datos.get('Costo Base', '[Sin Costo]')
            print(f"ID: {n_id} | País: {pais} | Ciudad: {ciudad} | Costo Base: {costo_base}")
