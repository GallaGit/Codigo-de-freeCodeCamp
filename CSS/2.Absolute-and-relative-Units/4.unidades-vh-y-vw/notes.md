# ¿Qué son las unidades vh y vw, y cuándo debes usarlas?

En CSS, vh y vw son unidades relativas al viewport que te permiten dimensionar elementos basándote en las dimensiones de la ventana del navegador. Estas unidades son particularmente útiles para crear diseños responsivos que se adaptan a diferentes tamaños de pantalla.

vh significa "altura del viewport", y 1vh es igual al 1% de la altura del viewport.

De manera similar, vw significa "ancho del viewport", y 1vw es igual al 1% del ancho del viewport.

Esto significa que si estableces la altura de un elemento a 100vh, ocupará toda la altura del viewport, independientemente de las dimensiones en píxeles reales del dispositivo.

Estas unidades son especialmente útiles cuando deseas crear diseños de pantalla completa o elementos que mantengan una proporción específica de la pantalla.

Este CSS asegura que la sección de héroe siempre tendrá exactamente el tamaño del viewport, independientemente del tamaño de pantalla del dispositivo.

Las unidades vh y vw también pueden ser utilizadas para la tipografía y crear tamaños de texto responsivos.

Activa el editor interactivo y prueba ajustando el tamaño de la ventana de vista previa para ver cómo el texto se escala con el tamaño del viewport:

Esto establecerá el tamaño de fuente de los elementos h1 al 5% del ancho del viewport, permitiendo que el texto se escale suavemente con el tamaño de la ventana del navegador.

Una de las ventajas de las unidades vh y vw es que responden a cambios en el tamaño del viewport en tiempo real. Esto significa que si un usuario redimensiona la ventana de su navegador, los elementos dimensionados con estas unidades se ajustarán en consecuencia sin necesidad de recargar la página. Sin embargo, es importante utilizarlas con criterio. Establecer tamaños de fuente únicamente con unidades vw, por ejemplo, puede llevar a que el texto sea demasiado pequeño en pantallas estrechas o demasiado grande en pantallas anchas.

Otro aspecto a considerar es que en dispositivos móviles, la altura del viewport puede cambiar cuando la barra de direcciones del navegador aparece o desaparece, lo cual puede causar cambios inesperados en el diseño si estás utilizando extensivamente unidades vh.

En resumen, las unidades vh y vw son herramientas poderosas para crear diseños responsivos y elementos que se adapten al tamaño del viewport. Son particularmente útiles para secciones de pantalla completa, mantener proporciones de aspecto y crear diseños que se escalan suavemente. Sin embargo, deben utilizarse con reflexión y a menudo en combinación con otras técnicas CSS para asegurar la mejor experiencia de usuario en todos los dispositivos.
