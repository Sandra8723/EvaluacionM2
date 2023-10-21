import pandas as pd
import streamlit as st

data = pd.read_csv('historico_resultados_pruebas_saber_11.csv')

data = data.dropna()
data

st.header("Filtro 1")
st.write ("seleccionar las palabras claves: popular  y manrique, de la columna registros")
palabras_clave = ['popular','manrique']
filtro1 = data[data["registros"].isin(palabras_clave)]
st. dataframe(filtro1)

st.header("Filtro 2")
st.write ("Mostrar puntaje global diferente a 246")
filtro2 = data[data["puntaje_global"] != 246]
st.dataframe(filtro2)

st.header("Filtro 3")
st.write ("Mostrar los publicados ")
filtro3 = data[(data['publicados']==63)]
st. dataframe(filtro3)


st.header("Filtro 4")
st.write ("Mostrar los puntajes de matematicas iguales a 49")
filtro4 = data[(data['puntaje_matematicas']==49)]
st. dataframe(filtro4)

st.header("Filtro 5")
st.write ("Mostrar los establecimientos de la comuna popular ")
filtro5 = data[(data["prestacion_servicio"]=='privado')]
st. dataframe(filtro5)



