ultimo_id = 0
destinos = {}

def agregar_destino():
    global ultimo_id
    pais = input("Agregue el pais al cual quiere ir: ")
    ciudad = input ("Agregue la ciudad a la cual quiere ir: ")
    costo_base = int(input ("Agregue el precio de su viaje: "))
    ultimo_id += 1
    destinos[ultimo_id] = {
        "Pais" : pais,
        "Ciudad" : ciudad,
        "Costo Base": costo_base
    }
    print (f"Destino agregado con ID {ultimo_id}")

def modificar_destino():
    print ("---Modificar Destino---")
    n_id = int(input("Agregue el ID correspondiente al destino a modificar: " ))
    if n_id in destinos:
        destino = destinos[n_id]
        print(f"Destino actual: País: {destino['Pais']} | Ciudad: {destino['Ciudad']} | Costo Base: {destino['Costo Base']}")
        
        nuevo_pais = input("Nuevo Pais (dejar vacío para mantener): ").strip()
        nueva_ciudad = input ("Nueva ciudad (dejar vacío para mantener): ").strip()
        nuevo_costo = int(input("Nuevo costo del viaje(dejar vacio para mantener):"))

        if nuevo_pais:
            destino['Pais'] = nuevo_pais
        if nueva_ciudad:
            destino['Ciudad'] = nueva_ciudad
        if nuevo_costo:
            destino['Costo Base'] = nuevo_costo
        print("✅ Destino modificado con éxito.")
    else: 
        print ("No se encontro el destino")

def eliminar_destino():
    print("=== Eliminar Destino ===")
    n_id = int(input("ingrese el ID del destino a eliminar: "))
    if n_id in destinos:
        confirmacion = input(f"¿Está seguro de eliminar a {destinos[n_id]['Ciudad']} {destinos[n_id]['Pais']} {destinos[n_id]['Costo Base']}? (s/n): ").lower()
        if confirmacion == 's':
            del destinos[n_id]
            print("✅ Destino eliminado.")
        else:
            print("❎ Operación cancelada.")
    else:
        print("❌ No se encontró un destino ese ID")

def ver_destinos():
    print("=== Lista de Destino ===")
    if not destinos:
        print("No hay destinos registrados.")
    else:
        for n_id, datos in destinos.items():
            pais = datos.get('Pais', '[Sin Pais]')
            ciudad = datos.get('Ciudad', '[Sin Ciudad]')
            costo_base = datos.get('Costo Base', '[Sin Costo Base]')
            print(f"ID: {n_id} | Pais: {pais} | Ciudad: {ciudad} | Costo Base: {costo_base}")