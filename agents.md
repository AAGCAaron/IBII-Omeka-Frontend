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

### A. Tarjetas Grid Verticales (Formal Cards)
Se utiliza un diseño de tarjeta sólida blanca (`bg-white`) para mostrar elementos en grillas de varias columnas.
* **Clases Bootstrap usadas:** `card border-0 shadow-sm rounded-4 h-100 p-4`.
* **Estructura de la tarjeta:**
  1. Pre-título pequeño (`.text-uppercase`, color Acento).
  2. Título principal (`h5.fw-bold.text-primary`).
  3. Texto descriptivo (`p.small.text-muted.flex-grow-1`).
  4. Botón interactivo anclado al fondo (`.mt-auto`).

### B. Tarjetas Horizontales de Recursos (Horizontal Cards)
Utilizadas en las subcolecciones para mostrar ítems de forma apaisada, ideales para detallar publicaciones o videos de difusión.
* **Estructura HTML:**
  - Contenedor principal: `.horizontal-card` con la clase de Bootstrap `.position-relative`.
  - Columna izquierda (`col-md-4 col-lg-3 col-xl-2 cover-column`): Contiene un gradiente temático (`.cover-book`, `.cover-chapter`, `.cover-article`, `.cover-web`, `.cover-ponencia`, etc.), un lomo de libro decorativo (`.cover-spine`) y un icono centrado. **Nota:** Si el icono está sobre un fondo oscuro, usar `text-white` para evitar pérdida de contraste.
  - Columna derecha (`col-md-8 col-lg-9 col-xl-10`): Contiene el `.card-body` con título, autores, lorem ipsum (si no hay texto oficial), y el botón de acción.
* **Comportamiento Clickable (Importante):** Por defecto, no usar `.stretched-link` en los botones dentro de estas tarjetas si se requiere que el botón de acción sólo se ilumine/anime cuando el cursor pasa exactamente sobre él. Usar `.stretched-link` hará que toda la tarjeta actúe como botón y la animación del botón se disparará prematuramente.
* **Hover Micro-Animations:** Al pasar el cursor por cualquier parte de la tarjeta, esta realiza una traslación hacia arriba (`translateY(-4px)`) y gana sombra.

### C. Footer Institucional (Floating Island)
* **Diseño:** No es un footer anclado al fondo clásico. Es una sección flotante (`floating-section shadow-sm rounded-4 bg-white p-4 mx-3 mx-lg-5 mb-4`) sin bordes (`border: none;`), diseñada como una "isla" flotante final.
* **Contenido:** Contiene el nombre del proyecto (PAPIIT IG300724), dependencia (IIBI / CISAN UNAM) y dirección física. **Prohibido** incluir datos de contacto (teléfono, email) en el footer según requerimiento.

### D. Botones de Redirección y Acciones
Los recursos multimedia (como Spotify o YouTube) o enlaces académicos se manejan con botones con iconos explícitos y colores semánticos:
* **YouTube:** `btn-outline-danger` + `bi-youtube` (para ponencias o videos).
* **Spotify:** `btn-outline-success` + `bi-spotify` (para podcasts de audio).
* **Repositorio UNAM:** `btn-outline-primary` + `bi-bank` (para visualización/lectura de PDFs).
* **Descargas directas (EPUB):** `btn-outline-success` + `bi-download` con atributo `download`.
* **Botones Principales (Hub):** Clases customizadas (`btn-hero-primary`, `btn-hero-accent`, `btn-hero-warning`, `btn-hero-indigo`) creadas en `style.css` que aseguran colores sólidos e íconos.

---

## 5. Solución de Problemas Críticos en Omeka S (Quirks)
Al inyectar código en Omeka S, los estilos globales del tema de Omeka suelen "romper" o "aplastar" el CSS personalizado. La IA debe recordar lo siguiente al escribir CSS y HTML:

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
* **Filtro de Seguridad de Omeka (HTML Purifier - Etiquetas Vacías):** Al copiar el HTML en Omeka S, el sistema eliminará automáticamente cualquier etiqueta que esté vacía por considerarla inválida.
  * Para usar iconos o figuras vacías, es **estrictamente obligatorio** colocar un carácter de contenido dentro de la etiqueta.
  * **Alineación Perfecta en Círculos y Flexbox:** Si se usa un espacio común (`&nbsp;`) dentro de un icono `<i>` dentro de un círculo con flexbox centrado, el icono se verá **desplazado a la izquierda**. Para resolverlo y que se mantenga centrado, **se debe utilizar un Zero-Width Joiner (`&zwj;`) en lugar de un espacio**.
    * ❌ Incorrecto (desplazado): `<i class="bi bi-broadcast">&nbsp;</i>`
    * ✅ Correcto (centrado): `<i class="bi bi-broadcast">&zwj;</i>`
