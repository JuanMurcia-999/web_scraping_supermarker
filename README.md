# Web scraping de productos de tienda web reconocida

Este proyecto de web scraping tiene como objetivo la extracción de todos los productos ofrecidos por una empresa reconocida, relacionada con la construcción, el hogar, autopartes, elementos ferreteros, entre otros.

## Pasos seguidos para extraer los productos

0. Configurar la cookie que elimina la solicitud de ubicacion de la pagina
1. Hacer *hover* sobre los elementos de la barra de navegación, denominados **secciones**.
2. En cada *hover*, recuperar la URL de los elementos resaltados en azul, que corresponden a las **familias**.
3. Reemplazar la palabra `'landing'` por `'category'` en cada una de las URLs recuperadas, para acceder al catálogo completo de esa familia.
4. Recuperar la URL de cada **categoría** presente por familia en la barra lateral izquierda de la página.
5. Verificar si cada página de categoría tiene **subcategorías**:
   - Si hay subcategorías, recorrer cada una y extraer los productos.
   - Si no hay subcategorías, extraer los productos directamente desde la URL de la categoría.

## Jerarquía de los productos

- Sección
- Familia
- Categoría
- Subcategoría (si existe)

Este scraping comprende contenido estático y dinámico, por lo cual se hace uso de las siguientes librerías:

- **Selenium**: para el contenido dinámico presente en los primeros pasos.
- **BeautifulSoup**: para el contenido estático presente en las páginas que contienen los productos.

## Datos extraídos

- `score`: Puntuación de 1 a 5 estrellas.
- `brand`: Marca del fabricante del producto.
- `sku`: Código único por producto.
- `price`: Precio en pesos colombianos.
- `url`: URL del producto en la tienda real.
- `image`: URL de la imagen de presentación del producto.
- `name`: Nombre del producto.
- `section`: Agrupación global.
- `family`: Grupo en la sección al que pertenece.
- `category`: Grupo en la familia al que pertenece.
- `sub_category`: Grupo (si existe) al que pertenece.

El tiempo total de extracción fue de aproximadamente **2 horas**, recuperando cerca de **200,000 productos**.

## Modelado y transformación de los datos

En este punto, los datos cargados en una base de datos SQLite se presentan en una única tabla con todos los productos, y deben ser remodelados para obtener tablas separadas de:

- `products`
- `categories`
- `brands`
- `sections`
- `families`
- `sub_categories`

Con sus respectivas relaciones.

![image](https://github.com/user-attachments/assets/9d847555-8302-4979-a7e1-e0e7944f93f5)
