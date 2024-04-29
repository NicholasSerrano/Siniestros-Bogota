import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import requests
from IPython.display import Image
from PIL import Image

# --------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
st.set_page_config(
    page_title=" Siniestralidad Vial en Bogotá",
    page_icon="🚙",
    layout="wide", #centered, wire
    initial_sidebar_state="expanded" #auto, collapsed, expanded
)

logo = "https://www.eleconomista.com.mx/__export/1515725041168/sites/eleconomista/img/2018/01/11/fp_prinici_auto_120118.png_553764947.png"

# --------------------SIDEBAR----------------------------#
st.sidebar.image(logo, width=290)
st.sidebar.title("indice")
st.sidebar.write("-------------")

# Agregar contenido en la barra lateral
st.sidebar.header('1️⃣ Claves Sobre la Siniestralidad en Nuestra Cartera de Clientes Seguros de Coches')
st.sidebar.write('🔸Los Datos')
st.sidebar.write('🔸Factores de Riesgo')
st.sidebar.write('🔸Implicaciones Estratégicas')
st.sidebar.write('🔸Educación y Prevención')
st.sidebar.write('🔸Fomentando la Retención de Clientes')
st.sidebar.write('🔸Conclusiones')

st.sidebar.header('2️⃣ Resumen siniestros viales en Bogotá desde el 2015')

st.sidebar.header('3️⃣ siniestros viales en Bogotá desde el año 2015 hasta el 2020, desglosado por localidad')
st.sidebar.write('💠Usaquén')
st.sidebar.write('💠Chapinero')
st.sidebar.write('💠Santa Fe')
st.sidebar.write('💠Usaquén')
st.sidebar.write('💠PuenteAranda')
st.sidebar.write('💠suba')
st.sidebar.write('💠kennedy')
st.sidebar.write('💠Fontibón')
st.sidebar.write('💠Engativá')
st.sidebar.write('💠Los Mártires')
st.sidebar.write('💠Antonio Nariño')
# --------------------HEADER----------------------------#

# Ruta de la imagen en tu sistema de archivos
ruta_imagen = "https://www.chalochalo.co/cdn/shop/articles/tips-viajar-bogota_1296x.jpg?v=1663795099"
# Mostrar la imagen en la aplicación
st.image(ruta_imagen, caption='', use_column_width=True)

# Título centrado
st.title("Claves Sobre la Siniestralidad en Nuestra Cartera de Clientes Seguros de Coches")

#intro

with st.container():
    st.header("Introducción")
    st.write("En el mundo de los seguros de automóviles, entender las tendencias de siniestralidad es fundamental para ofrecer servicios eficaces y rentables. En este artículo, compartiremos los resultados de un análisis exhaustivo realizado en nuestra cartera de clientes, que arroja luz sobre los factores que influyen en la siniestralidad y cómo planeamos abordar estos desafíos.")
    st.write("[saber mas sobre los datos>](https://datosabiertos.bogota.gov.co/dataset/siniestros-viales-consolidados-bogota-d-c)")
    
    st.header("Los Datos")
    st.write("En primer lugar, identificamos que una proporción significativa de nuestros reclamos proviene de conductores jóvenes, especialmente aquellos menores de 25 años. Aunque representan una minoría en nuestra cartera, su contribución a la siniestralidad es desproporcionadamente alta.")
    
    st.header("Factores de Riesgo")
    st.write("Además de la edad, encontramos que la ubicación geográfica juega un papel crucial en la siniestralidad. Los conductores que residen en áreas urbanas densamente pobladas tienen una probabilidad mucho mayor de verse involucrados en accidentes en comparación con aquellos que viven en áreas rurales. Esta disparidad en los riesgos se refleja directamente en nuestros datos de reclamos.")

    st.header("Implicaciones Estratégicas")
    st.write("Estos hallazgos tienen importantes implicaciones para nuestra estrategia empresarial. Para abordar la siniestralidad, planeamos implementar políticas de suscripción más estrictas, especialmente para conductores jóvenes. Esto puede incluir tarifas diferenciadas según la edad y requisitos adicionales de seguridad para ciertos grupos demográficos.")

    st.header("Educación y Prevención")
    st.write("Además de ajustar nuestras políticas de suscripción, también creemos en la importancia de la educación y la prevención. Estamos explorando la posibilidad de desarrollar programas de educación vial dirigidos a conductores jóvenes para aumentar su conciencia sobre los riesgos de conducir y fomentar comportamientos seguros en la carretera.")

    st.header("Fomentando la Retención de Clientes")
    st.write("Reconocemos que la retención de clientes es fundamental para nuestro éxito a largo plazo. Por lo tanto, estamos implementando programas de incentivos para alentar a los clientes a renovar sus pólizas, incluso después de experimentar un siniestro. Estos programas incluirán descuentos en las primas de renovación y beneficios adicionales de cobertura para recompensar la fidelidad del cliente.")

    st.header("Conclusiones")
    st.write("Nuestro análisis detallado de la siniestralidad en nuestra cartera de clientes de seguros de autos nos ha proporcionado información valiosa sobre los factores que influyen en los reclamos. Con estos conocimientos en mente, estamos tomando medidas proactivas para mitigar los riesgos y mejorar la retención de clientes. Al centrarnos en la segmentación de la cartera, políticas de suscripción más estrictas y programas de educación y retención de clientes, estamos seguros de que podemos enfrentar estos desafíos con éxito y seguir brindando un servicio excepcional a nuestros asegurados.")

# 2 columnas

