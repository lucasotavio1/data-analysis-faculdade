import pandas as pd
import matplotlib.pyplot as plt


# lendo o arquivo csv filtrado
df_oscar = pd.read_csv('the_oscar.csv')

# exibindo todas as linhas do data frame
pd.set_option('display.max_rows', None)
print(df_oscar)

# separando os vencedores dos indicaods
df_vencedores = df_oscar[df_oscar['winner'] == True]
df_indicados = df_oscar[df_oscar['winner'] == False]

# selecionando os top 20 vencdeores e indicados com maior bilheteria
df_vencedores_top20 = df_vencedores.nlargest(20, 'boxoffice')
df_indicados_top20 = df_indicados.nlargest(20, 'boxoffice')

# calculando o skew (assimetria) da bilheteria para vencedores e indicados
skew_vencedores = df_vencedores['boxoffice'].skew()
skew_indicados = df_indicados['boxoffice'].skew()

# calculando a correlação entre vencer o Oscar e bilheteria
correlacao = df_oscar[['winner', 'boxoffice']].corr()

# calculando a média da bilheteria de vencedores e indicados
media_vencedores = df_vencedores['boxoffice'].mean()
media_indicados = df_indicados['boxoffice'].mean()

# agrupando a bilheteria média por ano de vencedores e indicados
bilheteria_por_ano_vencedores = df_vencedores.groupby('year_film')['boxoffice'].mean()
bilheteria_por_ano_indicados = df_indicados.groupby('year_film')['boxoffice'].mean()

# criando um gráfico de barras para os top 20 filmes vencedores com maior bilheteria
plt.figure(figsize=(12, 6))
plt.bar(df_vencedores_top20['film'], df_vencedores_top20['boxoffice'], color='gold')
plt.title('Top 20 filmes vencedores de Oscar com maior bilheteria')
plt.xlabel('Filmes')
plt.ylabel('Bilheteria')
plt.xticks(rotation=90)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# criando um gráfico de barras para os top 20 filmes indicados com maior bilheteria
plt.figure(figsize=(12, 6))
plt.bar(df_indicados_top20['film'], df_indicados_top20['boxoffice'], color='limegreen')
plt.title('Top 20 filmes indicados ao Oscar com maior bilheteria')
plt.xlabel('Filmes')
plt.ylabel('Bilheteria')
plt.xticks(rotation=90)
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()

# criando um gráfico de barras para comparar a média da bilheteria entre vencedores e indicados
plt.figure(figsize=(12, 6))
cores = ['gold', 'limegreen']
plt.bar(
    ['Vencedores', 'Indicados'],
    [media_vencedores, media_indicados],
    label=['Vencedores', 'Indicados'],
    color=cores
)
plt.title('Média da Bilheteira (Vencedores x Indicados)')
plt.ylabel('Bilheteira Média')
plt.ticklabel_format(style='plain', axis='y')
plt.legend(loc='best')
plt.show()

# criando um gráfico de linha para mostrar a evolução da bilheteria média ao longo dos anos
plt.figure(figsize=(12, 6))
plt.plot(
    bilheteria_por_ano_vencedores.index,
    bilheteria_por_ano_vencedores,
    label='Vencedores',
    color='gold',
    marker='o'
)
plt.plot(
    bilheteria_por_ano_indicados.index,
    bilheteria_por_ano_indicados,
    label='Indicados',
    color='limegreen',
    marker='o'
)
plt.title('Evolução das bilheteria média ao longo dos anos (Vencedores x Indicados)')
plt.xlabel('Ano')
plt.ylabel('Bilheteria Média')
plt.ticklabel_format(style='plain', axis='y')
plt.grid(linestyle='--', alpha=0.7)
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# criando um gráfico de pizza para mostrar a proporção de vencedores e indicados
plt.figure(figsize=(12, 6))
contador = df_oscar['winner'].value_counts()
cores = ['lightcoral', 'lightgreen']
plt.pie(
    contador,
    labels=['Indicados', 'Vencedores'],
    autopct='%1.1f%%',
    colors=cores
)
plt.title('Proporção de vencedores e indicados')
plt.legend(loc='best')
plt.show()

# exibindo considerações finais com valores dos cálculos
print('Considerações finais')
print(f'Skew da bilheteria dos vencedores: {skew_vencedores:.2f}')
print(f'Skew da bilheteria dos indicados: {skew_indicados:.2f}')
print(f'Correlação entre vencer e bilheteria: \n{correlacao}')