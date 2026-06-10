# ARCHIVO_DE_CONTEXTO.md

Este documento sirve como la memoria del proyecto para el desarrollo frontend y maquetación de la interfaz de la **Mediateca Digital / Repositorio de Acceso Abierto** del proyecto PAPIIT para la **Universidad Nacional Autónoma de México (UNAM)** y el **Instituto de Investigaciones Bibliográficas y de la Información (IIBI)**.

---

## 1. Identidad Institucional y Estilo Visual

* **Institución:** UNAM / IIBI.
* **Enfoque de Diseño:** Rigurosamente académico, formal, simétrico, limpio y de alto perfil.
* **Paleta de Colores:**
  * **Azul Primario (Institucional):** `#0a3663` (Encabezados, banners, secciones principales).
  * **Azul Secundario (Acentos/Interactivos):** `#0d47a1` o `#1565c0` (Botones, enlaces, destacados).
  * **Neutros:** Fondos limpios (`#ffffff`, `#f8f9fa`) y textos en gris oscuro (`#212529`).

---

## 2. Infraestructura Técnica

* **CMS de Destino:** Omeka S v4.2.0.
* **Framework CSS:** Bootstrap v5.3.8 (alojado localmente de forma global en el servidor).
* **Iconografía:** Bootstrap Icons v1.11.3 (alojado localmente en el servidor).
* **Control de Layout:** Control total de la maquetación a través de bloques de código personalizados (independientes de las plantillas nativas de los temas de Omeka S).

---

## 3. Objetivos y Naturaleza del Repositorio PAPIIT

* **¿Qué es el PAPIIT?**  
  El Programa de Apoyo a Proyectos de Investigación e Innovación Tecnológica (PAPIIT) es el fondo institucional más importante de la UNAM. Financia proyectos de investigación científica, humanística y tecnológica dentro de la universidad, potenciando al IIBI para generar nuevo conocimiento y herramientas especializadas.
* **Beneficios Clave para el Usuario Final (Enfoque de Diseño de Contenidos):**
  1. **Democratización del Conocimiento (Acceso Abierto):** Permite la consulta y descarga gratuita de libros, artículos y manuscritos del IIBI, eliminando barreras de pago.
  2. **Preservación de la Memoria Bibliográfica:** Salvaguarda a largo plazo de documentos históricos digitalizados bajo el estándar internacional de metadatos **Dublin Core**.
  3. **Optimización de la Consulta:** Centralización de recursos multimedia, iconográficos y textuales en una interfaz unificada, responsiva y ágil para facilitar el descubrimiento de información científica.

---

## 4. Restricciones Críticas de Código (Inyección en Omeka S)

Para evitar rechazos, deformaciones o eliminación de código por parte del editor HTML y del motor de renderizado de Omeka S, se deben seguir estrictamente estas reglas:

1. **Prohibido Generar Textos de Test o Casos de Prueba:**  
   No incluir scripts de testing, bloques HTML de demostración redundantes ni explicaciones extensas sobre cómo probar el código. Se entrega exclusivamente la estructura final solicitada.
   
2. **Cero Etiquetas Estructurales Globales:**  
   Está prohibido incluir `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, o llamadas externas a archivos `<link>` y `<script>`. La maquetación debe iniciar directamente con los contenedores de Bootstrap (ej. `<div class="container py-5">`, `<div class="row">`, etc.).
   
3. **Regla de Iconos Anti-Borrado (Crucial):**  
   El editor HTML de Omeka S purga y elimina las etiquetas de iconos vacías (como `<i class="bi bi-search"></i>`). Para evitar esto, cada etiqueta de icono debe incluir obligatoriamente un espacio invisible `&nbsp;` en su interior.  
   * *Ejemplo correcto:* `<i class="bi bi-search">&nbsp;</i>`
   
4. **Estilos Inline Permitidos:**  
   Para detalles minuciosos como degradados personalizados, sombras específicas y micro-ajustes de posicionamiento, se deben inyectar directamente mediante el atributo `style="..."` de forma limpia.

5. **Estructura Semántica:**  
   El código debe entregarse estructurado semánticamente, bien indentado y con comentarios HTML cortos (`<!-- ... -->`) para facilitar su mantenimiento directo en el CMS.

---

## 5. Historial y Estructura del Home (Mediateca Pública)

La página de inicio maquetada en `home_layout.html` se reestructuró con un enfoque centrado en la ciudadanía y el investigador, organizada en las siguientes secciones secuenciales:

1. **Hero Banner Principal:**  
   De orientación institucional con título, descripción enfocada en la consulta pública y libre de buscador integrado (para no interferir con el motor de búsqueda global nativo del CMS Omeka S).
2. **Indicadores de Acceso Abierto (Métricas):**  
   *Actualmente comentados en el código HTML de desarrollo.* Diseñados para mostrar de manera visual la escala de recursos (4,500+), colecciones (25), uso de Dublin Core y el 100% de Acceso Abierto.
3. **Sección Informativa PAPIIT (Conoce el Proyecto):**  
   Sección introductoria explicativa y de redacción amigable, describiendo el impacto social del financiamiento UNAM y la labor del IIBI mediante 4 pilares:
   * Conocimiento libre y sin costo.
   * Protección del patrimonio histórico.
   * Agilización en la búsqueda de información.
   * Rigor y respaldo académico de las investigaciones del IIBI.
4. **Sección Central de Colecciones y Herramientas (Dos Columnas):**  
   * **Columna Izquierda (Ancha):** Fondos Documentales y Colecciones (Producción Editorial PAPIIT, Fondo Antiguo y Documental, y Archivos Multimedia).
   * **Columna Derecha (Angosta):** Guía del Investigador (Accesos rápidos a normas de citación académica, búsqueda avanzada por Dublin Core y políticas de Creative Commons).
5. **Pie de Página Académico:**  
   Mención formal a la UNAM, al Instituto de Investigaciones Bibliográficas y de la Información, y la mención de desarrollo optimizado localmente en 2026.
