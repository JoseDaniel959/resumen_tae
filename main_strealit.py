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
