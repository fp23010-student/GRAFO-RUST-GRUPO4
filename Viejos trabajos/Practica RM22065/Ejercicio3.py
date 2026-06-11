import matplotlib.pyplot as plt
import pandas as pd

journal = [
    {"date": "2024-01-01", "account": "Sales", "amount": 5000, "type": "Credit"},
    {"date": "2024-01-02", "account": "Cash", "amount": 5000, "type": "Debit"},
    {"date": "2024-01-03", "account": "Utilities Expense", "amount": 1000, "type": "Debit"},
    {"date": "2024-01-04", "account": "Accounts Payable", "amount": 1000, "type": "Credit"}
]

df = pd.DataFrame(journal)

df.loc[df['type'] == 'Debit', 'amount'] *= -1

pivot_df = df.pivot(index="date", columns="type", values="amount").fillna(0)

pivot_df.plot(kind='bar', figsize=(10, 6))

plt.title('Débitos vs Créditos')
plt.xlabel('Fecha')
plt.ylabel('Cantidad ($)')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.tight_layout()
plt.show()