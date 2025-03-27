# Inicio del proyecto

Levantar entorno virtual, para encapsular dependencias

    python3 -m venv ~/.venvs/django-env

El comando de arriba inicializa en la ruta .venvs, dentro de la carpeta django-env, que es donde
se encuentra el entorno. Útil si prefieres organizar tus entornos virtuales en un directorio centralizado, en lugar de tenerlos dentro de cada proyecto.

Activar el entorno virtual según la ubicación donde se creó

    source ~/.venvs/django-env/bin/activate

Si la activación fue exitosa, deberías ver algo como esto en la terminal:

    (django-env) user@pc:~/django$

Esto indica que estás usando el entorno virtual.

Para salir del entorno virtual y volver al sistema normal:

    deactivate

## Comando para inicializar el proyecto con Django

Ubicarse dentro del proyecto en la terminal, luego ejecutar

    pip install Django

Para instalar Django, posteriormente, el comando

    django-admin --help

Con el parámetro --help, puedes obtener una descripción general de los comandos, sus opciones y su uso. Se debe de escribir el comando luego el parámetro --help

El comando para inicializar Django es el siguiente 

    django-admin startproject nombre_del_proyecto

Importante colocar el nombre del proyecto con guiones bajos, no usar "-", porque los tomará como si
quicieras restar variables, al usar guiones bajos, lo reconoce como nombre.

Luego aparecerá la estructura normal del proyecto, aparecerá un archivo llamado manage.py, este archivo servirá para levantar la aplicación. ubicarse dentro del proyecto y ejecutar el siguiente comando.

    python manage.py --help # para obtener la descripción de los comandos

    python manage.py runserver
    python3 manage.py runserver # para versiones posteriores

Para levantar el proyecto, tener en cuenta la versión de python para ejecutar los comandos,
si se usa python3, utilizar la versión con python3.

## Iniciar app para dividir lógica en el proyecto

    python manage.py startapp {nombre_app} # colocar el nombre sin las llaves, las llaves son solo para referencia.

## Crear migrates por defecto de Django para las tablas del proyecto

    python manage.py migrate
    ./manage.py migrate # es lo mismo pero para no escribir python

## Crear las migraciones creadas durante el proyecto

    python manage.py makemigrations
    ./manage.py makemigrations # es lo mismo pero para no escribir python

## Comando para revisar Base de Datos

    ./manage.py dbshell

Por si aparece un error al revisar la base de datos, aquí la solución
CommandError: You appear not to have the 'sqlite3' program installed or on your path.

Al ejecutar: $ python manage.py dbshell

Falta instalar sqlite3. En linux lo instala así: - Primero actualiza tu gestor de paquetes (recomendable para obtener la ultima version disponible del paquete a instalar): 

    sudo apt update- 

ahora instala el paquete sqlite3 

    sudo apt install sqlite3

## Dentro de la Shell de Sqlite3, para ver las tablas utilizar el siguiente comando

    .tables

## Dentro de la Shell de Sqlite3, para ver dentro de las tablas utilizar el siguiente comando

    .schema {nombre de la tabla}

## Comando para entrar a la Shell con Python, utilizado para entrar a las tablas SQL

    python manage.py shell
    ./manage.py shell # lo mismo que el de arriba pero abreviado

    CTRL + z # Para salir de la terminal Shell

## Comando para instalar librería para hacer más interactiva la Shell de Python

    pip install ipython

Luego se puede ejecutar la shell de python, con la nueva forma interactiva

    ./manage.py shell

Para salir de la consola usar el siguiente comando
   
    exit

# Ver el objeto request en Django, desde la terminal Shell

    from django.http import HttpRequest

    request = HttpRequest()
    print(request.__dict__)




# Comentario sobre la estructura de archivos en Django
En Django, la estructura del proyecto y la ubicación de los archivos de plantilla (templates) siguen ciertas convenciones para asegurar que el framework pueda encontrar y renderizar correctamente los archivos HTML

Cada aplicación en Django puede tener sus propias plantillas y, para mantener el código organizado y evitar conflictos de nombres, se recomienda seguir esta estructura:

myproject/

myapp/

templates/

myapp/

template1.html

template2.html

views.py

models.py

Debido a que pertenece a un comentario, es preferible revisar bien en otras fuentes si es la única
o si hay otras mejores. 

# Un poco sobre Managers en Django
Los managers son una parte fundamental del sistema de consultas.

Definición: Un manager es la interfaz a través de la cual Django proporciona operaciones de consulta a la base de datos para un modelo.
Función principal: Actúa como un intermediario entre el modelo y la base de datos, proporcionando métodos para realizar consultas.
Manager por defecto: Cada modelo de Django tiene al menos un manager, llamado objects por defecto.
todos_los_libros = Book.objects.all() libros_filtrados = Book.objects.filter(autor="Tolkien")

Métodos comunes:

all(): Recupera todos los objetos.
filter(): Filtra objetos según criterios.
get(): Obtiene un objeto único.
create(): Crea un nuevo objeto.
update(): Actualiza objetos.
Managers personalizados: Puedes crear managers personalizados para añadir métodos específicos o modificar el comportamiento de las consultas.
Chaining: Los métodos de los managers se pueden encadenar para construir consultas complejas.
Lazy evaluation: Las consultas no se ejecutan hasta que realmente se necesitan los resultados, lo que permite una construcción eficiente de consultas complejas.