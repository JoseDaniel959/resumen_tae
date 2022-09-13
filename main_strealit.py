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


st.title('Aplicación web de segmentos de universidades en EEUU')

col1, col2, col3,col4 = st.columns(4)
with col1:
    st.image(image,width=80)
with col2:
    st.image(image2,width=80)
with col3:
    st.image(image1,width=80,use_column_width=100)



st.markdown('## Propósito')
st.markdown('El departamento de Estados Unidos comparte información al público sobre las universidades del país, para que puedan tomar una decisión al momento de elegir una. El propósito de esta aplicación web es ayudar a los que deseen estudiar, escoger una universidad. ')

st.markdown('Para la selección de la universidad, se debe basar en los siguiente criterios:')
st.markdown('- **Tipo de universidad**: ya si sea pública privada o privada con ánimo de lucro.')
st.markdown('- **Tipo de carrera:** Los que deseen estudiar Computación,ingeniería,ingeniería y tecnología o matemáticas.')
st.markdown('- **Modalidad de estudio:** presencial o virtual.')
st.markdown('- **Porcentaje de estudiantes que reciben prestamos:** Pell Grant o Loan.')
st.markdown('En base a los criterios se dividieron a las universidades en 6 segmentos.En esta aplicación web se podrá ver las características de cada uno segmentos. Además se puede comparar todas las características de los segmentos juntos')

st.markdown('### Información adicional')
st.markdown('Se proporciona la siguiente información,para que el aspirante se pueda informar más y tomar una mejor decisión')


st.markdown('## Segmentos')




df = pd.read_csv('base1 (2).csv') 
df.rename({'Clusters': 'cluster'}, axis=1, inplace=True)
show_clust, compare = st.tabs(["Características por cluster",
                               "Comparar clusters"])

coordenadas = pd.read_csv('sinNulosyConCoordenadas.csv')
coordenadas['Cluster'] = df['cluster'] 
coordenadas = coordenadas[["LONGITUDE", "LATITUDE","INSTNM",'Cluster']].dropna(axis = 0,subset = ["LONGITUDE", "LATITUDE"])

print("sin nulos")
print(coordenadas.info())
print(coordenadas['Cluster'].unique())



