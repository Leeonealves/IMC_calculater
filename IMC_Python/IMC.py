
import streamlit as st

st.title("Calculadora de IMC")

peso = st.number_input("Digite seu peso (kg):", min_value=1.0, format="%.2f")

altura = st.number_input("Digite sua altura (m):", min_value=0.5, format="%.2f")

if st.button("Calcular IMC"):
    if altura > 0:
        imc = peso / (altura ** 2)
        st.write(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            st.write("Classificação: Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            st.write("Classificação: Peso normal")
        elif 25 <= imc < 29.9:
            st.write("Classificação: Sobrepeso")
        else:
            st.write("Classificação: Obesidade")
    else:
        st.write("Por favor, insira uma altura válida.")