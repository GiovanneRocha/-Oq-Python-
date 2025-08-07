import pandas as pd
import matplotlib.pyplot as plt

# Etapa 1: Criar um arquivo CSV com dados de vendas
dados_vendas = {
    'Data': ['2023-01-15', '2023-01-20', '2023-02-10', '2023-02-25', '2023-03-05', '2023-03-18'],
    'Valor': [1500, 2300, 1800, 2200, 2500, 2700]
}

df_vendas = pd.DataFrame(dados_vendas)
df_vendas.to_csv('vendas.csv', index=False)

# Etapa 2: Ler os dados do arquivo CSV
df = pd.read_csv('vendas.csv')

# Etapa 3: Converter a coluna de datas para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Etapa 4: Extrair o mês e calcular o total de vendas por mês
df['Mes'] = df['Data'].dt.strftime('%Y-%m')
vendas_mensais = df.groupby('Mes')['Valor'].sum()

# Etapa 5: Gerar gráfico de barras
plt.figure(figsize=(8, 5))
vendas_mensais.plot(kind='bar', color='skyblue')
plt.title('Faturamento Mensal')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_faturamento_mensal.png')

# Exibir mensagem de sucesso
print("Arquivo CSV criado, total de vendas por mês calculado e gráfico gerado com sucesso.")

