import pandas as pd


# lendo o csv
df_oscar = pd.read_csv('the_oscar_award.csv')

# filtrando o csv
df_oscar_filtrado = [
   df_oscar['film'].notna() &
   df_oscar['year_film'].notna() &
   (df_oscar['category'] == 'BEST PICTURE') &
   df_oscar['year_ceremony'].notna() &
   (df_oscar['year_film'] >= 2004) &
   (df_oscar['year_film'] <= 2024)
]

df_oscar_filtrado = df_oscar_filtrado['film', 'year_film', 'category', 'year_ceremony', 'winner']

# salvando o csv filtrado em um novo arquivo
df_oscar_filtrado.to_csv('the_oscar.csv', None)

# editei o arquivo csv manualmente adicionando a coluna boxoffice com ajuda da ia deepseek
