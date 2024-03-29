import os
import configparser # Module pour lire et écrire des fichiers de configuration
import mplwidget # Importer le fichier mplwidget.py qui contient la classe de la figure matplotlib
import main # Importer le fichier main.py qui contient la classe principale de l'application
import appMain # Importer le fichier appMain.py qui contient la classe de l'application
from appMain import Ui_MainWindow # Importer la classe Ui_MainWindow du fichier appMain.py
import configScript # Importer le fichier config.py qui contient les fonctions pour lire et écrire des fichiers de configuration
from configScript import read_config # Importer la fonction read_config du fichier config.py

# Chemin du fichier de configuration
config_path = configScript.config_path

# Create an instance of Ui_MainWindow

def fill_ui_from_config(ui):
    if os.path.exists(config_path):
        for field, widget in fields.items():
            if field in configScript["DEFAULT"]:
                widget.setText(configScript["DEFAULT"][field])

def closeEvent(self, event):
    for field, widget in fields.items():
        configScript["DEFAULT"][field] = widget.text()
    with open(config_path, "w") as file:
        configScript.write(file)