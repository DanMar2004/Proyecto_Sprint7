import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Graficos de Vehiculos')

build_histo = st.button('Construir histograma')
if build_histo:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir grafico de dispersion')
if build_scatter:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)