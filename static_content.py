from bs4 import BeautifulSoup,SoupStrainer
from validate_and_loading import *
import json
import requests
import time
import re



# para tomar el codigo de fuente de la pagian y evitar la multiple consulta en la web
def leer_plantilla(name):
    with open(name, 'r', encoding='utf-8') as data:
        return data.read()





fail_get_categories=[]
fail_get_sub_categories=[]
fail_get_num_pages_for_category=[]
fail_get_products_for_page=[]

def get_categories(url_family,hierarchy):
    print('🔵  Obteniendo urls por catgeoria')
    try:
        response = requests.get(url_family).content
        solo_pagination =SoupStrainer('li', id=re.compile('li_product.L2_category_paths'))
        soup = BeautifulSoup(response, 'lxml', parse_only=solo_pagination)
        if soup and soup.text.strip():
            elements_a= soup.find_all(['a']) 
            for a in elements_a:                         # ⚪ Delimitar con cuantas categorias por familia trabajar  
                try:                                           
                    hierarchy['category'] = a.text
                    url_category= 'https://www.homecenter.com.co'+a['href']
                    get_sub_categories(url_category,hierarchy)
                except Exception:
                    fail_get_categories.append(url_family)
    except Exception as e:
        print(' 🔴 error in get_categories')    



def get_sub_categories(url_category,hierarchy):
    print('🟣  Obteniendo urls por subcatgeoria')
    try:
        response = requests.get(url_category).content
        solo_pagination =SoupStrainer('li', id=re.compile('li_product.L3_category_paths'))
        soup = BeautifulSoup(response, 'lxml', parse_only=solo_pagination)
        if soup and soup.text.strip():
            elements_a= soup.find_all(['a']) 
            for a in elements_a:                                # ⚪ Delimitar con cuantas sub_categorias por categoria trabajar
                try:                                   
                    hierarchy['sub_category'] = a.text
                    urls_sub_category='https://www.homecenter.com.co'+a['href']
                    get_num_pages_for_category(urls_sub_category,hierarchy)
                except Exception as e:
                    fail_get_sub_categories.append(url_category)
        else:
        # Solo elimina la clave si ya existía antes
            if 'sub_category' in hierarchy:
                del hierarchy['sub_category']
            get_num_pages_for_category(url_category,hierarchy)
    except Exception as e:
        print('🔴 error in get_categories')    



def get_num_pages_for_category(page,hierarchy):
    print('🟠  Obteniendo urls por cada pagina de productos')
    urls = []
    try:
        response = requests.get(page).content
        solo_pagination = SoupStrainer('div', class_='jsx-570059173 pagination-container notranslate')
        soup = BeautifulSoup(response, 'lxml', parse_only=solo_pagination)
  
        if soup and soup.text.strip():
            buttons = soup.find_all(['button'])
            num_pages=int(buttons[-2].text)
            for i in range(1,num_pages+1):
                if 'id=123' in page:
                    urls.append(page.replace('id=123',f'currentpage={i}'))  
                else:
                    urls.append(page+f'?currentpage={i}')
            get_products_for_page(urls,hierarchy)
        else:
            urls.append(page)
            get_products_for_page(urls,hierarchy)
    except Exception as e:
        fail_get_num_pages_for_category.append(page)
        print('🔴 falla',e,page)




def get_products_for_page(pages,hierarchy):
    print('⚪  Obteniendo los productos')
    all_products = []
    try:

        for page in pages:
            try:
                response = requests.get(page).content
                soup = BeautifulSoup(response, 'lxml') 
                scripts = soup.find_all('script', type='application/ld+json')

                for script in scripts:
                    try:
                        data = json.loads(script.string)

                        if isinstance(data, dict) and data.get('@type') == 'WebPage':
                            productos=  data['mainEntity']['offers']['itemOffered']
                            all_products.extend(productos)
                            break
                    except Exception as e:
                        fail_get_products_for_page.append(page)
                        print('Error', e)
            except Exception as e:
                fail_get_products_for_page.append(page)
        print('Ⓜ',hierarchy, f"Se encontraron {len(all_products)} productos.")
        create_dataset(all_products,hierarchy)
    except Exception as e:
        fail_get_products_for_page.append(page)
        print('🔴 falla',e,page)
