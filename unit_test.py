import unittest # Bibliothèque utilisée pour les tests unitaires
from PIL import Image
import os
from filters.blur_filter import BlurFilter
from filters.contrast_filter import ContrastFilter
from filters.brightness_filter import BrightnessFilter
from image_manager import ImageManager

class TestImageFilterApp(unittest.TestCase):

    def setUp(self):
        self.image_manager = ImageManager()
        self.test_image_path = "images/input.jpg"
        self.image_manager.load_image(self.test_image_path)

    # Fonction pour tester le chargement d'image
    def test_load_image(self):
        self.assertIsNotNone(self.image_manager.image, "Image non chargée correctement.")

    # Fonction pour tester l'application du filtre de flou
    def test_apply_blur_filter(self):
        blur_filter = BlurFilter()
        blurred_image = blur_filter.apply(self.image_manager.image, intensity=5.0)
        self.assertIsInstance(blurred_image, Image.Image, "Le filtre de flou n'a pas renvoyé une image valide.")

    # Fonction pour tester l'application du filtre de contraste
    def test_apply_contrast_filter(self):
        contrast_filter = ContrastFilter()
        contrasted_image = contrast_filter.apply(self.image_manager.image, intensity=1.5)
        self.assertIsInstance(contrasted_image, Image.Image, "Le filtre de contraste n'a pas renvoyé une image valide.")

    # Fonction pour tester l'application du filtre de luminosité
    def test_apply_brightness_filter(self):
        brightness_filter = BrightnessFilter()
        bright_image = brightness_filter.apply(self.image_manager.image, intensity=1.2)
        self.assertIsInstance(bright_image, Image.Image, "Le filtre de luminosité n'a pas renvoyé une image valide.")

    # Fonction pour tester la sauvegarde de l'image
    def test_save_image(self):
        self.image_manager.save_image("images/output.jpg")
        self.assertTrue(os.path.exists("images/output.jpg"), "L'image n'a pas été sauvegardée.")

if __name__ == "__main__":
    unittest.main()
