import streamlit as st
import pandas as pd

from graficos_mtlp import *

cluster_1 = st.checkbox('cluster_1')
cluster_2 = st.checkbox('cluster_2')
cluster_3 = st.checkbox('cluster_3')

st.pyplot(grafico_2(cluster_1, cluster_2, cluster_3))
st.pyplot(grafico_2(cluster_1, cluster_2, cluster_3))
st.pyplot(grafico_2(cluster_1, cluster_2, cluster_3))
st.pyplot(grafico_2(cluster_1, cluster_2, cluster_3))