import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación de Bases de Ciencia de Datos", layout="centered", initial_sidebar_state="expanded")
st.title("Evaluación de Bases de Ciencia de Datos")
st.markdown("Responde las siguientes preguntas para evaluar tus conocimientos básicos en Ciencia de Datos. Al final, obtendrás un puntaje basado en tus respuestas.")

# Función para calcular puntaje
def calcular_puntaje(respuestas):
    puntaje = 0
    respuestas_correctas = {
        "pregunta_1": "b",
        "pregunta_2": "c",
        "pregunta_3": "a",
        "pregunta_4": "b",
        "pregunta_5": "c"
    }
    for pregunta, respuesta in respuestas.items():
        if respuestas_correctas.get(pregunta) == respuesta:
            puntaje += 1
    return puntaje

# Formulario interactivo
with st.form("formulario_evaluacion"):
    st.subheader("Preguntas")

    # Pregunta 1
    pregunta_1 = st.radio(
        "1. ¿Qué es un DataFrame en pandas?",
        options=["a) Un tipo de base de datos", "b) Una estructura de datos tabular", "c) Una visualización gráfica"],
        key="pregunta_1"
    )

    # Pregunta 2
    pregunta_2 = st.radio(
        "2. ¿Qué función se utiliza para cargar datos desde un archivo CSV en pandas?",
        options=["a) load_csv()", "b) open_csv()", "c) read_csv()"],
        key="pregunta_2"
    )

    # Pregunta 3
    pregunta_3 = st.radio(
        "3. ¿Cuál de las siguientes opciones es una técnica de reducción de dimensionalidad?",
        options=["a) PCA", "b) K-Means", "c) Naive Bayes"],
        key="pregunta_3"
    )

    # Pregunta 4
    pregunta_4 = st.radio(
        "4. ¿Qué mide la métrica R^2 en un modelo de regresión?",
        options=["a) El error promedio", "b) La proporción de varianza explicada", "c) La correlación entre las variables"],
        key="pregunta_4"
    )

    # Pregunta 5
    pregunta_5 = st.radio(
        "5. ¿Qué tipo de gráfico es más adecuado para mostrar la distribución de una variable numérica?",
        options=["a) Gráfico de líneas", "b) Gráfico de barras", "c) Histograma"],
        key="pregunta_5"
    )

    # Botón para enviar
    submit_button = st.form_submit_button("Enviar respuestas")

# Mostrar resultados
if submit_button:
    respuestas = {
        "pregunta_1": pregunta_1.split(")")[0],
        "pregunta_2": pregunta_2.split(")")[0],
        "pregunta_3": pregunta_3.split(")")[0],
        "pregunta_4": pregunta_4.split(")")[0],
        "pregunta_5": pregunta_5.split(")")[0]
    }

    puntaje = calcular_puntaje(respuestas)
    st.markdown(f"## Tu puntaje es: {puntaje}/5")

    # Feedback según puntaje
    if puntaje == 5:
        st.success("¡Excelente! Tienes una base sólida en Ciencia de Datos.")
    elif puntaje >= 3:
        st.info("¡Bien hecho! Tienes buenos conocimientos, pero puedes mejorar.")
    else:
        st.warning("Es un buen momento para repasar los conceptos básicos de Ciencia de Datos.")
