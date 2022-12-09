
precio_h = 3.49
precio_m = round((precio_h*0.4), 2)

def pan(fresco, reposado):

    precio_fresco = (fresco*precio_h)
    precio_reposado = (reposado*precio_m)
    total_costo = round((precio_fresco+precio_m), 2)

    return total_costo

cant_fresco = int(input("Por favor ingrese el número de panes frecos que hay: "))
cant_reposado = int(input("Por favor ingrese el número de panes que sobraron del día anterior: "))

costo_total = pan(cant_fresco, cant_reposado)

print("El precio habitual de un pan es de " + str(precio_h) + ". \n El precio del pan reposado es de " + str(precio_m) + ". \n Por tanto el costo total seria de " + str(costo_total) + ".")