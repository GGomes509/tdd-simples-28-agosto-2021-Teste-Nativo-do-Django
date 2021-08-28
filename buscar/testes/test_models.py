from django.test import TestCase, RequestFactory
from buscar.models import BuscarRaças

class TesteModelAppBuscar(TestCase):

    def setUp(self):
        self.buscar = BuscarRaças.objects.create(

            nome_raça = "Doberman",
            tamanho = "Arande",
            inteligencia = "Alta",
            expectativa_de_vida = "de 10 a 12 anos"

        )

    def test_buscar(self):
        """Teste que varifica se o cachorro esta com suas caracteristicas"""
        self.assertEqual(self.buscar.nome_raça,"Doberman")