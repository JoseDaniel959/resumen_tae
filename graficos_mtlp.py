import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def boxplot_continuas(df: pd.DataFrame,
                      clusters: list,
                      col: str):
    """Comparar diferentes clusters con respecto a una columna en su blox_plot"""
    # TODO
    pass


def dens_plot_continuas(df: pd.DataFrame,
                        clusters: list,
                        col: str):
    """Comparar diferentes clusters con respecto a una columna en su densidad"""
    # TODO
    pass


def violin_plot_continuas(df: pd.DataFrame,
                          clusters: list,
                          col: str):
    """Comparar diferentes clusters con respecto a una columna en su densidad"""
    # TODO
    pass


