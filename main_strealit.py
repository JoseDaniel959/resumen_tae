import streamlit as st
import pandas as pd
import numpy as np

from tabs import *
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
    options = st.multiselect(
        '¿Que cluster quieres comparar?',
        [0, 1, 3, 4],
        [0, 1, 3, 4])
    #clusters = [value for value in options.values()]
    st.write(str(options))
