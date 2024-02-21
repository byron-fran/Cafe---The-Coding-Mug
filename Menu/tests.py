from django.test import TestCase,RequestFactory
from .models import Menu
# Create your tests here.

class MenuTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(name="cafe", price=100, image="cafe.jpg", description="cafe exelente")
     
    def test_detail(self):
        request = self.factory.get('/menu/')
            
    def create_success_menu(self):
        name = Menu.objects.get(name="cafe")
        self.assertEqual(name=name,)    