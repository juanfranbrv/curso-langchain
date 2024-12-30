## Practicando con ChatPromptTemplate en LangChain

#### Objetivo del Ejercicio

Crea un chatbot interactivo utilizando la biblioteca LangChain que actúe como tutor de idiomas. El chatbot debe configurarse con prompts dinámicos a través de ChatPromptTemplate, incluyendo un mensaje para el sistema que defina el rol del tutor (por ejemplo, ser paciente, motivador y corregir errores gramaticales) y un mensaje para el usuario que introduzca las interacciones del estudiante. Además, implementa el chatbot con al menos dos modelos de lenguaje diferentes, como uno de OpenAI (por ejemplo, gpt-4) y otro accesible en Groq (como Gemini), para comparar sus respuestas. Experimenta con variaciones en los prompts y analiza cómo estas afectan el comportamiento del chatbot y las respuestas de los modelos.

El objetivo de este ejercicio es aprender a trabajar con los **Prompt Templates** en LangChain, específicamente con `ChatPromptTemplate`, para diseñar interacciones dinámicas con modelos de lenguaje (LLMs). Además, se busca comparar el comportamiento de diferentes modelos de lenguaje y cómo varían sus respuestas según las plantillas de prompt que se utilicen.

#### Tareas

1. **Configuración Inicial**:
    
    - Configura tu entorno de trabajo con la librería LangChain.
    - Asegúrate de tener acceso a dos modelos de lenguaje diferentes, como OpenAI GPT y algún modelo disponible en **Groq** (por ejemplo, Gemini).
2. **Implementación del Código Base**:
    
    - Utiliza el código base proporcionado para crear un chatbot que sirva como tutor de idiomas.
    - Configura los prompts siguiendo el esquema definido:
        - Un prompt para el **sistema** que define el rol del tutor (por ejemplo, paciente y motivador).
        - Un prompt para el **usuario** que introduce los mensajes del estudiante.
3. **Prueba con Diferentes Modelos de LLM**:

    - Implementa el chatbot utilizando al menos dos modelos de LLM diferentes:
        - Un modelo de OpenAI, como `gpt-4`.
        - Un modelo accesible desde **Groq**, como Gemini Pro.
    - Compara las diferencias en las respuestas proporcionadas por cada modelo.

    Cuando tengas una version funcional, realmente solo tendras que hacer otra version casi identica, llamando al otro modelo.

4. **Experimentación con Variantes de Prompts**:
    
    - Modifica las plantillas de prompt (por ejemplo, cambia el tono del tutor, agrega instrucciones adicionales o elimina restricciones).
    - Observa cómo los cambios afectan las respuestas de los modelos.
    - Documenta tus observaciones: ¿Qué modelo responde mejor a cambios en el prompt? ¿Cómo afecta la temperatura al tono y detalle de las respuestas?
5. **Informe Final**:
    
    - Prepara un breve informe donde describas:
        - Las diferencias encontradas entre los modelos.
        - Cómo las modificaciones en los prompts afectan el comportamiento del chatbot.
        - Tus conclusiones sobre la utilidad de `ChatPromptTemplate` para diseñar interacciones efectivas.

#### Sugerencias

- **Aspectos Técnicos**:
    
    - Utiliza funciones para estructurar tu código y hacerlo más reutilizable.
    - Si tienes problemas de configuración con algún modelo, consulta la documentación oficial de LangChain o los recursos de Groq.
- **Evaluación del Ejercicio**:
    
    - No hay respuestas "correctas" o "incorrectas". La idea es que explores y documentes los cambios observados.



¡Buena suerte y diviértete explorando! 🚀