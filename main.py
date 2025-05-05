from dinamic_content import *
from static_content import *
from validate_and_loading import *


if __name__ == "__main__":
   
    di_get_popups_home()
    driver.quit()
    print('🔴 fail_get_categories', fail_get_categories)
    print('🔴 fail_get_sub_categories', fail_get_sub_categories)   
    print('🔴 fail_get_num_pages_for_category', fail_get_num_pages_for_category)
    print('🔴 fail_get_products_for_page', fail_get_products_for_page)
"""   
Pasos del webscraping


1) Hacer hover sobre los elementos de la barra de navegacion, denomidados secciones
2) En cada hover recuperar la url de los elementos resaltados en azul, que son las familias
3) Remplazar la plabra 'landing' por 'category' de cada una de las urls recuperadas para acceder al catalogo completo de esa familia
4) Recuperar la url de cada categoria presnete por familia en la barra lateral del izquierda de la pagina
5) Verificar si cada pagina de catgeoria tiene subcategorias
    --- Si habian sub_categorias recorrer cada una y extraer los productos
    --- Si no habian recuperar los productos de la url de la categoria

Gerarquia de los productos
-- seccion
-- familia
-- categoria
-- sub categoria 
"""