
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    # Example
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    input_element = browser.find_element(By.NAME, 'q')
    input_element.send_keys('Python')
    sleep(3)
    input_element.send_keys(Keys.ENTER)
    sleep(3)
    browser.quit()



# from selenium import webdriver
# from time import sleep
#
#
# class ChromeAuto:
#     def __init__(self):
#         self.driver_path = 'chromedriver'
#         self.options = webdriver.ChromeOptions()
#         self.options.add_argument('user-data-dir=Perfil')
#         self.chrome = webdriver.Chrome(
#             self.driver_path,
#             options=self.options
#         )
#
#     def clica_sign_in(self):
#         try:
#             btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
#             btn_sign_in.click()
#         except Exception as e:
#             print('Erro ao clicar em Sign in:', e)
#
#     def acessa(self, site):
#         self.chrome.get(site)
#
#     def sair(self):
#         self.chrome.quit()
#
#     def clica_perfil(self):
#         try:
#             perfil = self.chrome.find_element_by_css_selector(
#                 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details')
#             perfil.click()
#         except Exception as e:
#             print('Erro ao clicar no perfil:', e)
#
#     def faz_logout(self):
#         try:
#             perfil = self.chrome.find_element_by_css_selector(
#                 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
#             perfil.click()
#         except Exception as e:
#             print('Erro fazer logout:', e)
#
#     def verifica_usuario(self, usuario):
#         profile_link = self.chrome.find_element_by_class_name(
#             'user-profile-link')
#         profile_link_html = profile_link.get_attribute('innerHTML')
#         assert usuario in profile_link_html
#
#     def faz_login(self):
#         try:
#             input_login = self.chrome.find_element_by_id('login_field')
#             input_password = self.chrome.find_element_by_id('password')
#             btn_login = self.chrome.find_element_by_name('commit')
#
#             input_login.send_keys('')
#             input_password.send_keys('')
#             sleep(3)
#             btn_login.click()
#
#         except Exception as e:
#             print('Erro ao fazer login:', e)
#
#
# if __name__ == '__main__':
#     chrome = ChromeAuto()
#     chrome.acessa('https://github.com/')
#
#     chrome.clica_perfil()
#     chrome.faz_logout()
#
#     chrome.clica_sign_in()
#     chrome.faz_login()
#
#     chrome.clica_perfil()
#     chrome.verifica_usuario('fulano de tal')
#
#     sleep(5)
#     chrome.sair()
