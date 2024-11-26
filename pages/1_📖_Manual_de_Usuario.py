import streamlit as st

# Set page configuration
st.set_page_config(page_title="Manual de Usuario", page_icon="👩‍💻")

def render_user_manual():
	"""
	Render the user manual page with Streamlit layout and styling.
	"""
	# Main title
	st.title("👩 Predicción de Género por Nombre 👨")

	# Introduction text
	st.write(
			"""
			🎉 **Bienvenido** a nuestra herramienta de predicción de género por nombre. 
			Esta aplicación utiliza técnicas de aprendizaje profundo para predecir 
			el género más probable asociado a un nombre.
			"""
	)

	# Features section
	st.header("✨ Características Principales")
	st.write(
			"""
			- 🤖 Predicción de género basada en el nombre ingresado.
			- ✅ Nivel de confianza del modelo.
			- 📊 Análisis rápido y preciso.
			"""
	)

	# How to use section
	st.header("🚀 Cómo Usar")
	st.write(
			"""
			1. **Ingresa un Nombre**:
			   - Escribe un nombre en el campo de texto.
			   - Puede ser un nombre simple o compuesto.
	
			2. **Obtén el Resultado**:
			   - Verás el género predicho: 👩 (Mujer) o 👨 (Hombre).
			   - Un porcentaje de confianza indicará la precisión de la predicción.
	
			3. **Ejemplo**:
			   - Nombre: "Ana Maria"
			   - Resultado: 👩 Mujer
			   - Confianza: 99.1%
			"""
	)

	# Additional details section
	st.header("🛠 Detalles Importantes")
	st.write(
			"""
			- 🔒 Tu privacidad está protegida.
			- 🌐 Accesible desde cualquier dispositivo.
			- ⚠️ Las predicciones son aproximaciones basadas en datos históricos.
			"""
	)

	# FAQ section
	st.header("🎯 Preguntas Frecuentes")

	with st.expander("❓ ¿Cómo funciona el modelo?"):
		st.write(
				"""
				- Análisis de patrones de letras en nombres.
				- Comparación con una base de datos extensa.
				- Predicción estadística basada en machine learning.
				"""
		)

	with st.expander("❓ Contacto en caso de dudas"):
		st.write(
				"""
				Contáctanos si tienes preguntas:
				- j.padillas@uniandes.edu.co
				- ek.diaz@uniandes.edu.co
				- a.quinoneso@uniandes.edu.co
				- m.gonzalezc@uniandes.edu.co
				"""
		)

# Render the user manual
if __name__ == "__main__":
	render_user_manual()