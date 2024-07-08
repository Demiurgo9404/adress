from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_data(cc):
    # Configuración del navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Ingresar a la página y buscar el elemento
    driver.get("https://www.adres.gov.co/eps/regimen-contributivo/Paginas/afiliados-compensados.aspx")
    tipo_doc_element = driver.find_element_by_id("RblTipoDoc_7")
    tipo_doc_element.click()

    # Ingresar el número de cédula
    num_doc_element = driver.find_element_by_id("txtNumDoc")
    num_doc_element.send_keys(cc)

    # Ingresar el texto del captcha
    captcha_text_element = driver.find_element_by_id("RadCaptcha1_CaptchaTextBox")
    # Debes implementar la lógica para resolver el captcha aquí
    captcha_text_element.send_keys("solución del captcha")

    # Click en el botón de consultar
    consultar_button_element = driver.find_element_by_id("btnConsultar")
    consultar_button_element.click()

    # Capturar los datos necesarios
    primer_apellido_element = driver.find_element_by_css_selector("#RadGrid1_ctl00__0 > td:nth-child(4)")
    segundo_apellido_element = driver.find_element_by_css_selector("#RadGrid1_ctl00__0 > td:nth-child(4)")
    primer_nombre_element = driver.find_element_by_css_selector("#RadGrid1_ctl00__0 > td:nth-child(5)")
    segundo_nombre_element = driver.find_element_by_css_selector("#RadGrid1_ctl00__0 > td:nth-child(6)")
    ultimo_periodo_cotizado_element = driver.find_element_by_css_selector("#RadGrid1_ctl00__0 > td:nth-child(7)")
    eps_element = driver.find_element_by_css_selector("#RadGrid1_ctl00__0 > td:nth-child(8)")
    tipo_afiliacion_element = driver.find_element_by_css_selector("#RadGrid1_ctl00__0 > td:nth-child(9)")

    data = {
"primer_apellido": primer_apellido_element.text,
        "segundo_apellido": segundo_apellido_element.text,
        "primer_nombre": primer_nombre_element.text,
        "segundo_nombre": segundo_nombre_element.text,
        "ultimo_periodo_cotizado": ultimo_periodo_cotizado_element.text,
        "eps": eps_element.text,
        "tipo_afiliacion": tipo_afiliacion_element.text
    }

    # Cerrar el navegador
    driver.quit()

    return data