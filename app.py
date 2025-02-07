import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Graficos de Vehiculos')

build_histo = st.checkbox('Construir histograma')
if build_histo:
    st.write(
        'Construir histograma para el conjunto de datos de anuncios de ventas de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

