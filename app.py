import streamlit as st

st.set_page_config(page_title="Quinielas de Coleo", layout="centered")

st.title("🏆 Plataforma de Quinielas de Coleo")
st.subheader("Registra tu cuadro oficial")

# Formulario básico
with st.form("formulario_cuadro"):
    nombre = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("Número de WhatsApp")
    
    st.write("Selecciona tus 4 coleadores:")
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    boton_enviar = st.form_submit_button("Enviar Cuadro")

if boton_enviar:
    st.success(f"¡Gracias {nombre}! Hemos recibido tu cuadro.")
    st.write("Por favor, confirma tu pago por WhatsApp para validar tu registro.")
