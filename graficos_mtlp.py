import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

""""Gráficas para comparaciones entre clusters"""

def barplot_cat(df: pd.DataFrame,
                cluster: str,
                cols_to_graph: list):
    """Barplot de la cantidad de cada categoría por cada columna en el cluster dado"""


    # TODO: pendiente poner nombre de columna label
    df_clust = df[df['cluster'] == cluster]

    # TODO: pendiente cambiar estos nombres
    datos = {'tipo': [], 'carrera': [], 'cantidad': []}

    # TODO: Nombre de gráfica y labels
    for col in cols_to_graph:
        for key, value in df_clust[col].value_counts().to_dict().items():
            datos['tipo'].append(key)
            datos['carrera'].append(col)
            datos['cantidad'].append(value)

    fig, ax = plt.subplots()
    sns.barplot(data=datos,
                x='tipo',
                y='cantidad',
                hue='carrera',
                palette="mako")

    return fig

def boxplot_cluster_vs_continuas(df: pd.DataFrame,
                           clusters: list,
                           colnum: str):
    """Comparar diferentes clusters con respecto a una columna en su blox_plot"""
   
    df_show = df.loc[df['cluster'].isin(clusters)]

    fig, ax = plt.subplots()
    sns.boxplot(x=df_show["cluster"], y=df_show[colnum], palette="mako")

    return fig

def dens_plot_cluster_vs_continuas(df: pd.DataFrame,
                        clusters: list,
                        col: str):
    """Comparar diferentes clusters con respecto a una columna en su densidad"""
    # TODO
    
    df_show = df.loc[df['cluster'].isin(clusters)]

    
    #fig, ax = plt.subplots()
    fig = sns.displot(df_show, x=col, hue="cluster", kind="kde")
    #df_show.pivot(columns='cluster', values=col).plot.density(figsize = (7, 7), linewidth = 4)
      
    #plt.xlabel(col)

    return fig


def violin_plot_cluster_vs_continuas(df: pd.DataFrame,
                          clusters: list,
                          col: str):
    """Comparar diferentes clusters con respecto a una columna en su densidad"""
    df_show = df.loc[df['cluster'].isin(clusters)]

    fig, ax = plt.subplots()
    sns.violinplot(x=df_show["cluster"], y=df_show[col], palette="mako")
    
    return fig

""""Gráficas para comparaciones intra clusters"""
#??? Para comparar solo discretas vs continuas?

def boxplot_continuas(df: pd.DataFrame,
                           cluster: list,
                           colcat: str,
                           colnum: str):
    """Comparar una columna del mismo cluster contra una categorica"""

    df_clust = df[df['cluster'] == cluster]

    fig, ax = plt.subplots()
    sns.boxplot(x=df[colcat], y=df[colnum], palette="mako")

    return fig

def violin_plot_continuas(df: pd.DataFrame,
                           cluster: list,
                           colcat: str,
                           colnum: str):
    """Comparar una columna discreta con respecto a una columna continua en su densidad"""
    df_clust = df[df['cluster'] == cluster]

    fig, ax = plt.subplots()
    sns.violinplot(x=df[colcat], y=df[colnum])

    return fig





