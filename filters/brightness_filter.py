from PIL import ImageEnhance # pour utiliser la méthode Brightness de ImageEnhance
from .image_filter import ImageFilter

class BrightnessFilter(ImageFilter):
    def __init__(self, intensity = 0.0):
        super().__init__("Brightness", intensity) # appeler le constructeur parent

    def apply(self, image, intensity):
        print(f"Applying BrightnessFilter with intensity {intensity}")
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(intensity)
