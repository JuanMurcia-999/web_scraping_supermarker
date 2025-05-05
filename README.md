# webscraping productos de tienda web reconocida


Este web scraping tiene como obgetivo la extraccion de todos los productos ofrecios por una empresa reconocida relacionada con la construccion, hogar, auto partes, elementos ferreteros entre otras.

Estos son los pasos seguidos para extrarer los productos:

1. Hacer hover sobre los elementos de la barra de navegacion, denomidados secciones
2. En cada hover recuperar la url de los elementos resaltados en azul, que son las familias
3. Remplazar la plabra 'landing' por 'category' de cada una de las urls recuperadas para acceder al catalogo completo de esa familia
4. Recuperar la url de cada categoria presnete por familia en la barra lateral del izquierda de la pagina
5. Verificar si cada pagina de catgeoria tiene subcategorias
    - Si habian sub_categorias recorrer cada una y extraer los productos
    - Si no habian recuperar los productos de la url de la categoria

### Gerarquia de los productos
- seccion
- familia
- categoria
- sub categoria 

Este webscraping comprende contenido estatico y dinamico por lo cual se hace uso de las librerias ** sellenium ** para el contenido dinamico presente en los primeros pasos
y ** beautifulSoup ** para el contenido estatico presente en las paginas que contiene los productos.

### Datos extraidos

- score: Puntuacion de 1 a 5 estrellas 
- brand: Marca del fabricante del produco
- sku: Codigo unico por producto
- price: precio en pesos colombianos
- url: url del producto en la tienda real
- image: url de la imagen de presentacion del producto
- name: Nombre del producto
- section: agrupacion global
- family: Grupo en la seccion al que pertenece
- category: grupo en la familia a la que pertenece
- sub_category: grupo (si existe) al que pertenece

El tiempo total de extraccion fue de 2 horas recuperando cerca de 200k productos


### Modelado y tranformacion de los datos


En este punto los datos cargados en una base de datos sqlite se presentan en una unica tabla con todos los productos y se debe remodelar para obtener tablas de:

- products
- categories
- brands
- sections
- familys
- categories
- sub_categories

- 
  ![image](https://github.com/user-attachments/assets/9d847555-8302-4979-a7e1-e0e7944f93f5)


y sus respectivas relaciones


