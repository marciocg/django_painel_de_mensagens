from django.test import TestCase
from django.urls import reverse
from .models import Postagem


class PostModelTeste(TestCase):
    def setUp(self):
        Postagem.objects.create(texto='texto de teste')

    def teste_text_content(self):
        postagem = Postagem.objects.get(id=1)
     #   expected_object_name = f'{postagem.text}'
     #   expected_object_name = '{' + postagem.texto + '}'
        expected_object_name = postagem.texto
        self.assertEqual(expected_object_name, 'texto de teste')


class HomePageViewTest(TestCase):
    def setUp(self):
        Postagem.objects.create(texto='este é outro teste')

    def teste_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def teste_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def teste_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
