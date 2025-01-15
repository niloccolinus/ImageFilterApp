from PIL import ImageFilter as PILImageFilter # pour utiliser la méthode GaussianBlur de ImageFilter
from .image_filter import ImageFilter

class BlurFilter(ImageFilter):
    def __init__(self, intensity = 0.0):
        super().__init__("Blur", intensity) # appeler le constructeur parent

    def apply(self, image, intensity):
        print(f"Applying BlurFilter with intensity {intensity}")
        return image.filter(PILImageFilter.GaussianBlur(intensity))
