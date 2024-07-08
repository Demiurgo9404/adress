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
    driver.get("https://www.adres.gov.co/consulte-su-eps")
    tipo_doc_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "tipoDoc"))
    )
    tipo_doc_element.click()
    tipo_doc_option = tipo_doc_element.find_element_by_css_selector("option:nth-child(1)")
    tipo_doc_option.click()

    # Ingresar el número de cédula
    num_doc_element = driver.find_element_by_id("txtNumDoc")
    num_doc_element.send_keys(cc)

    # Validar el captcha
    captcha_image_element = driver.find_element_by_id("Capcha_CaptchaImageUP")
    captcha_text_element = driver.find_element_by_id("Capcha_CaptchaTextBox")
    # Debes implementar la lógica para resolver el captcha aquí
    captcha_text_element.send_keys("solución del captcha")

    # Click en el botón de consultar
    consultar_button_element = driver.find_element_by_id("btnConsultar")
    consultar_button_element.click()

    # Esperar a que se abra la ventana emergente
    window_handle = driver.window_handles[1]
    driver.switch_to.window(window_handle)

    # Capturar los datos necesarios
    nombre_element = driver.find_element_by_css_selector("#GridViewBasica > tbody > tr:nth-child(4) > td:nth-child(2)")
    apellidos_element = driver.find_element_by_css_selector("#GridViewBasica > tbody > tr:nth-child(5) > td:nth-child(2)")
    estado_element = driver.find_element_by_css_selector("#GridViewAfiliacion > tbody > tr.DataGrid_Item > td:nth-child(1)")
    entidad_element = driver.find_element_by_css_selector("#GridViewAfiliacion > tbody > tr.DataGrid_Item > td:nth-child(2)")

    data = {
        "nombre": nombre_element.text,
        "apellidos": apellidos_element.text,
        "estado": estado_element.text,
        "entidad": entidad_element.text
    }

    # Cerrar el navegador
    driver.quit()

    return data