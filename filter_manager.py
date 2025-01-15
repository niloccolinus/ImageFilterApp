class FilterManager:
    def __init__(self):
        self.filters = [] # Initialisation d'une liste pour stocker les filtres

    # Méthode pour appliquer un filtre spécifique à une image
    def apply_filter(self, image_filter, image, intensity):
        return image_filter.apply(image, intensity)
    
    # Méthode pour appliquer plusieurs filtres (utilisée lors de la sauvegarde de l'image finale)
    def apply_all_filters(self, image, filters):
        for image_filter, intensity in filters:
            image = self.apply_filter(image_filter, image, intensity)
        return image

