import streamlit as st
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Cargar el modelo
@st.cache_resource
def load_model():
    with open("C:/Users/Josue/4GA.DataScience/models/3c_G_MD4_MF8_MSL4_MSS7.sav", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()

# Obtener nombres de características del modelo
feature_names = model.feature_names_in_.tolist()

# Interfaz de usuario
st.title("Visualizador de Árbol de Clasificación")

# Mostrar el árbol
st.subheader("Árbol de Decisión")
fig, ax = plt.subplots(figsize=(20, 10))
plot_tree(model, filled=True, feature_names=feature_names, ax=ax)
st.pyplot(fig)

# Mostrar reglas del árbol (opcional)
st.subheader("Reglas del Árbol")
from sklearn.tree import export_text
tree_rules = export_text(model, feature_names=feature_names)
st.text(tree_rules)

# Predicciones (opcional)
st.subheader("Predicciones")
st.write("Introduce los valores de las características para hacer una predicción:")

# Crear campos de entrada para cada característica
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"{feature}:")

# Botón para realizar la predicción
if st.button("Predecir"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    st.write(f"La predicción es: {prediction[0]}")