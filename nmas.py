from belvo import Client
import os

# Inicializar cliente
client = Client(
    os.getenv('BELVO_SECRET_ID'),
    os.getenv('BELVO_SECRET_PASSWORD'),
    "https://api.belvo.com"  # o sandbox
)

# Crear link (conexión con banco)
link = client.Links.create(
    institution="banco_abc",
    username="usuario",
    password="contraseña",
    # ... otros parámetros
)

# Obtener cuentas y transacciones
accounts = client.Accounts.retrieve(link_id=link['id'])
transactions = client.Transactions.retrieve(
    link_id=link['id'],
    date_from="2025-01-01",
    date_to="2026-05-01"
)

# Enviar a sistema contable (ejemplo simplificado)
for tx in transactions:
    # Crear registro en tu ERP o base de datos
    registrar_transaccion_contable(
        fecha=tx['date'],
        monto=tx['amount'],
        descripcion=tx['description'],
        categoria=enriquecer_categoria(tx)  # ML de Belvo
    )