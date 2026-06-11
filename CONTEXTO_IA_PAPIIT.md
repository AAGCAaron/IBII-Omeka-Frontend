# CONTEXTO DE DESARROLLO FRONTEND: PROYECTO PAPIIT PARA OMEKA S
**Propósito de este archivo:** Este documento es una base de conocimiento diseñada para que cualquier asistente de Inteligencia Artificial (IA) pueda continuar el desarrollo del frontend de este proyecto en otra computadora, manteniendo la coherencia visual, técnica y estructural sin perder contexto.

---

## 1. Información General del Proyecto
* **Proyecto:** PAPIIT IG300724 "Comunidades digitales emergentes de creación de conocimiento".
* **Institución:** UNAM (Universidad Nacional Autónoma de México) / IIBI / CISAN.
* **Objetivo:** Maquetar la interfaz pública (Frontend) que se inyectará en el CMS **Omeka S v4.2.0**.
* **Contenido de Autoridad:** Todos los recursos, textos y enlaces oficiales provienen del archivo `Omeka_colecciones.md`. **Regla estricta:** No inventar contenido de relleno, métricas ni secciones que no existan en el documento base.

---

## 2. Pila Tecnológica y Estructura
* **HTML:** HTML5 puro. El código HTML se inyecta directamente en Omeka, por lo que NO debe llevar las etiquetas `<html>`, `<head>` o `<body>`. Todo se envuelve en un contenedor principal `<div class="container-fluid px-0 papiit-theme-wrapper">`.
* **CSS:** CSS Vanilla.
* **Frameworks Externos (vía CSS):** 
  * Bootstrap v5.3.8
  * Bootstrap Icons v1.11.3
  * *Nota para la IA:* Estos frameworks se cargan localmente usando `@import` al inicio del archivo `style.css` (`/application/asset/vendor/...`).

---

## 3. Identidad Visual y UI/UX
* **Enfoque de Diseño:** Rigurosamente académico, formal, simétrico, limpio y de alto perfil institucional.
* **Paleta de Colores Oficial (Obligatoria):**
  * **Azul Primario (Institucional):** `#0a3663` (Para encabezados, banners, tipografía fuerte).
  * **Azul Secundario (Interactivos):** `#0d47a1` (Para botones y elementos hover).
  * **Azul Acento:** `#1565c0` (Para detalles y pre-títulos).
  * **Fondo Principal:** `#f8f9fa` (Gris/Azul muy suave para contraste con tarjetas blancas).
  * *Regla:* **Prohibido** usar colores naranjas (`#ee8219`) o amarillos, así como diseños tipo *Glassmorphism*.

---

## 4. Patrones de Diseño (Componentes)
Para mantener la coherencia visual con el resto del sitio, se deben seguir estos patrones:

### A. Tarjetas Formales (Formal Cards)
Se utiliza un diseño de tarjeta sólida blanca (`bg-white`) para mostrar las colecciones.
* **Clases Bootstrap usadas:** `card border-0 shadow-sm rounded-4 h-100 p-4`.
* **Estructura de la tarjeta:**
  1. Pre-título pequeño (`.text-uppercase`, color Acento).
  2. Título principal (`h5.fw-bold.text-primary`).
  3. Texto descriptivo (`p.small.text-muted.flex-grow-1`).
  4. Botón interactivo anclado al fondo (`.mt-auto`).

### B. Botones de Redirección (Manejo de Enlaces)
Omeka S no procesa bien algunos reproductores multimedia (como Spotify o YouTube). Por lo tanto, los ítems en las tarjetas deben incluir botones de redirección explícitos usando los colores semánticos de Bootstrap y los iconos correspondientes:
* **YouTube:** `btn-outline-danger` + `bi-youtube`.
* **Spotify:** `btn-outline-success` + `bi-spotify`.
* **Repositorio UNAM:** `btn-outline-primary` + `bi-bank`.
* **Web/Zotero/Glosarios:** `btn-outline-secondary` + iconos como `bi-globe`, `bi-link-45deg` o `bi-file-earmark-pdf`.

---

## 5. Solución de Problemas Críticos en Omeka S (Quirks)
Al inyectar código en Omeka S, los estilos globales del tema de Omeka suelen "romper" o "aplastar" el CSS personalizado. La IA debe recordar lo siguiente al escribir CSS:

* **Protección de Listas (Bullets):** Omeka fuerza puntos negros (`•`) en las listas. Si usas listas (`<ul>`, `<li>`), debes forzarlas agresivamente desde `style.css`:
  ```css
  .papiit-theme-wrapper .formal-list-group {
    margin: 0 !important; padding: 0 !important; list-style-type: none !important;
  }
  .papiit-theme-wrapper .formal-list-item {
    list-style-type: none !important;
  }
  .papiit-theme-wrapper .formal-list-item::marker,
  .papiit-theme-wrapper .formal-list-item:before {
    content: none !important; display: none !important;
  }
  ```
* **Contenedor Aislado:** Todo el CSS personalizado debe tener como prefijo la clase `.papiit-theme-wrapper` para evitar afectar la interfaz de administración de Omeka S.
* **Filtro de Seguridad de Omeka (HTML Purifier):** Al copiar el código HTML en los bloques de contenido de Omeka S, el sistema eliminará automáticamente cualquier etiqueta que esté vacía por considerarla inválida. Para usar iconos, es **estrictamente obligatorio** colocar un espacio en blanco inquebrantable (`&nbsp;`) dentro de cada etiqueta de icono para engañar al filtro.
  * ❌ Incorrecto: `<i class="bi bi-youtube"></i>`
  * ✅ Correcto: `<i class="bi bi-youtube">&nbsp;</i>`
* **Navegación Interna Inhabilitada (Anchor Links rotos):** El enrutador de Omeka S y su filtro interceptan y rompen la navegación nativa mediante anclas (hashes `#id`). **Regla estricta:** NO incluir menús internos ni botones flotantes o tipo "Hero" que apunten a secciones dentro de la misma página (ej. `<a href="#publicaciones">`). El scroll nativo no funcionará bajo este CMS.
* **Gráficos SVG Borrados:** El filtro HTML Purifier de Omeka S elimina sin piedad cualquier etiqueta `<svg>` que se escriba en el bloque HTML. Para usar ilustraciones vectoriales hechas con código, **está prohibido usar etiquetas `<svg>` en el layout**. Se debe inyectar la imagen vectorizada usando una clase en `style.css` con el atributo `background-image: url("data:image/svg+xml;base64,...")`.

---

## 6. Archivos Clave del Proyecto
1. `PAPIIT/home_layout.html`: Contiene la estructura principal en HTML5 puro (usando grid de Bootstrap).
2. `PAPIIT/style.css`: Contiene las variables institucionales y los overrides necesarios.
3. `Omeka_colecciones.md`: Fuente única de verdad para el contenido textual y los hipervínculos de los recursos.
