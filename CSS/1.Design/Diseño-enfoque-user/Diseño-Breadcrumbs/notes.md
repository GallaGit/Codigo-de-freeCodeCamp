# Breadcumbs

Los **breadcrumbs** (o **migas de pan**) son un elemento de navegación que muestra al usuario **en qué parte de un sitio web se encuentra** y le permite volver fácilmente a páginas anteriores de la jerarquía.

Ejemplo:

```text
Inicio > Cursos > CSS > Breadcrumbs
```

En **CSS**, los breadcrumbs no son una característica especial del lenguaje. CSS solo se utiliza para **darles estilo**, por ejemplo:

* Mostrar los elementos en una sola línea.
* Agregar separadores (`>`, `/`, `→`) entre enlaces.
* Cambiar colores, espaciado y efectos al pasar el cursor.

Un ejemplo básico en HTML y CSS:

```html
<nav>
  <a href="/">Inicio</a> >
  <a href="/cursos">Cursos</a> >
  <span>CSS</span>
</nav>
```

```css
nav a {
  color: blue;
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}
```

**En resumen:** los breadcrumbs son una **ayuda de navegación** que indica la ruta del usuario dentro del sitio, mientras que **CSS se encarga únicamente de su apariencia**.
