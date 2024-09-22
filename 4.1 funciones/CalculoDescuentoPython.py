""""Crea una función llamada calcular_descuento que tome dos parámetros:
el monto total de la compra y un valor predeterminado para el porcentaje de descuento
(por ejemplo, 10% por defecto).
La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
La función debe devolver el monto del descuento calculado.

Llamada a la Función:

Llama a la función calcular_descuento al menos dos veces desde el programa principal.
En una llamada, proporciona el monto total de la compra y,
en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento."""

# Funcion para calcular el descuento

def calcular_descuento(valor_total,porcentaje_descuento=10):
    descuento = valor_total * porcentaje_descuento /100
    return descuento

monto_total = 2000
descuento = calcular_descuento(monto_total)
print(f"Monto Total de {monto_total}: ")
print(f"descuento : {descuento}")

print("*************************")
monto_total2 = 2000
descuento = 45
descuento2 = calcular_descuento(monto_total2,descuento)
print(f"Monto Total de {monto_total2}: ")
print(f"descuento : {descuento2}")

# Función para calcular el IVA
def calcular_iva(valor, porcentaje_iva=15):
    iva = valor * porcentaje_iva / 100
    return iva

# Función para generar la factura
def generar_factura(monto_total, porcentaje_descuento=10):
    descuento = calcular_descuento(monto_total, porcentaje_descuento)
    valor_con_descuento = monto_total - descuento
    iva = calcular_iva(valor_con_descuento)
    total_final = valor_con_descuento + iva

    print("********** FACTURA **********")
    print(f"Monto Total: ${monto_total:.2f}")
    print(f"Descuento ({porcentaje_descuento}%): -${descuento:.2f}")
    print(f"Subtotal (después del descuento): ${valor_con_descuento:.2f}")
    print(f"IVA (15%): +${iva:.2f}")
    print(f"Total a Pagar: ${total_final:.2f}")
    print("******************************")

# Llamadas a la función
monto_total_1 = 2000
generar_factura(monto_total_1)

