# Guía de Control de Versiones y Despliegue - Parte 1

Esta guía documenta los cambios realizados en el frontend de los portales **PAPIIT** y **Museo Tamazola**, y detalla los comandos de Git necesarios para subir las modificaciones a GitHub de forma ordenada.

---

## 1. Resumen de Cambios Realizados

Se han modificado y creado los siguientes archivos locales en la carpeta `Tests`:

*   **Páginas Principales (Homes/Hubs de Navegación)**:
    *   `Tests/museoTamazola.html`: Rediseñado a partir del modelo de `papiit.html`, eliminando las listas detalladas ("islas") y reemplazándolas con un acceso directo de dos columnas a los nuevos sub-sitios.
    *   `Tests/papiit.html`: Modificado para habilitar que toda la tarjeta de sección sea clickable de forma integral.
*   **Sub-sitios de Colecciones (Tamazola)**:
    *   `Tests/colecciones Tamazola/ArchivoBienesComunales.html`: Se cambiaron todos los botones de descarga/lectura interactiva a un estado formal **Pendiente** (color secundario y deshabilitados).
    *   `Tests/colecciones Tamazola/museoDigitalComunitario.html` (NUEVO): Se creó la maqueta con las colecciones de *Memoria oral*, *Música de la región* y *Tradiciones y costumbres*. Todos los accesos se configuraron como **Pendiente**.
*   **Hojas de Estilo Centralizadas (CSS)**:
    *   `PAPIIT/style.css`: Añadido comportamiento de hover coordinado (animación del botón cuando el usuario pasa el cursor por cualquier área de la tarjeta clickable).
    *   `MuseoTamazola/style.css`: Agregado el degradado formal verde bosque (`.hero-museo`), gradientes específicos para las portadas del museo y animación coordinada en hover.

---

## 2. Comandos para Git y GitHub

Sigue estos pasos en tu terminal (ubicada en la raíz del proyecto `d:\OMEKAS`) para cargar los archivos a tu repositorio remoto:

### Paso A: Verificar el estado local
Muestra los archivos modificados y sin seguimiento (el nuevo archivo `museoDigitalComunitario.html` y esta guía aparecerán aquí):
```bash
git status
```

### Paso B: Preparar los cambios (Staging)
Agrega todos los archivos nuevos y modificados a la cola de confirmación:
```bash
git add .
```

### Paso C: Confirmar los cambios (Commit)
Crea una confirmación con un mensaje descriptivo de la entrega:
```bash
git commit -m "feat: rediseño de portadas hub, tarjetas clickables y mockups con estados pendientes para Tamazola y PAPIIT"
```

### Paso D: Enviar a GitHub (Push)
Sube los cambios a la rama principal de tu repositorio remoto:
```bash
git push
```
