from django.http import response
from django.test import TestCase, RequestFactory
from buscar.models import BuscarRaças
from django.db.models.query import QuerySet

class TestBuscarViews(TestCase):

    def setUp(self):

        self.factury = RequestFactory()
        #Daqui para baixo até o end colocar depois que vejo se o test_views.py esta funcionado"
        self.buscar = BuscarRaças.objects.create(

            nome_raça = "Pinscher",
            tamanho = "Pequeno",
            inteligencia = "Alta",
            expectativa_de_vida = "15 anos"

        )
        #end#

    def test_ViewsHome(self):
    #Faço esse para ver o test_views.py esta funcionando""" 
       # response=self.client.get('/',
       #{'terra':'terra'}
       # )
    #end
    #Daqui para baixo até o end colocar depois que vejo se o test_views.py esta funcionado"
        response = self.client.get('/',
             {'buscar':'Pinscher'}
        )
        caracteristicas =response.context['terra']
        self.assertEqual(caracteristicas[0].nome_raça,'Pinscher')
    #end#
        self.assertIs(type(response.context['terra']), QuerySet)
        #Observação esse 'terra ' esta indicando na views.py#