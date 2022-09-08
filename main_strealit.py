import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
from tabs import *
from graficos_mtlp import *
# from matplotlib import pyplot as plt
# from sklearn import preprocessing
# from sklearn.cluster import AgglomerativeClustering
# import scipy.cluster.hierarchy as sch
# from sklearn.cluster import KMeans


st.title('Aplicación web de clusters')

df = pd.read_csv('ensayo_graficas.csv')
show_clust, compare = st.tabs(["Características por cluster",
                               "Comparar clusters"])
with show_clust:
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4"])

    with tab1:
        tab_show(0, df)

    with tab2:
        tab_show(1, df)

    with tab3:
        tab_show(2, df)
    with tab4:
        tab_show(3, df)

with compare:
    
    
    #------------------------------------------------------------
    st.markdown('## Ver gráficos de barra')
    
    #option_cluster_barplot = st.selectbox(
        #'¿Qué variable continua desea comparar?',
        #('0','1','2','3'))

    #options_barplot = st.multiselect(
        #'¿Que columnas categóricas quieres comparar?',
        #['CURROPER','CONTROL','CIP11BACHL','CIP15BACHL','CIP14BACHL','CIP27BACHL'],
        #['CURROPER','CONTROL','CIP11BACHL','CIP15BACHL','CIP14BACHL','CIP27BACHL'])
    

  
    #st.pyplot(barplot_cat(df, cluster, carreras_show))

    #barplot_cat(df,'0',['CONTROL'])
    #------------------------------------------------------
    options = st.multiselect(
        '¿Que cluster quieres comparar?',
        [0, 1, 2, 3],
        [0, 1, 2, 3])
    #clusters = [value for value in options.values()]
    option = st.selectbox(
        '¿Qué variable continua desea comparar?',
        ('DEBT_MDN','PCTFLOAN','GRAD_DEBT_MDN','PCIP11','PCIP15','PCIP14','PCIP27','PCTPELL'))

    #print(option)

   
    
    st.write(str(options))
    
    st.pyplot(boxplot_cluster_vs_continuas(df,options,option))
    st.pyplot(dens_plot_cluster_vs_continuas(df,options,option))
    st.pyplot(violin_plot_cluster_vs_continuas(df,options,option))
    
   