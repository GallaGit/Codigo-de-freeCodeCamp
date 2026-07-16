//¿Cómo se crea una nueva línea en cadenas y se escapan las cadenas?

/*let poem = "Roses are red,\nViolets are blue,\nJavaScript is fun,\nAnd so are you.";
console.log(poem);*/

//Estoy es un error
//let statement = "She said, "Hello!""; //JavaScript se confunde porque piensa que la cadena termina después de la palabra "said," pero quieres que las comillas alrededor de "Hello!" formen parte de la cadena.

//Forma correcta de escribir la cadena
/*let statement = "She said, \"Hello!\"";
console.log(statement); // She said, "Hello!"*/

//Aquí hay otro ejemplo usando comillas simples:

/*let quote = 'It\'s a beautiful day!';
console.log(quote);*/ // It's a beautiful day!
//Al escapar la comilla simple con \', JavaScript sabe incluirla como parte de la cadena en lugar de terminar la cadena anticipadamente.


//¿Qué son los literales de plantilla y qué es la interpolación de strings?

//Aquí tienes un ejemplo de un template literal:

/*const name = "Alice";
const greeting = `Hello, ${name}!`;*/

//console.log(greeting);
//Observe el uso de comillas inversas en lugar de comillas simples o dobles. La sintaxis ${name} es un ejemplo de interpolación de strings, donde el valor de la variable name se inserta directamente en la cadena.

//Aquí hay un ejemplo utilizando concatenación de strings y el operador más (+):

/*const name = "Alice";
const age = 25;
const message = "My name is " + name + " and I am " + age + " years old.";
console.log(message);*/

//Y aquí hay un ejemplo con literales de plantilla e interpolación de strings:

const name = "Alice";
const age = 25;
const message = `My name is ${name} and I am ${age} years old.`;
console.log(message); 

//Otra gran característica de los literales de plantilla es que soportan cadenas multilínea. Con las cadenas normales, necesitarías usar caracteres de escape (\n) para crear nuevas líneas. Con los literales de plantilla, simplemente puedes escribir la cadena en varias líneas, y el formato se preserva:

let poem = `Roses are red,
Violets are blue,
JavaScript is fun,
And so are you.`;

console.log(poem);

//Otra característica de los template literals es que te permiten insertar expresiones de JavaScript directamente dentro de la cadena, como en este ejemplo:

const song = "Bohemian Rhapsody";
const score = 9.5;
const highestScore = 10;
const output = `One of my favorite songs is "${song}". I rated it ${
  (score / highestScore) * 100
}%.`;
console.log(output); 
