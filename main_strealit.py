import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tabs import *
import pydeck as pdk
# from matplotlib import pyplot as plt
# from sklearn import preprocessing
# from sklearn.cluster import AgglomerativeClustering
# import scipy.cluster.hierarchy as sch
# from sklearn.cluster import KMeans

image = Image.open('eeuu.png')
image1 = Image.open('university.png')
image2 = Image.open('bachelor.png')
image3 = Image.open('desarrollo2.png')

st.set_page_config(layout="wide", page_title="Aplicación web de clusters", page_icon=":taxi:")

#st.title('Aplicación web de clusters')


st.title('Aplicación web de clusters')

col1, col2, col3,col4 = st.columns(4)
with col1:
    st.image(image,width=80)
with col2:
    st.image(image2,width=80)
with col3:
    st.image(image1,width=80,use_column_width=100)



st.markdown('## Propósito')
st.markdown('El departamento de Estados Unidos comparte información al público sobre las universidades del país, para que puedan tomar una decisión al momento de elegir una. El propósito de esta aplicación web es ayudar a la gente que  ')

st.markdown('El propósito de esta aplicación es que los que deseen estudiar se puedan basar en estos criterios:')
st.markdown('- Tipo de universidad: ya si sea pública privada o privada con ánimo de lucro')
st.markdown('- Los que deseen estudiar Computación,ingeniería,ingeniería y tecnología o matemáticas')
st.markdown('- Modalidad de estudio: presencial o virtual')
st.markdown('- Porcentaje de estudiantes que reciben prestamos: Pell Grant o Loan')
st.markdown('En esta aplicación web se podrá ver las características de cada uno cluster. Además se puede comparar todas las características de los clusters ')

st.markdown('## Clusters')




df = pd.read_csv('base1 (2).csv') 
df.rename({'Clusters': 'cluster'}, axis=1, inplace=True)
show_clust, compare = st.tabs(["Características por cluster",
                               "Comparar clusters"])

coordenadas = pd.read_csv('sinNulosyConCoordenadas.csv')
coordenadas['Cluster'] = df['clusters'] 
coordenadas = coordenadas[["LONGITUDE", "LATITUDE","INSTNM",'Cluster']].dropna(axis = 0,subset = ["LONGITUDE", "LATITUDE"])

print("sin nulos")
print(coordenadas.info())



def map(numeroCluster):
    
    coordenadas_show = coordenadas[coordenadas['Cluster'] == option]
    
    if(numeroCluster == 0):
        color = [255, 0, 0]
        st.markdown('### Características del Cluster 0')
        st.markdown('Mucho texto mucho texto mucho texto este cluster tiene las siguientes características')
        st.markdown('- Daniel daza encias')
        st.markdown('- fdafdfadfas')
        st.markdown('Mucho texto mucho texto mucho texto este cluster tiene las siguientes características')
        st.markdown('Siente mi aliento, sexoooo quiero yoooo')       

    elif(numeroCluster == 1):
        color = [0, 255, 0]
    elif(numeroCluster == 2):
        color = [0, 0, 255]
    elif(numeroCluster == 3):
        color = [255, 255, 0]
    elif(numeroCluster == 4):
        color = [255, 0, 255]
    elif(numeroCluster == 5):
        color = [0, 255, 255]                  
    
    layer = pdk.Layer(
    "ScatterplotLayer",
    coordenadas_show,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=50,
    radius_min_pixels=5,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position=["LONGITUDE", "LATITUDE"],
    get_radius="exits_radius",
    get_fill_color=color,
    get_line_color=[0, 0, 0],
)

# Set the viewport location
    view_state = pdk.ViewState(
        latitude=37.7749295, longitude=-122.4194155, zoom=6, min_zoom=0, max_zoom=15, bearing=0, pitch=0)

    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{INSTNM}"})   
    return r



with st.sidebar:
    
    st.image(image3,width=80)
    st.markdown("#### Desarrollado por:")
    st.markdown("- Jose Daniel Bustamante Arango.")
    st.markdown("- Daniel Santiago Cadavid Montoya.")
    st.markdown("- Ronald Grabiel Palencia.")
    st.markdown("- Marlo Calle Areiza.")
    st.markdown("- Daniel Daza Macías.")

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
    

    st.markdown('### Proporción de universidades por segmentos ')

    col4,col5 = st.columns(2)
    
    with col4:
        data = df['clusters'].value_counts()
        st.pyplot(grafico_torta(data))
    with col5:
        st.markdown('#### Información sobre los segmentos')
        st.markdown('')
        st.markdown('##### Segmento 1')
        st.markdown('Este segmento contiene las universidades que son públicas y')
        st.markdown('##### Segmento 2')

        st.markdown('##### Segmento 3')

        st.markdown('##### Segmento 4')
        
        st.markdown('##### Segmento 5')
    
    st.markdown('### Mapa de las universidades')
    st.markdown('En el siguiente mapa, se puede escoger las universidadades por clusters(las universidades son los circulos). Si pone el cursor encima de la bola, saldrá el nombre de la unviersidad')

    st.markdown('Hola bb')
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    
    
    
    option = st.selectbox(
        '¿Qué cluster desea comparar?',
        (0,1,2,3,4,5))
    st.write(map(option))

    

    #------------------------------------------------------------


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
    
    #clusters = [value for value in options.values()]
    continuas_show(df)