* **Botones Pierden el Texto (Letras apagadas) en Hover:** Al usar botones personalizados con colores fuertes y Bootstrap, el evento `:hover` puede forzar que el texto herede el color azul oscuro o gris de los enlaces. **Solución:** En `style.css`, declarar SIEMPRE `color: #ffffff !important;` dentro de la pseudo-clase `:hover` de cualquier botón personalizado.
* **Compatibilidad de Tarjetas Clickables (Evitar Enlaces en Bloque):** En HTML5 es válido colocar divs dentro de un enlace `<a>`, pero HTML Purifier en Omeka S suele desarmar esta estructura por regirse bajo estándares antiguos.
  * **Solución Obligatoria:** Mantener el enlace `<a>` anidado normalmente dentro del texto y utilizar la técnica de CSS `.stretched-link` de Bootstrap junto con `.position-relative` en la tarjeta. Esto simula el clic en toda la tarjeta sin envolver bloques visuales en un tag `<a>`.
* **Navegación Interna Inhabilitada (Anchor Links rotos):** El enrutador de Omeka S rompe la navegación nativa mediante anclas (hashes `#id`). **Regla estricta:** NO incluir menús internos ni botones flotantes o tipo "Hero" que apunten a secciones dentro de la misma página.
* **Gráficos SVG Borrados:** El filtro HTML Purifier elimina etiquetas `<svg>`. **Está prohibido usar etiquetas `<svg>` en el layout HTML**. Se debe inyectar la imagen vectorizada usando una clase en `style.css` con el atributo `background-image: url("data:image/svg+xml;base64,...")`.
* **Variables CSS en atributos `style` (Colores Eliminados):** HTML Purifier NO reconoce la sintaxis de variables `var(--...)` ni colores complejos como `rgba(...)` cuando se usan como estilos en línea (`style="..."`). Esto provoca que fondos, textos y bordes pierdan su color y se vuelvan transparentes o negros por defecto. **Solución estricta:** Siempre usar códigos hexadecimales puros (ej. `#0a3663`, `#f8f9fa`) en los atributos `style` del HTML.
* **Imágenes Deformadas (object-fit y overflow ignorados):** Omeka S puede purgar propiedades como `overflow: hidden` y `object-fit: cover` de los estilos en línea, provocando que los avatares se desborden de sus círculos o se aplasten. **Solución:** NUNCA usar estilos en línea para esto. Usar siempre las clases nativas de Bootstrap 5 directamente sobre la etiqueta `<img>`: añadir `rounded-circle` (para el corte circular) y `object-fit-cover` (para mantener proporciones).
* **Colapso de Secciones Inferiores (Barras que no tocan el fondo):** Si se diseña una barra de color o contenedor que deba ir pegado al ras del fondo de una sección, los márgenes inyectados por Omeka S pueden despegarla si usa `position-relative`. **Solución:** Anclar estrictamente el elemento al fondo usando las clases `position-absolute bottom-0 start-0 w-100`.
* **Etiquetas Estructurales Eliminadas (`<footer>`, `<header>`):** HTML Purifier en Omeka S puede considerar inválido insertar etiquetas semánticas de nivel superior como `<footer>` o `<header>` dentro del contenido de una página, y las borrará por completo (llevándose consigo todas sus clases y estilos). **Solución:** Siempre usar `<div>` estándar para construir pies de página o encabezados de sección personalizados dentro de las páginas.
* **Control de Cuadrículas (Grid) y Espacios en Blanco:** Para mantener la simetría y evitar huecos asimétricos al usar el sistema Grid de Bootstrap, NO se debe usar el ancho automático (`col-lg` libre) si se desea un máximo de columnas (ej. 3 por fila). El layout automático encogerá infinitamente los elementos en lugar de forzar un salto de línea. **Solución:** Usar restricciones explícitas como `col-lg-4` (para máximo 3 elementos por fila), y añadir SIEMPRE la clase `justify-content-center` al contenedor `.row`. De esta manera, si en la última fila sobran 1 o 2 tarjetas, se centrarán de forma simétrica sin estirarse ni dejar huecos feos del lado derecho.

---

## 6. Archivos Clave del Proyecto
1. **[Tests/papiit.html](file:///d:/OMEKAS/Tests/papiit.html)**: Portal de navegación o Home del sitio. Rediseñado como un hub que enlaza a las subpáginas `/s/papiit/page/publicaciones` y `/s/papiit/page/ProductosDeDifusionYDivulgacion` mediante tarjetas interactivas gigantes, libre de listados redundantes.
2. **[Tests/coleccionesPAPIIT/publicaciones.html](file:///d:/OMEKAS/Tests/coleccionesPAPIIT/publicaciones.html)**: Subpágina de la colección de Publicaciones con descarga de EPUBs y lectura directa de PDFs.
3. **[Tests/coleccionesPAPIIT/productosDeDifusionYDivulgacion.html](file:///d:/OMEKAS/Tests/coleccionesPAPIIT/productosDeDifusionYDivulgacion.html)**: Subpágina de la colección de Difusión con tarjetas horizontales completamente integradas con `.stretched-link` y el nuevo gradiente del héroe color vino.
4. **[PAPIIT/style.css](file:///d:/OMEKAS/PAPIIT/style.css)**: Hoja de estilos centralizada para el tema PAPIIT. Contiene variables, gradientes de héroes, colores temáticos de portadas y transiciones hover de tarjetas.
5. **[Omeka_colecciones.md](file:///d:/OMEKAS/Omeka_colecciones.md)**: Fuente única de verdad para el contenido textual y los hipervínculos de los recursos.
