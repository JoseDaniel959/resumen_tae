import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def barplot_cat(df: pd.DataFrame,
                cluster: str,
                cols_to_graph: list):
    """Barplot de la cantidad de cada categoría por cada columna en el cluster dado"""
    df_clust = df[df['label'] == cluster]


    # TODO: hacer la gráfica corresondiente la la columna col_to_graph

    pass


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


