despachos = {}

def registro_salida(placa, descripcion, nombre_conductor, contacto_conductor, ruta, descripcion_carga):
    numero_despacho = len(despachos) 
    despachos[numero_despacho] = {
        'placa': placa,
        'descripcion': descripcion,
        'nombre_conductor': nombre_conductor,
        'contacto_conductor': contacto_conductor,
        'ruta': ruta,
        'descripcion_carga': descripcion_carga
    }
    print(f"Despacho {numero_despacho} registrado con éxito.")

def mostrar_despachos():
    if despachos:
        print("Registro de Despachos:")
        for numero, despacho in despachos.items():
            print(f"Despacho {numero}:")
            for clave, valor in despacho.items():
                print(f"{clave}: {valor}")
            print("-------------------------")
    else:
        print("No hay despachos registrados.")



registro_salida(
    placa="ABC123",
    descripcion="Camión de carga",
    nombre_conductor="Juan Pérez",
    contacto_conductor="123456789",
    ruta="Ciudad A - Ciudad B",
    descripcion_carga="Productos diversos"
)

mostrar_despachos()