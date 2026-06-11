import matplotlib.pyplot as plt
import numpy as np

# Datos
years = ["Año 1", "Año 2", "Año 3", "Año 4", "Año 5"]
dta = [10, 15, 20, 25, 30]
dtl = [5, 10, 15, 10, 5]

net_deferred_tax = np.array(dta) - np.array(dtl)

x = np.arange(len(years))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(x - width/2, dta, width, label='Activos por Impuestos Diferidos')
ax.bar(x + width/2, dtl, width, label='Pasivos por Impuestos Diferidos')

for i, value in enumerate(net_deferred_tax):
    ax.text(i, max(dta[i], dtl[i]) + 1, f"Neto: {value}", ha='center')

ax.set_xlabel('Año')
ax.set_ylabel('Importe (millones)')
ax.set_title('Activos y Pasivos por Impuestos Diferidos')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()

plt.tight_layout()
plt.show()