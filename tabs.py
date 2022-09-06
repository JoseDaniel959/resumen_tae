import streamlit as st
from graficos_mtlp import *


def tab_show(cluster, df):
    carreras = {
         'CIP11BACHL': st.checkbox('CIP11BACHL' + ' '*cluster, value=True),
         'CIP14BACHL': st.checkbox('CIP14BACHL' + ' '*cluster),
         'CIP15BACHL': st.checkbox('CIP15BACHL' + ' '*cluster),
         'CIP27BACHL': st.checkbox('CIP27BACHL' + ' '*cluster),
    }
    carreras_show = [key for key, value in carreras.items() if value]
    st.pyplot(barplot_cat(df, cluster, carreras_show))