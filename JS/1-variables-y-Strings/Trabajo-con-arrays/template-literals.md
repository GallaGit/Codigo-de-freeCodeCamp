# ¿Qué son los literales de plantilla y qué es la interpolación de strings?

En JavaScript, los literales de plantilla son una forma poderosa y flexible de trabajar con cadenas. A diferencia de las cadenas normales, que usan comillas simples (') o dobles ("), los literales de plantilla se definen con comillas inversas (`).

Permiten una manipulación de cadenas más sencilla, incluido el incrustar variables directamente dentro de una cadena, una característica conocida como interpolación de strings.

Los literales de plantilla facilitan la creación de cadenas que abarcan múltiples líneas o incluyen expresiones (como variables o incluso código JavaScript) directamente dentro de la cadena.

Aquí tienes un ejemplo de un template literal:

---
const name = "Alice";
const greeting = `Hello, ${name}!`;
---

console.log(greeting);
Observe el uso de comillas inversas en lugar de comillas simples o dobles. La sintaxis ${name} es un ejemplo de interpolación de strings, donde el valor de la variable name se inserta directamente en la cadena.

La interpolación de strings te permite incrustar variables y expresiones dentro de una cadena. Esto representa una mejora significativa sobre el método anterior, donde se concatenaban cadenas y variables utilizando el operador +.

Aquí hay un ejemplo utilizando concatenación de strings y el operador más (+):

const name = "Alice";
const age = 25;
const message = "My name is " + name + " and I am " + age + " years old.";
console.log(message); 
Y aquí hay un ejemplo con literales de plantilla e interpolación de strings:

---
const name = "Alice";
const age = 25;
const message = `My name is ${name} and I am ${age} years old.`;
console.log(message);
---
Como puedes ver, la interpolación de strings con literales de plantilla es mucho más limpia y fácil de leer, especialmente cuando trabajas con múltiples variables.

Otra gran característica de los literales de plantilla es que soportan cadenas multilínea. Con las cadenas normales, necesitarías usar caracteres de escape (\n) para crear nuevas líneas. Con los literales de plantilla, simplemente puedes escribir la cadena en varias líneas, y el formato se preserva:

let poem = `Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.`;

console.log(poem);
Otra característica de los template literals es que te permiten insertar expresiones de JavaScript directamente dentro de la cadena, como en este ejemplo:

---
const song = "Bohemian Rhapsody";
const score = 9.5;
const highestScore = 10;
const output = `One of my favorite songs is "${song}". I rated it ${
  (score / highestScore) * 100
}%.`;
console.log(output);
---
Los literales de plantilla son particularmente útiles cuando necesitas incluir variables o expresiones en cadenas, formatear cadenas complejas o trabajar con texto multilínea. Son más concisos y legibles en comparación con la concatenación tradicional de cadenas.

