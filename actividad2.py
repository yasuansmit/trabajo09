pedidos = {}
def registrar_pedido(nombre_cliente, direccion, contacto, sexo, descripcion_lugar, nombre_producto, referencia_producto, cantidad):
    
    if nombre_cliente in pedidos:
    
        pedidos[nombre_cliente].append({
            'direccion': direccion,
            'contacto': contacto,
            'sexo': sexo,
            'descripcion_lugar': descripcion_lugar,
            'nombre_producto': nombre_producto,
            'referencia_producto': referencia_producto,
            'cantidad': cantidad
        })
    else:
        
        pedidos[nombre_cliente] = [{
            'direccion': direccion,
            'contacto': contacto,
            'sexo': sexo,
            'descripcion_lugar': descripcion_lugar,
            'nombre_producto': nombre_producto,
            'referencia_producto': referencia_producto,
            'cantidad': cantidad
        }]
    
    print("Pedido registrado con éxito.")

def mostrar_pedidos():
   
    if pedidos:
        print("Pedidos realizados:")
        for nombre_cliente, historial_pedidos in pedidos.items():
            print(f"Cliente: {nombre_cliente}")
            for pedido in historial_pedidos:
                print("Datos del pedido:")
                for clave, valor in pedido.items():
                    print(f"{clave}: {valor}")
                print("-------------------------")
    else:
        print("No hay pedidos registrados.")
