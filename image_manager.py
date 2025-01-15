from PIL import Image # pour utiliser les méthodes open, show et save de Image

class ImageManager:
    def __init__(self):
        self.image = None

    # Méthode pour charger une image depuis un fichier
    def load_image(self, path):    
        try:
            self.image = Image.open(path)
            print(f"Image loaded from: {path}")
        # on lance une exception si le fichier est introuvable
        except FileNotFoundError:
            print(f"Image '{path}' not found.")
            raise

    # Méthode pour afficher l'image
    def display_image(self):
        if self.image:
            self.image.show()
        else:
            print("No image to display.")

    # Méthode pour sauvegarder l'image dans un fichier
    def save_image(self, path):
        if self.image:
            self.image.save(path)
            print(f"Image saved in: {path}")
        else:
            print("No image to save.")
