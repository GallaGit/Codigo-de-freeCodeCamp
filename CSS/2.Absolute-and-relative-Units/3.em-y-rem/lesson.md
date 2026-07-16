# ¿Qué son las em y rem en CSS y cuándo deberías usarlas?

En la lección anterior, aprendimos sobre unidades de longitud absolutas como los píxeles. Aunque las unidades absolutas pueden ser útiles en ciertas situaciones, habrá momentos en los que querrás usar unidades relativas.

En esta lección, aprenderemos sobre dos unidades relativas: ems y rems.

Las unidades em son relativas al tamaño de fuente del elemento. Si estás usando ems para la propiedad font-size, el tamaño del texto será relativo al tamaño de fuente del elemento padre.

Para el HTML, tenemos un párrafo y un elemento div. El elemento párrafo tiene una clase para, y el elemento div tiene una clase blue-box.

Para la clase para, establecemos el font-size a 20px y el margin-bottom a 1.5em. This means that the margin will be 1.5 times the font size of the paragraph element. 1.5em results in 30 pixels of margin at the bottom of the paragraph. También hemos establecido un border de 2px solid red para que puedas ver mejor los márgenes.

Para la clase blue-box, establecemos el color de fondo como blue, el color del texto como white y el padding de 10px en los cuatro lados.

Desde el ejemplo, habrá un espacio claro entre la parte inferior del elemento párrafo y la caja azul.

¿Qué pasa si quitamos la propiedad font-size de la clase para?

Bueno, el margen inferior será relativo al tamaño de fuente del elemento padre. En este caso, el elemento padre es el elemento body, que tiene un tamaño de fuente predeterminado de 16px.

Buenas aplicaciones para ems serían cuando estás trabajando con componentes modulares como botones o tarjetas. Al usar unidades em, puedes asegurarte de que todos los aspectos del componente (como el acolchado, margen y bordes) se escalen proporcionalmente con el tamaño de fuente, manteniendo proporciones consistentes.

Hasta este punto, hemos estado estableciendo el tamaño de fuente para un elemento usando píxeles. Pero eso presenta algunos desafíos para los usuarios.

Dentro de la configuración de tu navegador, puedes controlar el tamaño de fuente predeterminado.

Para aquellos con discapacidades visuales, pueden aumentar el tamaño de fuente para facilitar la lectura. Pero si estás estableciendo píxeles para los tamaños de fuente en tus diseños web, el texto no se escalará proporcionalmente con el resto del contenido.

Una forma de abordar este problema es usar unidades rem para la tipografía. Una unidad rem es relativa al tamaño de fuente del elemento raíz, que es el elemento html.

Por defecto, el tamaño de fuente del elemento html es 16px. Si el usuario aumenta el tamaño de fuente en la configuración de su navegador, el tamaño de fuente del elemento html aumentará, y todas las unidades rem se escalarán proporcionalmente.

Al establecer el tamaño de fuente en 1.2rem, el tamaño de fuente del elemento párrafo será 1,2 veces el tamaño de fuente del elemento raíz. Si el usuario no ha cambiado el tamaño de fuente predeterminado, el tamaño de fuente del elemento párrafo será de 19.2px porque es 1.2 veces 16px.

Entonces, ¿cuándo deberías usar unidades rem? Las unidades rem son preferidas sobre los píxeles para la tipografía porque escalan proporcionalmente con la configuración del navegador del usuario. Esto hace que tu contenido sea más accesible para usuarios con discapacidades visuales.

Las unidades rem también pueden ayudar a mantener un espaciamiento y diseño consistentes entre diferentes elementos.
