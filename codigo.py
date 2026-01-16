# stremlit_pesquisa
import streamlit as st 

def conversor():
    valores = []
    while True:
        valor = st.text_input("Insira as soicitações de serviço:", type="text")
        if valor == "":
            break
    valores.append(valor)
    print(" OR ".join(valores))

def front():
    st.set_page_config(page_title="CONVERSOR DE CARACTERES", layout="wide")
    st.write("FORMARTAR SS PARA PESQUISA NO OPER")
    st.text(conversor)

front()
