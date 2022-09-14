from enum import unique
import streamlit as st
from graficos_mtlp import *
from metadata import Texto


def tab_show(cluster, df):

    # carreras = {
    #      'CIP11BACHL': st.checkbox('CIP11BACHL' + ' '*cluster, value=True),
    #      'CIP14BACHL': st.checkbox('CIP14BACHL' + ' '*cluster),
    #      'CIP15BACHL': st.checkbox('CIP15BACHL' + ' '*cluster),
    #      'CIP27BACHL': st.checkbox('CIP27BACHL' + ' '*cluster),
    # }
    # carreras_show = [key for key, value in carreras.items() if value]
    a = ['CIP11BACHL', 'CIP14BACHL', 'CIP15BACHL', 'CIP27BACHL']
    st.pyplot(barplot_cat(df, cluster, a))

    optiont1_cat = st.selectbox(
    '¿Qué variable discreta quiere para el eje X?'+ ' '*cluster,
    ("CURROPER","CONTROL",'CIP11BACHL','CIP15BACHL','CIP14BACHL','CIP27BACHL'))

    optiont1_cont = st.selectbox(
    '¿Qué variable continua quiere para el eje Y?'+ ' '*cluster,
    ('DEBT_MDN','PCTFLOAN','GRAD_DEBT_MDN','PCIP11','PCIP15','PCIP14','PCIP27','PCTPELL'))

    st.pyplot(boxplot_continuas(df, cluster, optiont1_cat, optiont1_cont))
    st.pyplot(violin_plot_continuas(df, cluster, optiont1_cat, optiont1_cont))

    continuas = ['DEBT_MDN', 'PCTFLOAN', 'GRAD_DEBT_MDN', 'PCIP11', 'PCIP15',
                 'PCIP14', 'PCIP27', 'PCTPELL']

    for col in continuas:
        st.markdown(f'### Gráfico de densidad de {col}')
        st.pyplot(melito(df, cluster, col))

def continuas_show(df):
     options = st.multiselect(
        '¿Que cluster quieres comparar?',
        [0, 1, 2, 3,4,5],
        [0, 1, 2, 3,4,5])
    #clusters = [value for value in options.values()]
     option = st.selectbox(
        '¿Qué variable continua desea comparar?',
        ('DEBT_MDN','PCTFLOAN','GRAD_DEBT_MDN','PCIP11','PCIP15','PCIP14','PCIP27','PCTPELL'),key=unique)

 

    

     st.write(str(options))
     if(len(options) != 0):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('##### Boxplot de una variable continua vs clusters seleccionados')
                st.pyplot(boxplot_cluster_vs_continuas(df,options,option))
            with col2:
                st.markdown('##### Diagrama de densidad de una variable continua vs clusters seleccionados')
                st.pyplot(dens_plot_cluster_vs_continuas(df,options,option))

            st.markdown('En el boxplot, la línea dentro de la caja representa la mediana de los datos y el ancho de la caja está dado por la dispersión de los datos sobre esa mediana.')
            st.markdown('En las gráficas de densidad, en donde aparezca el pico mas alto se dice que es la moda y en donde es mas ancha la curva es donde mayor cantidad de datos.')

        
     else:
            st.markdown("##### Seleccione algún cluster")

