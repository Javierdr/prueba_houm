### Prueba desarrollador backend para houm por Javier Dreves

A continuación haré una breve descripción de cada una de las funciones que debía realizar con algunas consideraciones que tomé

##### 1) Cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre:

Esta función tiene el nombre ```pokemons_with_at_and_two_a()```. Para esta función se considerarons los 1118 pokemones que posee la base de datos de pokeapi. En caso de querer considerar más pokemones en un futuro (o menos ya que los pokemones despues del 898 son algo raros y pasan al id numero 10001), basta con cambiar la constante ```TOTAL_POKEMONS``` presente en el archivo ```constants.py``` a el numero de pokemones que se desee verificar que cumpla con la propiedad pedida.

##### 2) Con cuántas especies de pokémon puede procrear raichu:

Esta función tiene el nombre ```procreation_specie_quantity(pokemon_name)``` donde ```pokemon_name``` es el pokemon al cual se le desee revisar con cuantas especies puede procrear. No lo quise hardcodear a un raichu ya que podría ser util tener esta información para otros pokemones aparte de raichu. Para ejecutar la función con un raichu, bastaría con ejecutar la función de la siguiente manera: ```procreation_specie_quantity('raichu')```. Para este ejercicio se asumio que especie de pokemon quiere decir pokemones distintos, es decir, con cuantos pokemones distintos puede procrear un raichu. 

##### 3) Máximo y mínimo peso de los pokémon de tipo fighting de primera generación:

Esta función tiene por nombre ```max_and_min_weight_by_type(type)``` donde ```type``` es el tipo de pokemon del cual se quieren buscar los pesos. No lo quise hardcodear al tipo fighting ya que podría ser util tener esta información para otros typos aparte de fighting. En esta función se usó la constante llamada ```FIRST_GENERATION_MAX_ID``` presente en el archivo ```constants.py```. Esta constante tiene el valor 151 que corresponde al mayor valor de un pokemon de primera generación. Si se quisiera obtener el peso máximo y mínimo de más (o menos) pokemones basta con cambiar esta constante. Además se filtra el id de cada pokemon desde la url de cada pokemon, esto para no tener que hacer cada requests a pokemones que no deben ser considerados. Para ejecutar la función con fighting, bastaría con ejecutar la función de la siguiente manera: ```max_and_min_weight_by_type('fighting')```. 

### Funciones auxiliares creadas.

Se crearon dos funciones auxiliares con el fin de encapsular cierto funcionamiento y evitar el replicar codigo innecesariamente. Estas funciones son las siguientes:

- **make_request(url):** Esta función hace un llamado a la url entregada mediante la librería requests. Realiza un try y except por si la api falla. Se realizó como una función aparte para no repetir el try - except en varias partes del código.
- **get_id_by_url(url):** Esta función recibe una url que será del tipo https://pokeapi.co/api/v2/pokemon/107/. La idea de esta función es que retorne el id dada la url, en este caso el 107. Esto se realiza mediante una [expresion regular](https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular) mediante la librería ```re```y  sin importar el largo de este id o si cambia la estructura de la url, el id igual será capturado.

### Estructura del repositorio.

El repositorio cuenta con un ```requirements.txt``` que contiene las librerias utilizadas. Luego una carpeta llamada ```src``` que contiene 3 archivos:
- ```constants.py```: Contiene las constantes utilizadas por las funciones.
- ```utils.py```: Contiene las funciones auxiliares mencionadas más arriba.
- ```main.py```: Contiene las tres funciones principales pedidas.

### Ejecución 

Para ejecutar el programa, dentro de la carpeta src, se debe ejecutar el comando 
```sh
python3 main.py
```

Ya se encuentran escritas las funciones pedidas con los parametros adecuados para que imprima en consola el resultado pedido. 
