import streamlit as st

# Set page configuration
st.set_page_config(page_title="Manual de Instalación", page_icon="💻")

# Page title
st.title("👩Predicción de género por nombre👨")
st.header("📖 Manual de Instalación 📖")

# Introduction
st.subheader("📗 Introducción")
st.write(
		"""
		Este manual detalla los pasos necesarios para instalar y ejecutar un proyecto de predicción de género por nombres basado en Python y Streamlit. 
		El proyecto está diseñado para ser ejecutado en un entorno AWS. Este documento también incluye soluciones a problemas comunes y configuraciones específicas 
		para garantizar un correcto despliegue.
		"""
)

# AWS Preparation
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

st.write("#### Pasos para configurar la instancia:")
st.markdown(
		"""
		1. Accede a la consola de AWS, selecciona *Lanzar Instancia* y elige Ubuntu como sistema operativo.
		2. Configura el tipo de instancia como **t2.small** o superior.
		3. Asigna **20 GB** de almacenamiento.
		4. Agrega reglas para permitir el tráfico en los puertos mencionados:
		   - **22**: Acceso SSH desde tu IP.
		   - **8501**: Acceso HTTP desde tu IP pública (o abierta temporalmente).
		5. Usa la llave SSH descargada al crear la instancia. Conéctate desde la terminal con el siguiente comando:
		```bash
		ssh -i llave.pem ubuntu@<IP>
		```
		6. Una vez dentro de la instancia, actualiza los paquetes:
		```bash
		sudo apt update && sudo apt upgrade -y
		```
		"""
)

# Installation steps
st.subheader("📙 Instalación")

st.markdown(
		"""
		1. Clona el proyecto desde GitHub y accede al directorio:
		```bash
		git clone https://github.com/jpadilse/miad4304_sex_assigned_at_birth_ds.git
		```
	
		2. Accede a la carpeta del proyecto:
		```bash
		cd miad4304_sex_assigned_at_birth_ds
		```
	
		3. Crea un entorno virtual y actívalo:
		```bash
		python3 -m venv venv
		source venv/bin/activate
		```
	
		4. Instala los paquetes listados en el archivo `requirements.txt`:
		```bash
		pip install -r requirements.txt
		```
	
		5. Inicia la aplicación del proyecto con Streamlit:
		```bash
		streamlit run app.py --server.port 8501
		```
	
		6. Abre tu navegador y accede a la URL correspondiente:
		   - **Localmente**: [http://localhost:8501](http://localhost:8501).
		   - **En AWS**: [http://<IP-pública-de-tu-instancia>:8501](http://<IP-pública-de-tu-instancia>:8501).
		"""
)

# FAQs
st.subheader("🎯 Preguntas Frecuentes")

with st.expander("❓ ¿Dónde puedo comunicarme si tengo algún inconveniente?"):
	st.write(
			"""
			Puedes comunicarte con alguno de los miembros del equipo responsable del desarrollo de la herramienta, enviando un correo a:
	
			- 😊 j.padillas@uniandes.edu.co
			- 😊 ek.diaz@uniandes.edu.co
			- 😊 a.quinoneso@uniandes.edu.co
			- 😊 m.gonzalezc@uniandes.edu.co
			"""
	)
