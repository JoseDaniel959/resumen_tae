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

df = pd.read_csv('base1.csv')
df.rename({'Clusters': 'cluster'}, axis=1, inplace=True)
show_clust, compare = st.tabs(["Características por cluster",
                               "Comparar clusters"])
with show_clust:
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5", "Cluster 6"])
    with tab1:
        tab_show(0, df)
    with tab2:
        tab_show(1, df)
    with tab3:
        tab_show(2, df)
    with tab4:
        tab_show(3, df)
    with tab5:
        tab_show(4, df)
    with tab6:
        tab_show(5, df)


with compare:
    options = st.multiselect(
        '¿Que cluster quieres comparar?',
        [0, 1, 3, 4],
        [0, 1, 3, 4])
    #clusters = [value for value in options.values()]
    st.write(str(options))
