import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
@st.cache  # Esta línea ayuda a que Streamlit no recargue los datos cada vez que se haga una interacción
def load_data():
    data = pd.read_csv('/ruta/del/archivo.csv')
    return data

data = load_data()

# Título de la aplicación
st.title('Visualización de Datos de Películas')

# Mostrar las primeras filas del dataframe
st.header('Primeras filas del Dataset')
st.write(data.head())

# Selección del tipo de gráfico
chart_type = st.sidebar.selectbox('Selecciona el tipo de gráfico:', ['Histograma', 'Scatter Plot'])

# Configuración de los gráficos
if chart_type == 'Histograma':
    st.header('Histograma de Ratings')
    column = st.sidebar.selectbox('Selecciona la columna para el histograma:', ['Rating', 'Revenue (Millions)'])
    plt.figure(figsize=(10, 5))
    plt.title(f'Histograma de {column}')
    plt.hist(data[column].dropna(), bins=30, alpha=0.7, color='blue')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    st.pyplot(plt)
elif chart_type == 'Scatter Plot':
    st.header('Scatter Plot de Revenue vs Rating')
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=data['Revenue (Millions)'], y=data['Rating'])
    plt.title('Revenue vs Rating')
    plt.xlabel('Revenue (Millions)')
    plt.ylabel('Rating')
    st.pyplot(plt)

# Mostrar estadísticas descriptivas del dataset
st.header('Estadísticas Descriptivas del Dataset')
st.write(data.describe())
