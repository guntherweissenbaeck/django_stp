from django.test import TestCase
from bird.models import Bird

class BirdTestCase(TestCase):
    def setUp(self):
        self.bird = Bird.objects.create(name="Eagle", description="Aquila")

    def test_bird_exists(self):
        """Test if the bird exists in the database."""
        bird_exists = Bird.objects.filter(name="Eagle").exists()
        self.assertTrue(bird_exists)
    
    def test_bird_does_not_exist(self):
        """Test if the bird does not exist in the database."""
        bird_exists = Bird.objects.filter(name="Hawk").exists()
        self.assertFalse(bird_exists)
    
    def test_bird_name(self):
        """Test if the bird name is correct."""
        self.assertEqual(self.bird.name, "Eagle")
    
    def test_bird_description(self):
        """Test if the bird description is correct."""
        self.assertEqual(self.bird.description, "Aquila")
    
    def test_bird_name_not_correct(self):
        """Test if the bird name is not correct."""
        self.assertNotEqual(self.bird.name, "Hawk")
    
    def test_bird_description_not_correct(self):
        """Test if the bird description is not correct."""
        self.assertNotEqual(self.bird.description, "Falco")