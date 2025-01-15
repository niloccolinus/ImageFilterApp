from PIL import ImageEnhance # pour utiliser la méthode Contrast de ImageEnhance
from .image_filter import ImageFilter

class ContrastFilter(ImageFilter):
    def __init__(self, intensity = 0.0):
        super().__init__("Contrast", intensity) # appeler le constructeur parent

    def apply(self, image, intensity):
        print(f"Applying ContrastFilter with intensity {intensity}")
        enhancer = ImageEnhance.Contrast(image)
        return enhancer.enhance(intensity)
