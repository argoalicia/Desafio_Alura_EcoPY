import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 1. Cargar variables de entorno (API Key de OpenAI)
load_dotenv()

# Configuración de la página en Streamlit
st.set_page_config(
    page_title="Asistente Virtual - EcoPY",
    page_icon="♻️",
    layout="centered"
)

st.title("♻️ Asistente Virtual EcoPY")
st.caption("Consulta información sobre las políticas, tarifas y calendarios del servicio.")

PDF_PATH = "politica_ecopy.pdf"

# 2. Función para procesar e indexar el documento PDF
@st.cache_resource
def inicializar_sistema_rag(pdf_path):
    if not os.path.exists(pdf_path):
        st.error(f"El archivo {pdf_path} no existe en la carpeta del proyecto.")
        return None

    # a. Cargar el PDF
    loader = PyPDFLoader(pdf_path)
    documentos = loader.load()

    # b. Dividir el documento en fragmentos
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    fragmentos = text_splitter.split_documents(documentos)

    # c. Crear embeddings e indexar en FAISS
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vectorstore = FAISS.from_documents(
        fragmentos,
        embeddings
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    # d. Configurar modelo Gemini
    llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.2
    )

    system_prompt = (
        "Eres un asistente virtual formal y servicial de EcoPY.\n"
        "Responde utilizando únicamente el contexto del documento.\n"
        "Si la información no está en el documento, indica que no la encuentras.\n\n"
        "Contexto:\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # e. Crear cadena RAG
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
# Inicializar el motor RAG
rag_chain = inicializar_sistema_rag(PDF_PATH)

# 3. Gestor de historial de chat en Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy el asistente de EcoPY. ¿En qué puedo ayudarte hoy?"}
    ]

# Mostrar historial de mensajes
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 4. Interacción con el usuario
if prompt_usuario := st.chat_input("Escribe tu consulta aquí (ej: ¿Cuál es el costo del servicio?)..."):

    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt_usuario})
    st.chat_message("user").write(prompt_usuario)

    if rag_chain is not None:
        with st.spinner("Buscando respuesta en las políticas..."):
            try:
                # Generar respuesta usando la cadena de LangChain
                texto_respuesta = rag_chain.invoke(prompt_usuario)

            except Exception as e:
                texto_respuesta = (
                    "Lo siento, ocurrió un problema al generar la respuesta. "
                    "Por favor intenta nuevamente en unos segundos."
                )

                # El detalle queda en la consola de desarrollo
                print("ERROR AL CONSULTAR GEMINI/LANGCHAIN:", e)

        # Guardar y mostrar respuesta del asistente
        st.session_state.messages.append(
            {"role": "assistant", "content": texto_respuesta}
        )

        st.chat_message("assistant").write(texto_respuesta)