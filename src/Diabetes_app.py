import streamlit as st
from pickle import load

# Cargar el modelo
model = load(open("C:/Users/Josue/4GA.DataScience/models/3c_G_MD4_MF8_MSL4_MSS7.sav", "rb"))

# Variables objetivo y predictoras
target_var = 'Outcome'
predict_var1 = 'Pregnancies'
predict_var2 = 'Glucose'
predict_var3 = 'Insulin'
predict_var4 = 'BMI'
predict_var5 = 'DiabetesPedigreeFunction'
predict_var6 = 'Age'

# Diccionario de clases
class_dict = {
    "0": "No Diabetes",
    "1": "Diabetes"
}

# Título de la aplicación
st.title("Diabetes Prediction")

# Valores iniciales de las barras deslizantes
initial_values = {
    predict_var1: 0,
    predict_var2: 100,
    predict_var3: 100,
    predict_var4: 30.0,
    predict_var5: 0.5,
    predict_var6: 40
}

# Función para restablecer los valores
def reset_values():
    for var, value in initial_values.items():
        st.session_state[var] = value

# Inicializar st.session_state si no existe
if 'initialized' not in st.session_state:
    for var, value in initial_values.items():
        st.session_state[var] = value
    st.session_state['initialized'] = True

# Barras deslizantes para las variables predictoras
val1 = st.slider(predict_var1, min_value=0, max_value=16, step=1, key=predict_var1)
val2 = st.slider(predict_var2, min_value=25, max_value=200, step=1, key=predict_var2)
val3 = st.slider(predict_var3, min_value=0, max_value=350, step=1, key=predict_var3)
val4 = st.slider(predict_var4, min_value=10.0, max_value=60.0, step=0.1, key=predict_var4)
val5 = st.slider(predict_var5, min_value=0.10, max_value=1.4, step=0.01, key=predict_var5)
val6 = st.slider(predict_var6, min_value=20, max_value=75, step=1, key=predict_var6)

# Botón de predicción
if st.button("Predict"):
    # Realizar la predicción
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6]])[0])

    # Obtener el nombre de la clase predicha
    pred_class = class_dict[prediction]

    # Mostrar la predicción
    st.write("Prediction:", pred_class)

# Botón de reset
if st.button("Reset"):
    reset_values()
    st.experimental_rerun()