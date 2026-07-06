# ¿Qué es una cadena en JavaScript, y qué es la inmutabilidad de cadena?

- En JavaScript, una cadena es una secuencia de caracteres utilizada para representar datos de texto. Las cadenas son uno de los tipos de datos primitivos en el lenguaje, junto con los números, booleanos, null, y undefined.

Para crear una cadena en JavaScript, puede utilizar comillas simples (') o comillas dobles (").

Aquí hay un ejemplo de cómo crear dos variables que contienen valores de cadena:

let singleQuotes = 'This is a string';
console.log(singleQuotes);
let doubleQuotes = "This is also a string";
console.log(doubleQuotes);
Aunque puedes usar comillas simples o dobles para crear cadenas, es importante ser consistente. Si una cadena comienza con una comilla simple, también debe terminar con una comilla simple.

Lo mismo se aplica a las comillas dobles. El siguiente ejemplo lanzará un error porque comienza con una comilla doble y termina con una comilla simple:

const improperStr = "Do not do this';
Otra cosa a tener en cuenta es que las cadenas son inmutables. En programación, la inmutabilidad significa que una vez que algo se crea, no se puede cambiar. Por lo tanto, cuando creas una cadena, no puedes cambiar sus caracteres directamente. En su lugar, deberías crear una nueva cadena si quieres hacer cambios.

Aquí hay un ejemplo de asignación de una nueva cadena a una variable developer:

let developer = "Jessica";
console.log(developer);
developer = "Quincy";
console.log(developer);
Dado que las cadenas son inmutables, no podemos actualizar la primera cadena directamente. Por eso, estamos asignando una nueva cadena a la variable developer.

Las cadenas son una parte importante de la programación, y en futuras lecciones, aprenderás técnicas avanzadas para manipularlas y aprovechar todo su potencial para crear aplicaciones dinámicas e interactivas.
