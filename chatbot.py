import streamlit as st
from decouple import config

from langchain.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from langchain_openai import ChatOpenAI

st.set_page_config(
    page_title="ChatBot", page_icon="🤖", layout="wide", initial_sidebar_state="auto"
)



st.header(f"ChatBot experimental")

# ==================
# Configuración del modelo y plantillas de prompts
llm = ChatOpenAI(
    openai_api_key=config('OPENAI_API_KEY'),
    model_name="gpt-4o-mini",
    temperature=0.7
)

system_template = """Eres una calabaza parlante llamada Pepita. 
Responde de manera amigable, divertida y con un toque de humor vegetal.
Usa emojis ocasionalmente y mantén las respuestas breves.
Idioma: español\n"""
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{mensaje_usuario}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

# ==================



# Si la lista de mensajes no existe sn session.state, la inaurguramos
# Cada elemento de la lista de mensajes es un diccionario con role, mensaje y avatar
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Holi, soy Pepita la calabaza. ¿ En que puedo ayudarte hoy ?", "avatar": "🎃"}
    ]

# Renderizar el historial de mensajes
# Con un bucle recorremos la lista de mensajes y los pintamos con st_chat
for mensaje in st.session_state.messages:
    with st.chat_message(mensaje["role"], avatar=mensaje.get("avatar", "")):
        st.write(mensaje["content"])


# Pintamos la caja para el input
prompt_usuario = st.chat_input("Escribe aqui tu mensaje para la calabaza...")

# Si se ha escrito algo
if prompt_usuario:
    st.session_state.messages.append({"role": "user", "content": prompt_usuario, "avatar": "🧑🏻"})
    # Por el modo de ejecucion de Streamlit hay que pintar la respuesta ahora
    # El bucle no es responsable de renderizar el mensaje del usuario inmediatamente después de su entrada, 
    # ya que Streamlit ya habría pasado por esa parte del código antes de que el mensaje se añadiera al estado.
    with st.chat_message("user", avatar="🧑🏻"):
        st.write(prompt_usuario)

     # Generar respuesta del asistente
    with st.spinner("La calabaza está pensando..."):
        # Formatear y enviar el prompt
        formatted_messages = chat_prompt.format_messages(
            mensaje_usuario=prompt_usuario
        )
        respuesta = llm.invoke(formatted_messages)
        
    # Mostrar y almacenar respuesta
    with st.chat_message("assistant", avatar="🎃"):
        st.write(respuesta.content)
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": respuesta.content,
        "avatar": "🎃"
    })



