import pandas as pd
import matplotlib.pyplot as plt

# 1. Carrega os dados do CSV
tabela = pd.read_csv('despesas.csv')

# 2. Cria o gráfico de barras
plt.figure(figsize=(8, 5))  # Define o tamanho da figura (largura x altura)
plt.bar(tabela['Categoria'], tabela['Valor'], color='skyblue', edgecolor='black')

# 3. Personaliza o gráfico com títulos e rótulos
plt.title('Minhas Despesas do Mês', fontsize=14, fontweight='bold')
plt.xlabel('Categorias', fontsize=12)
plt.ylabel('Valor (R$)', fontsize=12)

# 4. Salva o gráfico como imagem no seu computador (ótimo para o GitHub!)
plt.savefig('grafico_despesas.png', dpi=300, bbox_inches='tight')

# 5. Mostra o gráfico na tela
plt.show()
