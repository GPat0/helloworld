import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header(' Mis Datos Personales')

# Ejemplo 1: texto con estilo
st.write('Hola, *mundo de los videojuegos!* ')

# Ejemplo 2: número
st.write(2025)

# Ejemplo 3: DataFrame personalizado (no del reto)
df = pd.DataFrame({
    'Juego': ['Halo', 'Zelda', 'Elden Ring', 'God of War'],
    'Horas jugadas': [120, 95, 140, 80]
})
st.write(df)

# Ejemplo 4: texto + DataFrame combinado
st.write('Estos son algunos de mis juegos favoritos:', df, '¡Y los volvería a jugar!')

# Ejemplo 5: Gráfica con Altair (datos aleatorios)
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['x', 'y', 'intensidad']
)
chart = alt.Chart(df2).mark_circle().encode(
    x='x', y='y', size='intensidad', color='intensidad', tooltip=['x', 'y', 'intensidad']
)
st.write(chart)
