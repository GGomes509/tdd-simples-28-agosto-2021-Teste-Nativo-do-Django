from django.test import LiveServerTestCase
from selenium import webdriver

class Testesraças(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/home/gabriel123/Documentos/teste_tdd/fgh/chromedriver')
    
    def tearDown(self):
        self.browser.quit()
    
    def test_buscarraçasdechachorros(self ):

        home_page = self.browser.get(self.live_server_url + '/')

         # klack, deseja encontrar um novo animal, para adotar.
         # Ele encontra o busca animail e decide usar o site, porque ele vê no menu do site escrito busca animal.
         # Ele vê um campo para pesquisar animais pelo nome.
         # Ele pesquisa por leão e clica no botão pesquisar.
         # O site exibe 04 caracteristicas do animal pesquisando.
         # Ele desiste de adotar.
        
        menu_tag = self.browser.find_element_by_css_selector('nav.menu')
        self.assertEqual('Buscar por rasças de cachorros', menu_tag.text)

        input_busca = self.browser.find_element_by_css_selector('input.inputtag')
        self.assertEqual(input_busca.get_attribute('placeholder'),'Exemplo: Dorberman')

        input_busca.send_keys('Dorberman')
        self.browser.find_element_by_css_selector('form button').click()

        caracteristicas = self.browser.find_elements_by_css_selector('div.css')
        self.assertGreater(len(caracteristicas),3)

