"""
Esta aplicacion recibe una URL de una web de noticias y
la scrapea para obtener un titular un texto que resume la noticia

"""
from decouple import config
import requests
from bs4 import BeautifulSoup
from rich import print as rprint

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI


def scrape_news(url):
    # Hacer la solicitud HTTP
    response = requests.get(url)

    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, "html.parser")

    return soup.get_text()


# ═════════════════════════════════════════════
#  PROGRAMA PRINCIPAL
# ═════════════════════════════════════════════

OPENAI_API_KEY = config("OPENAI_API_KEY")


url = "https://elpais.com/economia/2025-02-06/amazon-preve-frenar-su-crecimiento-tras-batir-record-de-ventas-con-638000-millones-de-dolares.html"

texto_extraido = scrape_news(url)

# ═════════════════════════════════════════════
#  SCRAPEAMOS LA NOTICIA
# ═════════════════════════════════════════════

# Configuración de LangChain
template_sistema = """
Eres un asistente experto en procesamiento de lenguaje natural. Tu tarea es analizar el contenido de una noticia proporcionada por el usuario y generar dos cosas:
1. Un **titular** claro y conciso que capture la esencia de la noticia.
2. Un **resumen extenso** que incluya los detalles más importantes de la noticia, manteniendo un tono neutral y objetivo.
3. Importante: Debes descartar e ignorar cualquier texto o contenido que no tenga que ver con la noticia principal.

Instrucciones:
- El titular debe ser breve (máximo 25 palabras) y directo.
- El resumen debe ser extenso (al menos 150 palabras) y cubrir los puntos clave de la noticia.
- Mantén un lenguaje formal y evita añadir información que no esté en el texto proporcionado.
"""

template_usuario = """
A continuación te proporciono el contenido de una noticia. Por favor, genera un titular y un resumen extenso basado en la información proporcionada.

Contenido de la noticia:
{texto_extraido}

Por favor, genera:
1. Un titular claro y conciso.
2. Un resumen extenso que cubra los detalles más importantes.
"""

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", template_sistema),
        ("human", template_usuario),
    ]
)

llm_extractor = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)

prompt = chat_prompt_template.format(texto_extraido=texto_extraido)

texto_de_la_noticia= llm_extractor.invoke(prompt).content

rprint(f"[bold blue]TEXTO EXTRAIDO: NOTICIA =====================")
rprint(f"[blue]{texto_de_la_noticia}")

# ═════════════════════════════════════════════
#  AHORA GENERAMOS EL CLICKBAIT
# ═════════════════════════════════════════════

template_sistema = """
Eres un modelo de lenguaje experto en la creación de titulares y subtítulos de tipo clickbait. Tu tarea es analizar el texto completo de una noticia y generar, a partir de él, un titular llamativo y un subtítulo un poco más extenso que despierte la curiosidad del lector. El titular debe ser breve, impactante y provocativo, mientras que el subtítulo debe expandir la idea del titular con detalles intrigantes, sin distorsionar la información original de la noticia. Emplea técnicas de sensacionalismo y misterio para incentivar el clic, pero mantén siempre un vínculo claro con el contenido de la noticia.


1. **Titular**:
   - Debe ser breve (máximo 10-12 palabras).
   - Debe ser llamativo, sensacionalista y generar curiosidad.
   - Usa palabras emocionales o impactantes (por ejemplo: "impactante", "increíble", "sorprendente", "descubre", "esto cambiará todo").

2. **Subtitular**:
   - Debe ser un poco más extenso que el titular (máximo 20 palabras).
   - Sigue siendo intrigante y persuasivo.
   - Usa un tono emocional y asegúrate de mantener el interés del lector.

Ejemplo:
- Titular: "¡No vas a creer lo que hizo esta persona para salvar a su mascota!"
- Subtitular: "En un acto de valentía sin precedentes, un hombre arriesgó su vida para rescatar a su perro de un peligro inminente. ¡Descubre cómo lo logró!"

Recuerda: el objetivo es captar la atención del lector y persuadirlo a hacer clic en la noticia.
"""

template_usuario = """
A partir del siguiente texto de una noticia, crea un titular clickbait y un subtítulo un poco más extenso que capte la atención y despierte la curiosidad de los lectores:

Contenido de la noticia:
{texto_de_la_noticia}

Por favor, genera:
1. Un titular llamativo y sensacionalista.
2. Un subtitular que amplíe ligeramente el titular y mantenga el interés del lector.
"""

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", template_sistema),
        ("human", template_usuario),
    ]
)

llm_redactor = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0.9
)

prompt = chat_prompt_template.format(texto_de_la_noticia=texto_de_la_noticia)

texto_clickbait= llm_redactor.invoke(prompt).content

rprint(f"\n[bold green]Noticia clickbait =====================")
rprint(f"[green]{texto_clickbait}")

