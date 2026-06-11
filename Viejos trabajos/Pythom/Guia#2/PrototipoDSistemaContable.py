
cuentas = {
"Banco": {"debe": 36540, "haber": 0},
"Clientes": {"debe": 63200, "haber": 0},
"Estimacion incobrables": {"debe": 0, "haber": 5100},
"Deudores diversos": {"debe": 6200, "haber": 0},
"Inventario": {"debe": 127500, "haber": 0},
"Mobiliario": {"debe": 350000, "haber": 0},
"Dep_mobiliario": {"debe": 0, "haber": 35000},
"Equipo_reparto": {"debe": 115000, "haber": 0},
"Dep_reparto": {"debe": 0, "haber": 28750},
"Equipo_computo": {"debe": 60000, "haber": 0},
"Dep_computo": {"debe": 0, "haber": 18000},
"Proveedores": {"debe": 0, "haber": 55965},
"Documentos_pagar": {"debe": 0, "haber": 65000},
"Impuestos_pagar": {"debe": 0, "haber": 11000},
"Capital": {"debe": 0, "haber": 500000},
"Ventas": {"debe": 0, "haber": 1125000},
"Costo_ventas": {"debe": 540000, "haber": 0},
"Gastos_admin": {"debe": 238750, "haber": 0},
"Gastos_venta": {"debe": 283500, "haber": 0},
"Otros_gastos": {"debe": 12125, "haber": 0},
"Gasto_impuesto": {"debe": 11000, "haber": 0}
}

def movimiento(cuenta, debe=0, haber=0):
    cuentas[cuenta]["debe"] += debe
    cuentas[cuenta]["haber"] += haber


# -----------------------------
# AJUSTE 1
# estimacion incobrables 10%
# -----------------------------

estimacion_total = 63200 * 0.10
actual = cuentas["Estimacion incobrables"]["haber"]

ajuste = estimacion_total - actual

movimiento("Gastos_admin", debe=ajuste)
movimiento("Estimacion incobrables", haber=ajuste)


# -----------------------------
# AJUSTE 2
# computadora mal registrada
# -----------------------------

movimiento("Equipo_computo", debe=26500)
movimiento("Gastos_admin", haber=26500)


# -----------------------------
# AJUSTE 3
# error compra mercaderia
# -----------------------------

movimiento("Proveedores", debe=9000)
movimiento("Costo_ventas", haber=9000)


# -----------------------------
# BALANZA AJUSTADA
# -----------------------------

print("BALANZA DE COMPROBACION AJUSTADA\n")

total_debe = 0
total_haber = 0

for cuenta, valores in cuentas.items():
    debe = valores["debe"]
    haber = valores["haber"]

    total_debe += debe
    total_haber += haber

    print(cuenta, "Debe:", debe, "Haber:", haber)

print("\nTOTAL DEBE:", total_debe)
print("TOTAL HABER:", total_haber)


# -----------------------------
# ESTADO DE RESULTADOS
# -----------------------------

ventas = cuentas["Ventas"]["haber"]

costo = cuentas["Costo_ventas"]["debe"] - cuentas["Costo_ventas"]["haber"]

g_admin = cuentas["Gastos_admin"]["debe"] - cuentas["Gastos_admin"]["haber"]
g_venta = cuentas["Gastos_venta"]["debe"]
otros = cuentas["Otros_gastos"]["debe"]

utilidad_bruta = ventas - costo

total_gastos = g_admin + g_venta + otros

utilidad_antes_impuesto = utilidad_bruta - total_gastos

impuesto = cuentas["Gasto_impuesto"]["debe"]

utilidad_neta = utilidad_antes_impuesto - impuesto


print("\nESTADO DE RESULTADOS\n")

print("Ventas:", ventas)
print("Costo de ventas:", costo)

print("Utilidad bruta:", utilidad_bruta)

print("Gastos administracion:", g_admin)
print("Gastos venta:", g_venta)
print("Otros gastos:", otros)

print("Total gastos:", total_gastos)

print("Utilidad antes de impuesto:", utilidad_antes_impuesto)

print("Impuesto:", impuesto)

print("UTILIDAD NETA:", utilidad_neta)