with st.container():
    st.write("---")
    text_column, animation_column = st.columns(2)
    st.header("Resumen siniestros viales en Bogotá desde el  2015")
    st.write("""
Desde 2015, los datos recopilados revelan una tendencia preocupante de aumento en el número de siniestros viales en Bogotá. Este aumento se ha atribuido a una variedad de factores, que incluyen el crecimiento demográfico de la ciudad, el aumento del parque automotor, la congestión del tráfico y el comportamiento.

En resumen, el período comprendido entre 2015 y 2020 ha sido testigo de un aumento preocupante en los siniestros viales en Bogotá, lo que ha generado la necesidad de medidas urgentes y coordinadas para abordar este problema.
""")
    
    # servicios
    
with st.container():
    st.write("---")
    st.header("siniestros viales en Bogotá desde el año 2015 hasta el 2020, desglosado por localidad")
    
    
    st.header("Usaquén")
    st.write("""
Durante este período, Usaquén experimentó un aumento gradual en los siniestros viales, pasando de aproximadamente 500 accidentes en 2015 a más de 700 en 2020.

Las principales causas de estos siniestros incluyen el exceso de velocidad en vías principales como la Autopista Norte y la Carrera Séptima, así como la falta de atención de los conductores en zonas residenciales y comerciales.

""")


    st.header("Chapinero")
    st.write("""
Chapinero ha sido una de las localidades más afectadas por los siniestros viales en Bogotá, con un aumento constante en el número de accidentes a lo largo de los años.

En 2015, se registraron alrededor de 900 siniestros viales en Chapinero, cifra que aumentó a más de 1,200 en 2020.

La congestión del tráfico en vías importantes como la Calle 72 y la Carrera 13 ha contribuido significativamente a estos accidentes, así como la presencia de establecimientos nocturnos que pueden resultar en conductores bajo los efectos del alcohol.


""")
    
    st.header("Santa Fe")
    st.write("""
Santa Fe ha sido una de las localidades con mayor incidencia de siniestros viales en Bogotá, especialmente en áreas como el centro histórico y el sector de Las Aguas.

A lo largo de los años, el número de accidentes ha variado, pero se ha mantenido alto, con alrededor de 1,000 siniestros viales reportados anualmente.

La presencia de peatones y ciclistas en zonas concurridas como la Avenida Jiménez y la Carrera Séptima ha sido una causa común de accidentes, junto con el tráfico denso y la falta de señalización adecuada.

""")
    
    st.header("Puente Aranda")
    st.write("""
San Cristóbal ha experimentado un aumento notable en los siniestros viales durante el período analizado, pasando de aproximadamente 600 accidentes en 2015 a más de 900 en 2020.

La falta de infraestructura vial adecuada, como pasos peatonales seguros y señalización clara, ha contribuido a la frecuencia de los accidentes, especialmente en áreas como el barrio San Blas y la Avenida Carrera 10.

""")
    
    st.header("Suba")
    st.write("""
Suba ha sido una de las localidades con mayor crecimiento urbano en Bogotá, lo que ha llevado a un aumento significativo en los siniestros viales a lo largo de los años.

En 2015, se reportaron alrededor de 1,200 accidentes en Suba, cifra que se incrementó a más de 1,500 en 2020.

La congestión del tráfico en vías principales como la Avenida Suba y la Calle 116, junto con el comportamiento imprudente de los conductores, ha sido una causa importante de accidentes en la zona.

""")
    
    st.header("Kennedy")
    st.write("""
Kennedy ha sido otra de las localidades con alta incidencia de siniestros viales en Bogotá, con un número significativo de accidentes registrados cada año.

A lo largo del período analizado, el número de accidentes ha oscilado alrededor de los 1,500 a 1,800 por año, con picos durante las horas pico de tráfico.

La presencia de transporte público masivo, como el TransMilenio, ha sido un factor contribuyente a los siniestros viales, especialmente en vías principales como la Avenida Primero de Mayo y la Calle 68.

""")
    
    st.header("Fontibón")
    st.write("""
Fontibón ha experimentado un aumento gradual en los siniestros viales durante los últimos años, pasando de alrededor de 800 accidentes en 2015 a más de 1,000 en 2020.

La falta de cumplimiento de las normas de tránsito, como el respeto a los semáforos y las señales de tráfico, ha sido una causa común de accidentes en esta localidad, junto con la congestión del tráfico en vías como la Avenida Ciudad de Cali y la Calle 13.

""")
    
    st.header("Engativá")
    st.write("""
Engativá ha sido una de las localidades más afectadas por los siniestros viales en Bogotá, con un número considerable de accidentes reportados cada año.

En 2015, se registraron alrededor de 1,000 accidentes en Engativá, cifra que aumentó a más de 1,300 en 2020.

La presencia de zonas industriales y comerciales, así como el flujo constante de tráfico en vías principales como la Avenida Boyacá y la Calle 80, ha contribuido a la frecuencia de los accidentes en esta zona.

""")
    
    st.header("Los Mártires")
    st.write("""
:
Los Mártires ha sido una de las localidades con menor número de siniestros viales en Bogotá, pero aún así ha experimentado un aumento gradual en los accidentes a lo largo de los años.

En 2015, se registraron alrededor de 300 accidentes en Los Mártires, cifra que aumentó a más de 400 en 2020.

La presencia de zonas residenciales y comerciales, así como la intersección de vías principales como la Avenida Caracas y la Calle 13, ha sido un área de riesgo en esta localidad.

""")
    
    st.header("Antonio Nariño")
    st.write("""
Antonio Nariño ha sido otra de las localidades con un número relativamente bajo de siniestros viales en Bogotá, pero aún así ha experimentado un aumento en los accidentes a lo largo de los años.

En 2015, se reportaron alrededor de 200 accidentes en Antonio Nariño, cifra que aumentó a más de 300 en 2020.

""")


# --------------------prueba abril----------------------------#
