import streamlit as st
# ... (tu configuración de conexión actual) ...

st.title("🏆 Registro de Quinielas")

with st.form("registro_cuadros"):
    participante = st.text_input("Nombre del Participante")
    whatsapp = st.text_input("WhatsApp")
    # Añade los campos para los coleadores
    c1 = st.text_input("Coleador 1")
    c2 = st.text_input("Coleador 2")
    c3 = st.text_input("Coleador 3")
    c4 = st.text_input("Coleador 4")
    
    enviar = st.form_submit_button("Guardar Cuadro")
    
    if enviar:
        # Aquí envías los datos a la hoja de Google Sheets
        hoja = client.open("BaseDatosColeo").worksheet("Cuadros")
        hoja.append_row([participante, whatsapp, c1, c2, c3, c4])
        st.success("¡Cuadro registrado correctamente!")
