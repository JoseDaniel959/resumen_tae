import streamlit as st
import pandas as pd

from graficos_mtlp import *

cluster = st.radio(
     "selecciona cluster",
     range(4))
df = pd.read_csv('ensayo_graficas.csv')

st.pyplot(barplot_cat(df, cluster, ['CIP11BACHL', 'CIP14BACHL', 'CIP15BACHL']))