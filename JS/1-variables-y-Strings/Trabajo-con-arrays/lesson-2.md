# ¿Cómo se crea una nueva línea en cadenas y se escapan las cadenas?

Cuando trabajas con cadenas en JavaScript, hay momentos en los que necesitas incluir caracteres especiales que el motor de JavaScript podría malinterpretar.

Dos tareas comunes implican crear una nueva línea dentro de una cadena y escapar ciertos caracteres (como comillas) para asegurarse de que se vean correctamente.

En muchos lenguajes de programación, incluido JavaScript, puedes crear una nueva línea en una cadena usando un carácter especial llamado secuencia de escape. La secuencia de escape más común para nuevas líneas es \n.

Por ejemplo, si deseas dividir una cadena en múltiples líneas, usarías \n donde quieres que comience la nueva línea:

let poem = "Roses are red,\nViolets are blue,\nJavaScript is fun,\nAnd so are you.";
console.log(poem);
La secuencia de escape \n le dice a JavaScript que inserte un salto de línea en ese punto, lo que da como resultado que la cadena se muestre en múltiples líneas.

Otro concepto importante al trabajar con cadenas es el escape de caracteres. A veces, necesitas incluir caracteres en tu cadena que JavaScript normalmente usa para algo más, como comillas.

Si simplemente usas comillas dentro de una cadena sin escaparlas, puede causar un error porque JavaScript pensará que estás tratando de terminar la cadena.

Por ejemplo, esto causará un error:

let statement = "She said, "Hello!"";
JavaScript se confunde porque piensa que la cadena termina después de la palabra "said," pero quieres que las comillas alrededor de "Hello!" formen parte de la cadena.

Para solucionar esto, puedes escapar las comillas internas colocando una barra inclinada (\) antes de ellas:

let statement = "She said, \"Hello!\"";
console.log(statement); // She said, "Hello!"
La barra inclinada le dice a JavaScript que trate las comillas como caracteres literales, para que aparezcan correctamente en la salida.

También puedes escapar otros caracteres especiales, como la barra inclinada en sí (\\), o comillas simples dentro de una cadena rodeada por comillas simples (\').

Aquí hay otro ejemplo usando comillas simples:

let quote = 'It\'s a beautiful day!';
console.log(quote); // It's a beautiful day!
Al escapar la comilla simple con \', JavaScript sabe incluirla como parte de la cadena en lugar de terminar la cadena anticipadamente.

Escapar y crear nuevas líneas son esenciales cuando estás formateando la salida o manejando caracteres especiales en cadenas. Estas técnicas te ayudan a prevenir errores y aseguran que tu texto aparezca exactamente como tienes la intención.
