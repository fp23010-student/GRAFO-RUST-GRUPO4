import matplotlib.pyplot as plt

initial_value = 100000
useful_life = 10
depreciation_per_year = initial_value / useful_life

years = list(range(0, useful_life + 1))
values = [initial_value - (depreciation_per_year * year) for year in years]

plt.figure(figsize=(10, 6))
plt.plot(years, values, marker='o', label='Valor del activo')

plt.title('Depreciación (Método Línea Recta)')
plt.xlabel('Año')
plt.ylabel('Valor ($)')
plt.xticks(years)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()