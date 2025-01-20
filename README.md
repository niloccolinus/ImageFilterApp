# Image Filter Application

## Description

Image Filter Application est une application interactive en Python permettant :

    L'application de filtres sur des images (flou, contraste, luminosité).
    La détection de formes géométriques (rectangles et cercles) dans une image.
    La sauvegarde des images modifiées avec leurs dimensions d'origine.

Cette application utilise Pillow pour le traitement d'images et PySimpleGUI pour l'interface graphique.

## Installation

Prérequis

Assurez-vous que Python est installé sur votre système. Vous pouvez vérifier en exécutant :

```
python --version
```

## Dépendances

Installez les bibliothèques nécessaires en exécutant la commande suivante :

```
pip install pillow pysimplegui
```

Note : PySimpleGUI

PySimpleGUI nécessite une clé de licence gratuite pour son utilisation. Suivez les étapes fournies après l'installation pour obtenir votre clé.

## Utilisation

Lancer l'application

Pour exécuter l'application, utilisez la commande suivante dans le terminal :

```
python main.py
```

## Fonctionnalités

    ### Chargement d'une Image :
        Cliquez sur le bouton Parcourir pour sélectionner une image depuis votre système.

    ### Application des Filtres :
        Ajustez les curseurs pour appliquer des filtres :
            Flou : Ajuste l'intensité du flou.
            Contraste : Modifie le contraste de l'image.
            Luminosité : Augmente ou diminue la luminosité.

    ### Détection de Formes :
        Cliquez sur Détecter Formes pour analyser l'image et :
            Matérialiser les contours des rectangles et cercles détectés.
            Afficher le nombre de rectangles et cercles dans une boîte de dialogue.

    ### Sauvegarde :
        Cliquez sur Sauvegarder pour enregistrer l'image modifiée dans le format souhaité (.jpg ou .png).
