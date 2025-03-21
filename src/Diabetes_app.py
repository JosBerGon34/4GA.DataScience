import streamlit as st
from pickle import load

#Cargar el modelo
model = load(open("C:/Users/Josue/4GA.DataScience/models/3c_G_MD4_MF8_MSL4_MSS7.sav", "rb"))

# Variables objetivo y predictoras
target_var = 'Outcome'
predict_var1 = 'Pregnancies'
predict_var2 = 'Glucose'
predict_var3 = 'Insulin'
predict_var4 = 'BMI'
predict_var5 = 'DiabetesPedigreeFunction'
predict_var6 = 'Age'

#Diccionario de clases
class_dict = {
    "0": "No Diabetes",
    "1": "Diabetes"
}

#Título de la aplicación
st.title("Diabetes Prediction")

# Barras deslizantes para las variables predictoras
val1 = st.slider(predict_var1, min_value=0, max_value=16, step=1)  # Pregnancies (0-16)
val2 = st.slider(predict_var2, min_value=25, max_value=200, step=1) # Glucose (25-200)
val3 = st.slider(predict_var3, min_value=0, max_value=350, step=1) # Insulin (0-350)
val4 = st.slider(predict_var4, min_value=10.0, max_value=60.0, step=0.1) # BMI (10.0-60.0)
val5 = st.slider(predict_var5, min_value=0.10, max_value=1.4, step=0.01) # DiabetesPedigreeFunction (0.10-1.4)
val6 = st.slider(predict_var6, min_value=20, max_value=75, step=1) # Age (20-75)

#Botón de predicción
if st.button("Predict"):
    #Realizar la predicción
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6]])[0])

    #Obtener el nombre de la clase predicha
    pred_class = class_dict[prediction]

    #Mostrar la predicción
    st.write("Prediction:", pred_class)