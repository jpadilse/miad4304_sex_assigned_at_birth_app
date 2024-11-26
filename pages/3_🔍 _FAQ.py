import streamlit as st

# Configuración de la página
st.set_page_config(page_title="FAQ", page_icon="🔍")

# Título de la página
st.title("👩 Predicción de Género por Nombre 👨")
st.header("🎯 Preguntas Frecuentes")

# Preguntas frecuentes
faq_items = [
	{
		"question": "¿Cómo funciona el modelo?",
		"answer": """
        Este modelo utiliza redes neuronales para analizar patrones en los caracteres del nombre:
			- Analiza la secuencia de letras y patrones comunes en nombres
			- Compara con patrones aprendidos de miles de nombres etiquetados
			- Genera una predicción basada en similitudes estadísticas
			- La confianza indica qué tan seguro está el modelo de su predicción
        """
	},
	{
		"question": "¿Dónde puedo comunicarme si tengo algún inconveniente?",
		"answer": """
        Puedes comunicarte con alguno de los miembros del equipo responsable del desarrollo de la herramienta, enviando un correo a:

        - Juan Felipe Padilla Sepulveda (j.padillas@uniandes.edu.co)
        - Eva Karina Díaz Gavalo (ek.diaz@uniandes.edu.co)
        - Andres Quiñones Quiñones (a.quinoneso@uniandes.edu.co)
        - Mauricio González Caro (m.gonzalezc@uniandes.edu.co)
        """
	}
]

for item in faq_items:
	with st.expander(item["question"]):
		st.write(item["answer"])
