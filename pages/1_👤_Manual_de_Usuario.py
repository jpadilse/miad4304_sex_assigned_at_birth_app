import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Manual de Usuario", page_icon="👤")

# Título principal
st.title("👩 Predicción de Género por Nombre 👨")

# Introducción
st.write(
		"""
		Esta aplicación utiliza técnicas de aprendizaje profundo para predecir 
		el género más probable asociado a un nombre de forma rápida y precisa.
		"""
)

# Sección de características
st.header("✨ Características Principales")
st.write(
		"""
		- 🤖 Predicción de género basada en el nombre ingresado.
		- ✅ Indicación del nivel de confianza del modelo.
		- 📊 Análisis sencillo y eficiente.
		"""
)

# Sección de cómo usar
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

# Sección de detalles adicionales
st.header("🛠 Detalles Importantes")
st.write(
		"""
		- 🔒 Tu privacidad está protegida.
		- 🌐 Accesible desde cualquier dispositivo con conexión a Internet.
		- ⚠️ Las predicciones son aproximaciones basadas en datos históricos y patrones comunes.
		"""
)