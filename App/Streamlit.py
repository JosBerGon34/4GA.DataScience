import streamlit as st
import joblib
import numpy as np
import os
import xgboost as xgb

# Función principal de la aplicación
def app():
    # Nombres de las variables predictoras (CORREGIDO)
    predict_vars = ['lw_pnd', 'ppl', 'imbgeco', 'cntgrp_fc', 'rel3fc', 'pplhlp', 'pplfair', 'ppltrst', 'stfdem', 'stfeco', 'stfgov', 'imwbcnt', 'trstep', 'trstlgl', 'trstplc', 'trstplt', 'trstprl', 'trstprt', 'trtsci_pnd']

    # Nombres de las variables objetivo y modelos cargados
    target_vars = ['happy', 'lr4d', 'polintr']
    models = {
        'happy': joblib.load("C:/Users/Josue/4GA.Datascience/4GA.DataScience/App/Happy.pkl"), 
        'lr4d': joblib.load("C:/Users/Josue/4GA.Datascience/4GA.DataScience/App/lr4d.pkl"), 
        'polintr': joblib.load("C:/Users/Josue/4GA.Datascience/4GA.DataScience/App/polintr.pkl"), 
    }

    st.title("Predicciones de Variables Objetivo")

    # Valores iniciales de las barras deslizantes
    initial_values = {var: 0 for var in predict_vars}

    # Inicializar st.session_state si no existe
    if 'initialized' not in st.session_state:
        for var, value in initial_values.items():
            st.session_state[var] = value
        st.session_state['initialized'] = True

    # Función para restablecer los valores
    def reset_values():
        for var, value in initial_values.items():
            st.session_state[var] = value
        st.experimental_rerun()

    # Barras deslizantes para las variables predictoras
    sliders = {}
    for var in predict_vars:
        if var == 'lw_pnd':
            sliders[var] = st.slider(var, min_value=1, max_value=5, step=1, key=var, value=st.session_state[var])
        elif var == 'cntgrp_fc' or var == 'rel3fc':
            sliders[var] = st.slider(var, min_value=0, max_value=2, step=1, key=var, value=st.session_state[var])
        else:
            sliders[var] = st.slider(var, min_value=0, max_value=10, step=1, key=var, value=st.session_state[var])

    # Botón de predicción
    if st.button("Predecir"):
        input_data = np.array([[sliders[var] for var in predict_vars]])
        print(input_data.shape)
        for target_var in target_vars:
            prediction = models[target_var].predict(input_data)[0]
            st.write(f"Predicción para {target_var}: {prediction}")

    # Botón de reset
    if st.button("Resetear"):
        reset_values()

# Llamada a la función principal
if __name__ == "__main__":
    app()