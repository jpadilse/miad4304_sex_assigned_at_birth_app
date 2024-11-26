import streamlit as st

# Set page configuration
st.set_page_config(page_title="Manual de Usuario", page_icon="👩‍💻")

def render_user_manual():
	"""
	Render the user manual page with Streamlit layout and styling
	"""
	# Main title
	st.markdown("# 👩 Predicción de Género por Nombre 👨")

	# Sidebar header
	st.sidebar.header("📖 Manual de Usuario")

	# Introduction text
	st.write(
			"""
			🎉 Bienvenido a nuestra herramienta de predicción de género por nombre. 
			Esta aplicación utiliza técnicas de aprendizaje profundo para predecir 
			el género más probable asociado a un nombre.
			"""
	)

	st.sidebar.header("📖 PRUEBA")
	# Detailed sections
	st.markdown("## ✨ Características Principales")
	st.markdown("""
    - 🧑‍💻 Predicción de género basada en el nombre ingresado
    - ✅ Nivel de confianza del modelo
    - 📊 Análisis rápido y preciso
    """)

	st.markdown("## 🚀 Cómo Usar")
	st.markdown("""
    1. **Ingresa un Nombre**
       - Escribe un nombre en el campo de texto
       - Puede ser un nombre simple o compuesto
    
    2. **Obtén el Resultado**
       - Verás el género predicho: 👩 (Mujer) o 👨 (Hombre)
       - Un porcentaje de confianza te indicará la precisión de la predicción
    
    3. **Ejemplo**
       - Nombre: "Ana Maria"
       - Resultado: 👩 Mujer
       - Confianza: 99.1%
    """)

	st.markdown("## 🛠 Detalles Importantes")
	st.markdown("""
    - 🔒 Tu privacidad está protegida
    - 🌐 Accesible desde cualquier dispositivo
    - ⚠️ Las predicciones son aproximaciones basadas en datos históricos
    """)

	st.markdown("## 🎯 Preguntas Frecuentes")

	with st.expander("❓ ¿Cómo funciona el modelo?"):
		st.write("""
        - Análisis de patrones de letras en nombres
        - Comparación con base de datos extensa
        - Predicción estadística basada en machine learning
        """)

	with st.expander("❓ Contacto en caso de dudas"):
		st.write("""
        Contáctanos si tienes preguntas:
        - j.padillas@uniandes.edu.co
        - ek.diaz@uniandes.edu.co
        - a.quinoneso@uniandes.edu.co
        - m.gonzalezc@uniandes.edu.co
        """)

# Render the user manual
render_user_manual()