import streamlit as st
import joblib
import numpy as np
import os


def app():
    
    predict_vars = ['lw_pnd', 'ppl', 'imbgeco', 'cntgrp_fc', 'rel3fc', 'pplhlp', 'pplfair', 'ppltrst', 
                    'stfdem', 'stfeco', 'stfgov', 'imwbcnt', 'trstep', 'trstlgl', 'trstplc', 'trstplt', 'trstprl', 
                    'trstprt', 'trtsci_pnd']

   
    target_vars = ['happyfc', 'lr4d', 'polintr']
    models = {
        'happyfc': joblib.load("C:/Users/Josue/4GA.Datascience/4GA.DataScience/App/happy.pkl"), 
        'lr4d': joblib.load("C:/Users/Josue/4GA.Datascience/4GA.DataScience/App/lr4d.pkl"), 
        'polintr': joblib.load("C:/Users/Josue/4GA.Datascience/4GA.DataScience/App/polintr.pkl"), 
    }

    st.title("Predicciones de Variables Objetivo")

   
    initial_values = {var: 0 for var in predict_vars}

    
    if 'initialized' not in st.session_state:
        for var, value in initial_values.items():
            st.session_state[var] = value
        st.session_state['initialized'] = True

   
    def reset_values():
        for var, value in initial_values.items():
            st.session_state[var] = value
        st.experimental_rerun()

    
    sliders = {}
    for var in predict_vars:
        if var == 'lw_pnd':
            sliders[var] = st.slider(var, min_value=1, max_value=5, step=1, key=var, value=st.session_state[var])
        elif var == 'cntgrp_fc' or var == 'rel3fc':
            sliders[var] = st.slider(var, min_value=0, max_value=2, step=1, key=var, value=st.session_state[var])
        else:
            sliders[var] = st.slider(var, min_value=0, max_value=10, step=1, key=var, value=st.session_state[var])

    
    if st.button("Predecir"):
        input_data = np.array([[sliders[var] for var in predict_vars]])

        for target_var in target_vars:
            prediction = models[target_var].predict(input_data)[0]
        
    
    if st.button("Resetear"):
        reset_values()


if __name__ == "__main__":
    app()