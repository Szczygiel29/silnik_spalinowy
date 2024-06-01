import pandas as pd
import matplotlib.pyplot as plt

# Dane wejściowe dla silników spalinowych
data = {
    'Silnik': ['Silnik 1', 'Silnik 2', 'Silnik 3'],
    'Moc (kW)': [100, 150, 200],
    'Zużycie paliwa (m3/h)': [10, 15, 20],
    'Skład biogazu CH4 (%)': [63.08, 58.60, 65.99],
    'Skład biogazu CO2 (%)': [36.05, 33.11, 33.62],
    'Emisje CO2 (g/kWh)': [250, 230, 240],
    'Emisje NOx (g/kWh)': [5, 4.5, 5.2],
    'Emisje PM (g/kWh)': [0.3, 0.25, 0.28]
}

# Tworzenie DataFrame z danymi
df = pd.DataFrame(data)

# Obliczanie wydajności silnika
df['Wydajność paliwa (kWh/m3)'] = df['Moc (kW)'] / df['Zużycie paliwa (m3/h)']

# Przykładowe wyliczenie emisji na godzinę pracy silnika
df['Emisje CO2 (kg/h)'] = df['Emisje CO2 (g/kWh)'] * df['Moc (kW)'] / 1000
df['Emisje NOx (kg/h)'] = df['Emisje NOx (g/kWh)'] * df['Moc (kW)'] / 1000
df['Emisje PM (kg/h)'] = df['Emisje PM (g/kWh)'] * df['Moc (kW)'] / 1000

# Obliczanie całkowitych emisji dla danego okresu pracy (np. 1000 godzin)
okres_pracy = 1000  # w godzinach
df['Całkowite emisje CO2 (kg)'] = df['Emisje CO2 (kg/h)'] * okres_pracy
df['Całkowite emisje NOx (kg)'] = df['Emisje NOx (kg/h)'] * okres_pracy
df['Całkowite emisje PM (kg)'] = df['Emisje PM (kg/h)'] * okres_pracy

# Wykresy
plt.figure(figsize=(14, 10))

# Wydajność paliwa
plt.subplot(2, 2, 1)
plt.bar(df['Silnik'], df['Wydajność paliwa (kWh/m3)'], color='blue')
plt.title('Wydajność paliwa')
plt.xlabel('Silnik')
plt.ylabel('Wydajność paliwa (kWh/m3)')

# Emisje CO2
plt.subplot(2, 2, 2)
plt.bar(df['Silnik'], df['Całkowite emisje CO2 (kg)'], color='red')
plt.title('Całkowite emisje CO2')
plt.xlabel('Silnik')
plt.ylabel('Całkowite emisje CO2 (kg)')

# Emisje NOx
plt.subplot(2, 2, 3)
plt.bar(df['Silnik'], df['Całkowite emisje NOx (kg)'], color='green')
plt.title('Całkowite emisje NOx')
plt.xlabel('Silnik')
plt.ylabel('Całkowite emisje NOx (kg)')

# Emisje PM
plt.subplot(2, 2, 4)
plt.bar(df['Silnik'], df['Całkowite emisje PM (kg)'], color='purple')
plt.title('Całkowite emisje PM')
plt.xlabel('Silnik')
plt.ylabel('Całkowite emisje PM (kg)')

plt.tight_layout()
plt.show()
