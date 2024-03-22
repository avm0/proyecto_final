# **Antes de ejecutar el código necesitamos tener en cuenta ver el menú de sabores primero** #
# ** Proyecto Final ** #
# ** Ángel Vega ** #

# Inicializamos los precios de los productos
precios_helados = {
    "vainilla": 600,
    "chocolate": 700,
    "caramelo": 750,
    "fresa": 800
}

precios_batidos = {
    1: 1200,
    2: 1300,
    3: 1400
}

# Inicializamos variables para el reporte final del día
ventas_totales = 0  # Variable para almacenar el total de ventas del día
total_helados_vendidos = 0  # Variable para almacenar el total de helados vendidos en el día
total_batidos_vendidos = 0  # Variable para almacenar el total de batidos vendidos en el día

# Bucle principal del programa
while True:
    # Mostramos el menú al usuario
    print("\n¡Bienvenido a Heladería POPS®!")
    print("********* Menú *********")
    print("1. Ver sabores de helados")
    print("2. Registrar pedido")
    print("3. Ver reporte del día")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")  # Solicitar al usuario que seleccione una opción del menú

    # Opción 1: Mostrar los sabores de helados disponibles
    if opcion == "1":
        print("\nSabores disponibles de helados:")
        for sabor in precios_helados.keys():
            print(f"- {sabor.capitalize()}")  # Mostrar los sabores de helados disponibles, capitalizando la primera letra

    # Opción 2: Registrar un nuevo pedido
    elif opcion == "2":
        print("\nPedido del cliente")
        apellido = input("Apellido del cliente: ")
        tiene_tarjeta_pops = input("Tiene tarjeta PuraVidaPops (sí/no): ").lower() == "sí"

        # Inicializamos variables para el cliente actual
        total_cliente = 0

        # Solicitar información sobre helados
        num_helados = int(input("Cantidad de helados: "))
        for j in range(num_helados):
            sabor_helado = input(f"Sabor del helado {j+1}: ").lower()
            while sabor_helado not in precios_helados:
                print("¡Sabor de helado no válido! Por favor, seleccione un sabor de la lista.")
                sabor_helado = input(f"Sabor del helado {j+1}: ").lower()  # Solicitar el sabor del helado y asegurarse de que sea válido
            precio_helado = precios_helados[sabor_helado]  # Obtener el precio del helado seleccionado
            total_cliente += precio_helado  # Sumar el precio del helado al total del cliente
            total_helados_vendidos += 1  # Incrementar el contador de helados vendidos

        # Solicitar información sobre batidos
        num_batidos = int(input("Cantidad de batidos: "))
        for k in range(num_batidos):
            num_frutas = int(input(f"Número de frutas del batido {k+1}: "))
            precio_batido = precios_batidos.get(num_frutas, 0)  # Obtener el precio del batido basado en el número de frutas
            total_cliente += precio_batido  # Sumar el precio del batido al total del cliente
            total_batidos_vendidos += 1  # Incrementar el contador de batidos vendidos

        # Calcular el descuento
        descuento = 0
        if tiene_tarjeta_pops:
            descuento += total_cliente * 0.15  # Aplicar descuento del 15% si el cliente tiene tarjeta PuraVidaPops
        if apellido.lower() == "alvarado":
            descuento += total_cliente * 0.10  # Aplicar descuento adicional del 10% si el apellido del cliente es "Alvarado"

        # Calcular el total a pagar
        total_pagar = total_cliente - descuento  # Calcular el total a pagar restando el descuento del total del cliente
        ventas_totales += total_pagar  # Sumar el total a pagar al total de ventas del día

        # Mostrar la cuenta total del cliente
        print("La cuenta total del cliente es:")
        print(f"Total sin descuento: {total_cliente} colones")
        print(f"Descuento total: {descuento} colones")
        print(f"Total a pagar: {total_pagar} colones")

    # Opción 3: Ver el reporte final del día
    elif opcion == "3":
        # Mostrar el reporte final del día
        print("\nReporte final del día para Heladería POPS®")
        print("----------------------")
        print(f"Total de ventas del día: {ventas_totales} colones")
        print(f"Total de helados vendidos: {total_helados_vendidos}")
        print(f"Total de batidos vendidos: {total_batidos_vendidos}")

    # Opción 4: Salir del programa
    elif opcion == "4":
        print("¡Gracias por visitar Heladería POPS®!")
        break  # Salir del bucle y terminar el programa

    # Si la opción no es válida, mostrar un mensaje de error
    else:
        print("Opción inválida. Por favor")