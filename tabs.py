import streamlit as st
from graficos_mtlp import *
from metadata import Texto


def tab_show(cluster, df):

     st.write(Texto.caract_per_clust[cluster]['grafica1'])
     carreras = {
         'CIP11BACHL': st.checkbox('CIP11BACHL' + ' '*cluster, value=True),
         'CIP14BACHL': st.checkbox('CIP14BACHL' + ' '*cluster),
         'CIP15BACHL': st.checkbox('CIP15BACHL' + ' '*cluster),
         'CIP27BACHL': st.checkbox('CIP27BACHL' + ' '*cluster),
    }
     carreras_show = [key for key, value in carreras.items() if value]

     st.pyplot(barplot_cat(df, cluster, carreras_show))

     optiont1_cat = st.selectbox(
        '¿Qué variable discreta quiere para el eje X?'+ ' '*cluster,
        ("CURROPER","CONTROL",'CIP11BACHL','CIP15BACHL','CIP14BACHL','CIP27BACHL'))
     
     optiont1_cont = st.selectbox(
        '¿Qué variable continua quiere para el eje Y?'+ ' '*cluster,
        ('DEBT_MDN','PCTFLOAN','GRAD_DEBT_MDN','PCIP11','PCIP15','PCIP14','PCIP27','PCTPELL'))

     st.pyplot(boxplot_continuas(df, cluster, optiont1_cat, optiont1_cont))
     st.pyplot(violin_plot_continuas(df, cluster, optiont1_cat, optiont1_cont))
