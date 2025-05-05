import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from sqlalchemy import create_engine
import time


def create_driver():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )
    options.add_argument("--disable-geolocation")
    options.add_argument("--disable-notifications")
    driver = uc.Chrome(options=options)
    return driver

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        # Registro del tiempo antes de la ejecución
        inicio = time.time()
        
        # Ejecutar la función
        resultado = func(*args, **kwargs)
        
        # Calcular el tiempo de ejecución
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"Tiempo de ejecución de {func.__name__}: {tiempo_ejecucion:.4f} segundos")
        
        return resultado
    return wrapper

driver = create_driver()
driver.get("https://www.homecenter.com.co")


# cofiguracion de cookie oara eliminar popup de ubicacion de la pagina
driver.add_cookie(
    {
        "name": "agmodal",
        "value": "1",
        "domain": "www.homecenter.com.co",
        "path": "/",
        "secure": False,
        "httpOnly": False,
    }
)
driver.refresh()


wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)


engine = create_engine("sqlite:///products.db")
