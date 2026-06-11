import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Finance:
    def __init__(self, inputs):
        self.user_name = inputs.get('name', 'Usuario')
        self.data_root = inputs.get('data_root', 'logs.csv')
        self.balance = 0
        
        self.read_database()
        
        self.run_app()

    def read_database(self):
        """Lee el archivo CSV. Si no existe, crea un DataFrame vacío con las columnas correctas."""
        try:
            self.data = pd.read_csv(self.data_root)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=['Date', 'Amount', 'Category', 'Comment'])

    def calculate_balance(self):
        """Suma la columna 'Amount' para obtener el balance total."""
        if not self.data.empty:
            self.balance = self.data['Amount'].sum()
        else:
            self.balance = 0

    def show_balance(self):
        """Calcula y muestra el balance actual."""
        self.calculate_balance()
        print(f"\n--- Balance actual: ${self.balance} ---\n")

    def add_log(self):
        """Solicita los datos al usuario para agregar un nuevo registro."""
        day = input("Día (DD): ")
        month = input("Mes (MM): ")
        year = input("Año (YYYY): ")
        
        try:
            amount = float(input("Monto (ej. -200 para gasto, 1000 para ingreso): "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            return

        category = input("Categoría (ej. Comida, Ropa, Salario): ")
        comment = input("Comentario: ")

        date = f"{day}/{month}/{year}"
        new_log = [date, amount, category, comment]

        self.data.loc[len(self.data)] = new_log
        self.save_database()
        print("\n¡Registro agregado con éxito!\n")

    def save_database(self):
        """Guarda el DataFrame actualizado en el archivo CSV sin incluir el índice."""
        self.data.to_csv(self.data_root, index=False)

    def show_report(self):
        """Genera un gráfico con los gastos/ingresos y el balance acumulativo."""
        if self.data.empty:
            print("\nNo hay datos para graficar todavía.\n")
            return

        plt.figure(figsize=(10, 6))
        
        plt.plot(self.data['Amount'], marker='o', label='Monto individual')
        
        plt.plot(np.cumsum(self.data['Amount']), linestyle='--', label='Balance acumulativo')

        plt.title('Reporte Financiero')
        plt.ylabel('Dinero')
        plt.xlabel('Transacciones')
        plt.legend()
        plt.show()

    def run_app(self):
        """Mantiene la aplicación corriendo hasta que el usuario decida salir."""
        keep_running = True
        while keep_running:
            self.menu()
            keep_running = self.keep_on()
        print("\nGoodbye!")

    def menu(self):
        """Imprime las opciones disponibles."""
        print("\n" + "="*35)
        print(f"Welcome to your financial app, {self.user_name}!")
        print("="*35)
        print("1. Show Balance (Mostrar Balance)")
        print("2. New Log (Nuevo Registro)")
        print("3. Show Report (Mostrar Gráfico)")
        
        option = input("\nOption selected (1, 2 o 3): ")
        
        if option == '1':
            self.show_balance()
        elif option == '2':
            self.add_log()
        elif option == '3':
            self.show_report()
        else:
            print("Opción no válida. Intenta de nuevo.")

    def keep_on(self):
        """Pregunta si el usuario desea realizar otra acción."""
        ans = input("Perform another action? (yes/no): ").strip().lower()
        if ans == 'yes' or ans == 'y':
            return True
        else:
            return False

if __name__ == "__main__":
    app_inputs = {
        'name': 'Estudiante',
        'data_root': 'logs.csv'
    }
    
    app = Finance(app_inputs)