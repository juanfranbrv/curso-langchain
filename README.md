# Curso de LangChain

¡Bienvenido/a al repositorio de nuestro **Curso de LangChain**! En este espacio encontrarás todos los recursos necesarios para dominar los fundamentos, las capacidades intermedias y las funcionalidades avanzadas de LangChain, a través de notebooks **Google Colab** organizados de forma progresiva.

---

## Tabla de Contenidos

1. [Descripción del Curso](#descripción-del-curso)
2. [Estructura del Contenido](#estructura-del-contenido)
   - [Serie 1: Básico](#serie-1-básico)
   - [Serie-2: Intermedio](#serie-2-intermedio)
   - [Serie-3: Avanzado](#serie-3-avanzado)
3. [Requisitos Previos](#requisitos-previos)
4. [Cómo Usar Este Repositorio](#cómo-usar-este-repositorio)
5. [Cómo Contribuir](#cómo-contribuir)
6. [Licencia](#licencia)

---

## Descripción del Curso

Este curso está diseñado para guiarte desde los **fundamentos de LangChain** hasta la **creación de aplicaciones avanzadas** en producción. El contenido está dividido en **tres niveles**, cada uno compuesto por múltiples notebooks que cubren los aspectos más relevantes de la librería y sus aplicaciones. El enfoque es práctico, con ejemplos y ejercicios que te permitirán asimilar los conceptos paso a paso.

---

## Estructura del Contenido (Work in progress!!)

### Serie 1: Básico
En esta primera serie, sentarás las bases para entender LangChain y aprenderás:
- ¿ Que es Langchain ? Configuración inicial del entorno [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juanfranbrv/curso-langchain/blob/main/langchain-01.ipynb#scrollTo=n4sbGgy_lcrD)
- Primeros Chains y uso básico de prompts
- Integración con herramientas y agentes sencillos

**Objetivos**:
- Familiarizarte con la sintaxis y los conceptos esenciales.
- Desarrollar ejemplos básicos de manipulación de prompts y cadenas simples.

### Serie 2: Intermedio
Una vez domines los fundamentos, pasarás a la siguiente serie, donde profundizarás en:
- Memoria conversacional para mantener el contexto
- Uso de vectores, embeddings y bases de datos vectoriales
- Construcción de sistemas de Pregunta-Respuesta (Q&A) con recuperación de contexto
- Carga y procesamiento de distintos tipos de documentos

**Objetivos**:
- Aplicar técnicas de **retrieval** y **embedding** para mejorar la efectividad de los sistemas conversacionales.
- Manipular distintos formatos de archivos y documentos de forma dinámica.

### Serie 3: Avanzado
En esta última serie, integraremos todas las funcionalidades vistas y exploraremos temas complejos:
- Combinar memoria, recuperación de información y agentes avanzados
- Uso de cadenas de razonamiento (Chain-of-Thought)
- Integración con APIs externas y chatbots multimodales
- Optimización y despliegue en producción
- Proyecto final integrador

**Objetivos**:
- Desarrollar aplicaciones completas, con múltiples componentes de LangChain.
- Aprender a optimizar el rendimiento y a desplegar proyectos en entornos de producción.

---

## Requisitos Previos
- Conocimientos básicos de Python.
- Familiaridad con Google Colab (o un entorno de Jupyter Notebooks).
- Cuenta de Google para ejecutar los notebooks en Google Colab (opcional, pero recomendado).

Además, para las secciones más avanzadas, se sugiere:
- Experiencia con APIs REST.
- Entendimiento básico de conceptos de **Data Science** y **Machine Learning** (deseable).

---

## Cómo Usar Este Repositorio
1. **Clona o descarga** este repositorio en tu ordenador o abre los notebooks directamente en Google Colab.

### Clonar el Repositorio desde el Terminal

Sigue estos pasos para clonar el repositorio en tu ordenador:

1.  **Abre tu terminal** (Linux/Mac) o **Git Bash** (Windows).
    
2.  Navega al directorio donde deseas clonar el repositorio usando el comando `cd`. Por ejemplo:
    
      cd ruta/de/tu/directorio
    
3.  Ejecuta el siguiente comando para clonar el repositorio:
    
    git clone https://github.com/juanfranbrv/curso-langchain.git
    
4.  Una vez completado el proceso, navega al directorio del repositorio clonado:
    
    cd curso-langchain
    
5.  ¡Listo! Ahora tienes una copia local del repositorio en tu ordenador.
    

### Descargar el Repositorio como Archivo ZIP

Si prefieres descargar el repositorio como un archivo ZIP:

1.  Visita la página del repositorio: [https://github.com/juanfranbrv/curso-langchain](https://github.com/juanfranbrv/curso-langchain).
    
2.  Haz clic en el botón verde **"Code"** en la parte superior derecha de la página.
    
3.  Selecciona **"Download ZIP"** en el menú desplegable.
    
4.  Una vez descargado, extrae el archivo ZIP en tu directorio preferido.





2. Cada serie cuenta con sus propios subdirectorios que contienen los notebooks (Colabs) numerados en orden progresivo.
3. **Lee la descripción** al inicio de cada notebook para entender los objetivos, requisitos y pasos a seguir.
4. **Ejecuta los ejemplos** propuestos y experimenta con tus propios casos de uso.
5. Cuando concluyas un nivel, pasa al siguiente para seguir aprendiendo de forma escalonada.

---

## Cómo Contribuir
¡Las contribuciones son bienvenidas! Si deseas mejorar este curso o corregir algún error:

1. Realiza un **fork** de este repositorio.
2. Crea una rama con tu propuesta de mejora: `git checkout -b fix-o-nueva-funcionalidad`.
3. Haz un **commit** con tus cambios y justifícalos en tu mensaje de commit: `git commit -m 'Breve descripción de lo que has mejorado'`.
4. Haz un **push** a tu rama: `git push origin fix-o-nueva-funcionalidad`.
5. Crea un **pull request** a la rama principal de este repositorio.

---

## Licencia
Este proyecto se distribuye bajo la licencia [MIT](LICENSE). Puedes usar, modificar y distribuir este contenido libremente, dando crédito a los autores originales.

---

¡Esperamos que este curso te resulte útil y que aprendas todo lo necesario para construir aplicaciones poderosas con LangChain! Si tienes alguna duda o sugerencia, no dudes en crear un **issue** o dejarnos tus comentarios.

**¡Feliz aprendizaje!**