def map(numeroCluster):
    
    coordenadas_show = coordenadas[coordenadas['Cluster'] == option]
    col1, col2, col3,col4, = st.columns(4)
    if(numeroCluster == 0):
        color = [255, 0, 0]
        cheap = Image.open('cheap.png')
        loans = Image.open('noloans.webp')
        bachelordegree = Image.open('bachelordegree.png')
        arrowDown = Image.open('arrowD.png')
        st.markdown('### Características del Segmento 1')
        with col1:
            st.image(cheap,width=100)
            st.markdown('Universidades Públicas, más baratas')
        with col2:
            st.image(loans,width=100)
            st.markdown(' Menos prestamos federales')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('Menos carreras de interés')
        with col4:
            st.image(arrowDown,width=100)
            st.markdown('Poca gente graduada de estas universidades')
      
        
    elif(numeroCluster == 1):
        st.markdown('### Características del Segmento 2')
        expensive = Image.open('expensive.png')
        prestamos = Image.open('prestamos.webp')
        bachelordegree = Image.open('bachelordegree.png')
        arrowDown = Image.open('arrowD.png')
        with col1:
            st.image(expensive,width=100)
            st.markdown('Universidades Privadas, más baratas')
        with col2:
            st.image(prestamos,width=100)
            st.markdown(' Más prestamos federales')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('Más oferta de carreras en modalidad prescencial')
        with col4:
            st.image(arrowDown,width=100)
            st.markdown('Mayor porcentaje de estudiantes graduados de estas universidades')
        color = [0, 255, 0]
    elif(numeroCluster == 2):
        color = [0, 0, 255]
    elif(numeroCluster == 3):
        color = [255, 255, 0]
    elif(numeroCluster == 4):
        color = [255, 0, 255]
    elif(numeroCluster == 5):
        print("Entro")
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
        ["Segmento 1", "Segmento 2", "Segmento 3", "Segmento 4", "Segmento 5", "Segmento 6"])
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
        st.markdown('#### Información sobre los segmentos')
        st.markdown('')
        st.markdown('##### Segmento 1')
        st.markdown('Compuesto por universidades públicas, en donde está el menor porcentaje de estudiantes con un préstamo federal y por tanto la menor deuda media. Sin embargo es el segmento que contiene las universidades con menor oferta de las carreras de interés, por ende es donde menor cantidad de estudiantes graduados en dichos pregrados hay.')
        st.markdown('##### Segmento 2')
        st.markdown('Compuesto por universidades en su mayoría privadas con ánimo de lucros y poseen un mayor porcentaje de estudiantes tanto con préstamo federal como con beca Pell Grants, debido a esto sus estudiantes tienen una deuda media mayor que los segmento 0 y 2 y es el de mayor deuda media de sus estudiantes graduados (junto con los segmento 3 y 4). En este segmento es donde se encuentran las universidades con más oferta presencial de los campos de computación e ingeniería y tecnología, además es donde mayor porcentaje de estudiantes graduados en computación, ingeniería y tecnología y matemáticas hay.')
    with col5:
        data = coordenadas['Cluster'].value_counts()
        print(data)
        st.pyplot(grafico_torta(data))
        
        
        
    col6,col7,col8,col9 = st.columns(4)
    
    with col6:
        st.markdown('##### Segmento 3')
        st.markdown('Compuesto por universidades en su mayoría privadas con ánimo de lucros y poseen un mayor porcentaje de estudiantes tanto con préstamo federal como con beca Pell Grants, debido a esto sus estudiantes tienen una deuda media mayor que los segmento 0 y 2 y es el de mayor deuda media de sus estudiantes graduados (junto con los segmento 3 y 4). En este segmento es donde se encuentran las universidades con más oferta presencial de los campos de computación e ingeniería y tecnología, además es donde mayor porcentaje de estudiantes graduados en computación, ingeniería y tecnología y matemáticas hay.')

    with col7:
        st.markdown('##### Segmento 4')
        st.markdown('Compuesto únicamente por universidades privadas con ánimo de lucro similar al segmento 0 contiene las universidas con menor oferta de las carreras y menor deuda media de sus estudiantes, pero tiene una mayor oferta que el cluster 0 de computación en la modalidad virtual. Tiene un porcentaje de estudiantes con préstamo federal muy similar a los segmneto 3, 4 y 5 y es el segundo en cuanto a estudiantes con beca Pell Grants. Respecto a los graduados, es el de menor porcentaje de estos en las carreras salvo en computación y en ingeniería y tecnología que es el segundo mayor.')

    with col8:
        st.markdown('##### Segmento 5')
        st.markdown('Compuesto únicamente por universidades públicas y privadas sin ánimo de lucro (siendo mayor la cantidad de éstas ultimas en el segmento) las cuales ofertan las carreras únicamente de forma presencial. Como en el segmento 3 tiene un porcentaje similar de estudiantes con préstamos federales a los segmento 2 y 5, pero es el segmento con universidades cuyos estudiantes tienen la mayor deuda media, ocasionado probablemente también porque es el de menor porcentaje de estudiantes con beca Pell Grants. Respecto al porcentaje de universidades graduados en sus universidades, ocurre aproximadamente lo mismo que en el segmento 3.')
    with col9:
        st.markdown('##### Segmento 6')
        st.markdown('Compuesto únicamente por universidades privadas sin ánimo de lucro, las universidades dentro de este grupo son similares en cuanto a su no oferta de las carreras como los segmento 0 y 2, sin embargo tienen un poco más de oferta en los campos de computación y matemáticas en las modalidades presencial y virtual que estos 2 segmento anteriormente mencionados. Su deuda media y porcentaje de estudiantes con préstamo federal son similares a los de segmento 1 y 4 respectivamente y es el tercero en cuanto a mayor media de porcentaje de estudiantes con becas Pell Grants. Destaca en que es el segmento con mayor porcentaje de graduados en ingeniería y en general es el tercero con mayor porcentaje de estudiantes graduados para las demás carreras.')

   
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.markdown('### Mapa de las universidades')
    st.markdown('En el siguiente mapa se puede escoger las universidadades por segmento (cada universidad está representada con un circulo). Si pone el cursor encima del circulo, saldrá el nombre de la unviersidad.Para todos los segmentos o agrupaciones o segmentos, la mayoría de las universidades quedan al este de Estados Unidos.')

    st.markdown('##### seleccione el segmento')
    option = st.selectbox(
        '¿Qué segmento desea comparar?',
        (0,1,2,3,4,5))
    x = option 
    print("opcion",x)
    st.write(map(x))

    st.markdown('### Estadísticas de las universidades por segmentos y variables ')
    continuas_show(df)
    