import streamlit as st
import sqlite3

conn = sqlite3.connect('form.db', check_same_thread=False)
cursor = conn.cursor()

st.write("Teste do role com sqlite")

def criar_formulario():
    with st.form('Teste'):
        nome = st.text_input('nome')
        idade = st.number_input('idade')
        enviar = st.form_submit_button('Enviar')

        if enviar:
            salvar(nome, idade) 

def salvar(nome, idade):
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

criar_formulario()