from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length = 250)
    year = models.TextField(max_length = 4, null = True)

    def __str__(self):  # Método que devuelve una representación en cadena del objeto
        return f"{self.title} - {self.year}"  # Devuelve el título y el año del coche

'''
Comandos usado dentro de la Shell 
CTRl + z para salir de la terminal Shell

from my_first_app.models import Car # Importar el modelo Car
car = Car(title = "BMW", year = "2023") # Crear una instancia del modelo Car
print(car) # Imprimir la instancia del modelo Car
car.save() # Guardar la instancia del modelo Car en la base de datos

# Actualización y eliminación de datos
car.title = "Audi" # Cambiar el título del coche
car.save() # Guardar los cambios en la base de datos
car_two = Car(title = "Mercedes", year = "2022") # Crear otra instancia del modelo Car
car_two.save() # Guardar la instancia del modelo Car en la base de datos
car.delete() # Eliminar la instancia del modelo Car de la base de datos

Para revisar en la base de datos
python manage.py dbshell
select * from my_first_app_car; # Ver todos los coches

'''

class Publisher(models.Model):
    name = models.TextField(max_length = 250)
    address = models.TextField(max_length = 250)

    def __str__(self):
        return f"{self.name} - {self.address}"  # Devuelve el nombre y la dirección del editor

class Author(models.Model):
    name = models.TextField(max_length = 250)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.birth_date}"  # Devuelve el nombre y el año de nacimiento del autor
    
'''
Crear autores
author = Author(name = "John Doe", birth_date = "1990-01-01") # Crear una instancia del modelo Author
author.save() # Guardar la instancia del modelo Author en la base de datos
book = Book.objects.first() # Obtener el primer libro de la base de datos
book.authors.add(author) # Agregar el autor al libro
author_list = book.authors.all() # Obtener todos los autores del libro
book.authors.set(author_list) # Establecer la lista de autores del libro

'''

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)  # Relación uno a uno con Author
    website = models.URLField()
    biography = models.TextField(max_length = 500)

'''
Crear perfiles
from my_first_app.models import Publisher, Book, Profile, Author
author = Author.objects.first() # Obtener el primer autor de la base de datos
profile = Profile(author = author, website = "www.example.com", biography = "Biography of the author") # Crear una instancia del modelo Profile
profile.save() # Guardar la instancia del modelo Profile en la base de datos

Ver en la bdd
python manage.py dbshell
select * from my_first_app_profile; # Ver todos los perfiles
'''

class Book(models.Model):
    title = models.TextField(max_length = 250)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # Relación uno a muchos con Publisher
    authors = models.ManyToManyField(Author, related_name="authors")  # Relación uno a muchos con Author

    def __str__(self):
        return f"{self.title} - {self.publication_date} - {self.publisher}"
    
'''
Documentación sobre los campos Django
https://docs.djangoproject.com/en/5.0/ref/models/fields/
'''

'''
Consultas para publisher y book

from my_first_app.models import Publisher, Book
publisher = Publisher(name = "Editorial XYZ", address = "Calle Falsa 123")
publisher.save() # Guardar el editor en la base de datos
book = Book(title = "El gran libro", publication_date = "2023-10-01", publisher = publisher)
book.save() # Guardar el libro en la base de datos
book = Book.objects.get(id = 1) # Obtener el libro con id 1
book.title = "El gran libro de Python" # Cambiar el título del libro
book.save() # Guardar los cambios en la base de datos
book.delete() # Eliminar el libro de la base de datos

Para consultar los libros en la bdd
para abrir sqlite3
python manage.py dbshell
select * from my_first_app_book; # Ver todos los libros
consultar tablas
.tables
'''
    
'''
Algunos métodos de managers de Django
Author.objects.all() # Obtener todos los autores
Author.objects.filter(name = "John Doe") # Filtrar autores por nombre
Author.objects.exclude(name = "John Doe") # Excluir autores por nombre
Author.objects.get(id = 1) # Obtener un autor por id
Author.objects.first() # Obtener el primer autor
Author.objects.last() # Obtener el último autor
Author.objects.count() # Contar el número de autores
Author.objects.all().order_by('name') # Ordenar autores por nombre ascendente
Author.objects.all().order_by('-name') # Ordenar autores por nombre descendente
Author.objects.distinct() # Obtener autores distintos
Author.objects.values() # Obtener valores de los autores
Author.objects.values_list() # Obtener lista de valores de los autores
Author.objects.raw() # Obtener autores en bruto
Author.objects.none() # Obtener ningún autor
Author.objects.create('name': 'John Doe', 'birth_date': '1990-01-01') # Crear un autor
Author.objects.filter(id = 1).update(name = "Jane Doe") # Actualizar un autor

Author.objects.delete() # Eliminar autores
Author.objects.filter(id = 1).delete() # Eliminar un autor
Author.objects.filter(name = "John Doe").delete() # Eliminar autores por nombre

Author.objects.bulk_create() # Crear varios autores
Author.objects.bulk_update() # Actualizar varios autores
Author.objects.bulk_delete() # Eliminar varios autores
Author.objects.get_or_create() # Obtener o crear un autor
Author.objects.update_or_create() # Actualizar o crear un autor

'''
