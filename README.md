# ♻️ EcoPY — Asistente Virtual (RAG Agent)

**Asistente de IA** con arquitectura **RAG** que responde preguntas sobre el servicio de recolección de residuos de **EcoPY** en **Mariano Roque Alonso (MRA)**.

Construido para el **challenge Oracle ONE / Alura** usando:

- **LangChain**
- **Gemini (Google AI)**
- **FAISS**
- **Streamlit**

---

## 🚀 ¿Qué hace este proyecto?

Este agente:

1. **Carga y procesa** el documento oficial de políticas (`politica_ecopy.pdf`) usando `PyPDFLoader`.
2. **Segmenta** el texto en *chunks* y crea un índice vectorial con **FAISS**.
3. Genera **respuestas basadas únicamente** en el contenido del PDF (modelo `gemini-flash-latest`).
4. Ofrece una **interfaz web** tipo chatbot desarrollada con **Streamlit**.
5. Está preparado para **despliegue público** en **Streamlit Community Cloud**.

## 🚀 Demo en vivo

Puedes probar la aplicación desplegada en Streamlit:

👉 [Abrir aplicación](https://desafioaluraecopy-eudutae9wr8fmvrzmcqwmw.streamlit.app/)

---

## ✨ Características principales

- 📄 **Procesamiento automático de documentos PDF**
- 🔍 **Búsqueda semántica vectorial**
- 🤖 **Respuestas con RAG** (con contexto del PDF)
- 💬 **Chatbot interactivo** con Streamlit
- ☁️ **Deploy público** listo para Streamlit Community Cloud

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python 3.10+
- **Web/App:** Streamlit
- **Framework IA:** LangChain (LangChain Community / LangChain Google GenAI)
- **Vector DB:** FAISS
- **Modelos:**
  - **Embeddings:** `text-embedding-001`
  - **LLM:** `gemini-flash-latest`
- **PDF Parsing:** `PyPDF`

---

## 📂 Estructura del proyecto

```text
Desafio_Alura_EcoPY/
│
├── .env                       # Variables de entorno (GOOGLE_API_KEY)
├── .gitignore                 # Archivos e historial ignorados por Git
├── README.md                 # Documentación del proyecto
├── requirements.txt          # Dependencias del proyecto
├── politica_ecopy.pdf        # Documento base de políticas
└── app.py                     # Aplicación principal de Streamlit

⚙️ Instalación y Configuración Local
1. Clonar el repositorio
Bash
git clone git@github.com:AliciaArgo/Desafio_Alura_EcoPY.git
cd Desafio_Alura_EcoPY
2. Crear y activar un entorno virtual
PowerShell
python -m venv venv
.\venv\Scripts\activate
3. Instalar dependencias
Bash
pip install -r requirements.txt
4. Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto y agrega tu API Key de Google AI Studio:

Fragmento de código
GOOGLE_API_KEY=tu_google_api_key_aqui
🚀 Ejecución de la Aplicación
Para iniciar la interfaz de Streamlit localmente, ejecuta:

Bash
streamlit run app.py
Abre tu navegador en http://localhost:8501.

💬 Preguntas de Ejemplo para Probar
¿Cuál es el costo del servicio por recolección?
<img width="1577" height="955" alt="image" src="https://github.com/user-attachments/assets/a4e20f05-38d0-4b8e-8266-89531681178f" />

¿Cuáles son los días y horarios para residuos reciclables?
<img width="1507" height="967" alt="image" src="https://github.com/user-attachments/assets/7c91475c-c314-45e8-8982-8e6cfba1bff2" />

¿Qué barrios están cubiertos por el servicio?

¿A qué número puedo realizar un reclamo?

🌐 Despliegue en Streamlit Community Cloud
Ingresa a share.streamlit.io.

Conecta tu cuenta de GitHub e importa este repositorio (AliciaArgo/Desafio_Alura_EcoPY).

En Advanced Settings > Secrets, configura la variable de entorno:

Ini, TOML
GOOGLE_API_KEY = "tu_google_api_key_aqui"
Haz clic en Deploy!.


---

### Paso 2: Subir el `README.md` y tus archivos a GitHub

Abre tu terminal en `C:\Desafio_Alura_EcoPY` y ejecuta los comandos para hacer `commit` y `push`:

```powershell
# 1. Agregar los archivos al área de preparación
git add .

# 2. Guardar el estado con un mensaje de commit
git commit -m "docs: Agrega README.md con la documentación completa del proyecto"

# 3. Subir los cambios a GitHub por SSH
git push -u origin main
