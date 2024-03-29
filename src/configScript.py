import os
import configparser
import appMain
import mplwidget


# Chemin du fichier de configuration
config_path = "config.ini"

# Vérifier si le fichier de configuration existe
if not os.path.exists(config_path):
    # Créer un nouveau fichier de configuration avec des valeurs par défaut
    config = configparser.ConfigParser()
    config["DEFAULT"] = {
        "version": "0.3",
        "Username": "guest",
        # champs de configuration et leurs liens avec les widgets
        "savable_fields": {
            "checkBox_davy": "",
            "checkBox_sharp": "",
            "checkBox_ISO": "",
            "checkBox_paredsimple": "",
            "largeur": "",
            "epeseur": "",
            "hauteur": "",
        },
        # path vers MATERIAUX.xlsx
        "path_materiaux": "src/MATERIAUX.xlsx",
    }
    with open(config_path, "w") as file:
        config.write(file)

# fonction pour enregistrer des valeurs dans le fichier de configuration
def save_config(key, value):
    config = configparser.ConfigParser()
    config.read(config_path)
    config["DEFAULT"][key] = value
    with open(config_path, "w") as file:
        config.write(file)

# fonction pour lire des valeurs à partir du fichier de configuration
def read_config(key):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config["DEFAULT"].get(key, None)
