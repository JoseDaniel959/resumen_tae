import streamlit as st
import pandas as pd

from graficos_mtlp import *

cluster = st.radio(
     "selecciona cluster",
     range(4))

carreras = {
     'CIP11BACHL': st.checkbox('CIP11BACHL', value=True),
     'CIP14BACHL': st.checkbox('CIP14BACHL'),
     'CIP15BACHL': st.checkbox('CIP15BACHL'),
     'CIP27BACHL': st.checkbox('CIP27BACHL'),
}

carreras_show = [key for key, value in carreras.items() if value]

df = pd.read_csv('ensayo_graficas.csv')

st.pyplot(barplot_cat(df, cluster, carreras_show))


"""Gráfica de los boxplot"""
clusters = {
     "0": st.checkbox("0", value=True),
     "1": st.checkbox("1"),
     "2": st.checkbox("2"),
     "3": st.checkbox("3"),
}

continua = st.radio(
     "Seleccione la variable",
     ('DEBT_MDN','PCTFLOAN','GRAD_DEBT_MDN','PCIP11','PCIP15','PCIP14','PCIP27','PCTPELL')
)

clusters_show = [int(key) for key, value in clusters.items() if value]

st.pyplot(boxplot_cluster_vs_continuas(df, clusters_show, continua))
