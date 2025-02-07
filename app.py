import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')

st.header('Graficos de Vehiculos')

if hist_button:
    st.write(
        'Construir histograma para el conjunto de datos de anuncios de ventas de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)
