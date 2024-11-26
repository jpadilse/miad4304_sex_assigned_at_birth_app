import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Manual de Instalación", page_icon="💻")

# Título de la página
st.title("👩 Predicción de Género por Nombre 👨")
st.header("📖 Manual de Instalación")

# Introducción
st.subheader("📗 Introducción")
st.write(
		"""
		Este manual describe los pasos para instalar y ejecutar un proyecto de predicción de género por nombres usando Python y Streamlit 
    	en un entorno AWS.
		"""
)

# Preparación de AWS
st.subheader("📘 Preparación Instancia AWS")

st.write("Antes de iniciar, asegúrate de contar con:")
st.markdown(
		"""
		1. Una cuenta de AWS activa.
		2. Una instancia EC2 con las siguientes especificaciones:
		   - **AMI**: Ubuntu 20.04 LTS.
		   - **Tipo de instancia**: t2.small o superior.
		   - **Almacenamiento**: 20 GB de EBS (General Purpose SSD, gp2).
		   - **Grupo de Seguridad**: Configura la siguiente regla de tráfico:
			 - **Puerto 8501 (Streamlit)**: Para acceder al tablero web.
		"""
)

# Pasos de instalación
st.subheader("📙 Instalación")

st.markdown(
		"""
		1. Clonar el repositorio:
		   ```bash
		   git clone https://github.com/jpadilse/miad4304_sex_assigned_at_birth_app.git
		   cd miad4304_sex_assigned_at_birth_app
		   ```
		
		2. Crear un entorno virtual (opcional pero recomendado):
		   ```bash
		   python -m venv venv
		   source venv/bin/activate 
		   ```
		
		3. Instalar dependencias:
		   ```bash
		   pip install -r requirements.txt
		   ```
		
		4. Inicia la aplicación del proyecto con Streamlit:
		   ```bash
		   streamlit run streamlit_app.py --server.port 8501
		   ```
		
		5. Abre tu navegador y accede a la URL correspondiente:
		   - **Localmente**: [http://localhost:8501](http://localhost:8501).
		   - **Online**: [http://<IP-pública-de-tu-instancia>:8501](http://<IP-pública-de-tu-instancia>:8501).
		"""
)