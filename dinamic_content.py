from config import *
from static_content import *

exceptions_sections_home = ["SERVICIOS Y PROYECTOS", "PROYECTOS E INSPIRACIÓN"]        

@medir_tiempo
def di_get_popups_home():
    print('🟢  Obteniendo popup')
    hierarchy ={}
    try:

        menu_bar = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "ul.MenuDesktop-module__menu___1eRE3")
            )
        )

        # Obtener todos los <a> dentro del menú
        a_menu_bar = menu_bar.find_elements(By.TAG_NAME, "a")
        
        # Recorrer los elementos, hacer hover y extraer texto
        for item in a_menu_bar[8::]:                                                 # ⚪ Delimitar con cuantas secciones del menubar trabajar 
            hierarchy['section_name'] = item.text.strip()
            if  hierarchy['section_name']:
                if (item.text in exceptions_sections_home):  # Aqui se excluyen dos categorias de servicios
                    continue
                else:
                    # Realiza la accion de hover
                    actions.move_to_element(item).perform()

                    popup = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.CSS_SELECTOR,
                                "[class^='mega-menu-desktop s-container MenuDesktop-module__mega-menu___3cbXS']",
                            )
                        )
                    )
                    
                    get_elements_a_popup(popup,hierarchy)
            else:
                print('🔴 error de extraccion de un popup', item)       
        
    except Exception as e:
        print("🔴 No fue posible recuperar todos los popup")


def get_elements_a_popup(popup,hierarchy):
    print('🟡  Obteniendo url por familia')
    try:
        script = """
                    const popupElement = arguments[0];
                    return [...popupElement.querySelectorAll('*')].filter(el => 
                        window.getComputedStyle(el).color === 'rgb(0, 114, 206)');
                            """
        a_popup = driver.execute_script(script, popup)
        
        for a in a_popup[2:3]:                                 # ⚪ Delimitar familias por seccion a trabajar
            if a.text.strip():
                if a.text == "Ver más >":
                    continue
                else:
                    hierarchy['family_name'] = a.text.strip().replace('>','')
                    url_family =a.get_attribute("href")
                    url_family = url_family.replace('landing', 'category') 
                    get_categories(url_family,hierarchy)
            else:
                print('🔴 error de extraccion de <a> en popup', a)
    except Exception as e:
        print("🔴 error in get_link_a_popup", e)




