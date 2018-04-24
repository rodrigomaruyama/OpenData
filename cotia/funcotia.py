import pandas as pd

funcotia = pd.read_csv('funcionariosCotia.csv', sep='|', encoding='iso-8859-1')

print(funcotia.groupby('Secretaria'))
