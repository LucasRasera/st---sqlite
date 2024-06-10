import streamlit as st
import sqlite3
import pandas as pd

st.write("Teste do role com sqlite")

def criar_formulario():
    with st.form('Teste'):
        nome = st.text_input('nome')
        idade = st.number_input('idade')
        enviar = st.form_submit_button('Enviar')

        if enviar:
            salvar(nome, idade) 

def salvar(nome, idade):
    conn = sqlite3.connect('form.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS  Teste (
                NOME TEXT(20),
                IDADE INT
            )
        """
    )

    cursor.execute("INSERT INTO Teste VALUES (?, ?)", (nome, idade))
    conn.commit()
    conn.close()
    st.success("Deu certo")

def visualizar():
    conn = sqlite3.connect('form.db', check_same_thread=False)
    query = "SELECT * FROM Teste"
    df = pd.read_sql_query(query, conn)
    return df

criar_formulario()
st.dataframe(visualizar())