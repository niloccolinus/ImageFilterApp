import PySimpleGUI as sg  # Bibliothèque pour l'interface graphique
from filters.blur_filter import BlurFilter
from filters.contrast_filter import ContrastFilter
from filters.brightness_filter import BrightnessFilter
from filter_manager import FilterManager
from image_manager import ImageManager
from PIL import ImageTk


# Fonction pour convertir une image Pillow en format compatible avec PySimpleGUI (ImageTk)
def convert_to_tk_image(image, max_size=(300, 300)):
    preview_image = image.copy()  # Créer une copie pour ne pas modifier l'image d'origine
    preview_image.thumbnail(max_size)  # Redimensionner l'image pour l'aperçu
    return ImageTk.PhotoImage(preview_image)


if __name__ == "__main__":
    # Initialisation des gestionnaires
    image_manager = ImageManager()
    filter_manager = FilterManager()

    # Image originale pour réinitialiser les modifications
    original_image = None

    # Définir la mise en page de la fenêtre
    sg.theme("BlueMono") # thème

    # Colonne pour les sliders et boutons
    sliders_column = [
        [sg.Text("Flou")],
        [sg.Slider(range=(0, 10), resolution=0.1, orientation="h", size=(20, 15), default_value=0, key="-BLUR-", enable_events=True)],
        [sg.Text("Contraste")],
        [sg.Slider(range=(0.1, 5), resolution=0.1, orientation="h", size=(20, 15), default_value=1.0, key="-CONTRAST-", enable_events=True)],
        [sg.Text("Luminosité")],
        [sg.Slider(range=(0.1, 5), resolution=0.1, orientation="h", size=(20, 15), default_value=1.0, key="-BRIGHTNESS-", enable_events=True)],
        [sg.Button("Sauvegarder"), sg.Button("Quitter")]
    ]

    # Colonne pour l'image
    image_column = [
        [sg.Image(key="-IMAGE-", size=(300, 300))]
    ]

    # mise en page principale
    layout = [
        [sg.Text("Choisissez une image :"), sg.Input(key="-FILE-", enable_events=True), sg.FileBrowse()],
        [sg.Column(sliders_column), sg.Column(image_column)]
    ]

    # Création de la fenêtre
    window = sg.Window("Image Filter Application", layout, finalize=True)

    # Boucle d'événements
    while True:
        event, values = window.read()

        # Si l'utilisateur ferme la fenêtre ou clique sur "Quitter"
        if event in (sg.WINDOW_CLOSED, "Quitter"):
            break

        # Si un fichier est sélectionné
        if event == "-FILE-":
            try:
                image_manager.load_image(values["-FILE-"])
                original_image = image_manager.image.copy()  # sauvegarder l'image originale
                # convertir l'image en miniature pour l'affichage
                tk_image = convert_to_tk_image(image_manager.image)
                window["-IMAGE-"].update(data=tk_image)
            except FileNotFoundError:
                sg.popup("Fichier introuvable", "L'image sélectionnée n'a pas été trouvée.")

        # Appliquer uniquement le filtre correspondant au slider déplacé
        if event in ("-BLUR-", "-CONTRAST-", "-BRIGHTNESS-"):
            if original_image:
                # Réinitialiser l'image avec l'image originale
                image_manager.image = original_image.copy()

                # Identifier le filtre à appliquer
                if event == "-BLUR-":
                    filter_to_apply = BlurFilter()
                    intensity = values["-BLUR-"]
                elif event == "-CONTRAST-":
                    filter_to_apply = ContrastFilter()
                    intensity = values["-CONTRAST-"]
                elif event == "-BRIGHTNESS-":
                    filter_to_apply = BrightnessFilter()
                    intensity = values["-BRIGHTNESS-"]

                # Appliquer le filtre correspondant
                image_manager.image = filter_manager.apply_filter(filter_to_apply, image_manager.image, intensity)

                # Mettre à jour l'affichage de l'image en miniature
                tk_image = convert_to_tk_image(image_manager.image)
                window["-IMAGE-"].update(data=tk_image)

        # Si clic sur Sauvegarder
        if event == "Sauvegarder":
            if original_image:
                # Appliquer les filtres sur une copie de l'image originale
                final_image = original_image.copy()
                filters = [
                    (BlurFilter(), values["-BLUR-"]),
                    (ContrastFilter(), values["-CONTRAST-"]),
                    (BrightnessFilter(), values["-BRIGHTNESS-"])
                ]
                final_image = filter_manager.apply_all_filters(final_image, filters)

                # Sauvegarder l'image finale avec ses dimensions originales
                save_path = sg.popup_get_file("Sauvegarder sous", save_as=True, file_types=(("Images", "*.jpg *.png"),))
                if save_path:
                    final_image.save(save_path)
                    sg.popup("Image sauvegardée", f"L'image a été sauvegardée sous {save_path}")
            else:
                sg.popup("Aucune image à sauvegarder", "Veuillez charger une image avant de la sauvegarder.")

    # Fermer la fenêtre
    window.close()
