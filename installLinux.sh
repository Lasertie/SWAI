#!/bin/bash

echo "Installation des dependances pour le projet..."
# Attendre 0.5 secondes
sleep 0.5
echo "Ce script est destine a etre execute sur un systeme Linux"
echo ""
echo "Note : ce script n'a pas ete teste sur toutes les distributions Linux et peut ne pas fonctionner sur certaines d'entre elles."
echo "Merci de me faire part de vos retours si vous rencontrez des problemes ou si au contraire tout fonctionne correctement !"
echo "Veuillez appuyer sur une touche pour continuer..."
read -n 1 -s
sleep 0.5
echo "Si necessaire des fenetres peuvent s'ouvrir pour installer python..."
sleep 0.5
# Update package list
echo "Mise a jour des paquets..."
apt-get update
echo "Mise a jour terminee !"
sleep 0.5
echo "Mise a jour des paquets deja installes..."
apt-get upgrade
echo "Mise a jour terminee !"
sleep 0.5
# Python est là ?
echo "Verifions si Python est installe..."
if ! [ -x "$(command -v python3)" ]; then
echo "Oh ! Python n'est pas installé ! Ne vous inquitez pas, on s'en occupe"
apt-get install python3
echo "Ca y est, Python est installe !"
else
echo "Python est deja installe ! Genial !"
fi
sleep 0.5
# Python pip est là ?
echo "Et pip ? Il est la ?"
sleep 0.5
if ! [ -x "$(command -v pip)" ]; then
echo "Oh ! Pip n'est pas installe ! On s'en charge tout de suite !"
sleep 0.5
echo "Installation de pip..."
apt-get install python3-pip
echo "pip est enfin installe !"
else
echo "pip est deja installe ! Parfait !"
fi

# Install dependencies from requirements.txt
pip install -r /path/to/requirements.txt

echo "Installation terminee !"
sleep 0.5
echo "Vous etes prets a utiliser le projet !"
echo "Pour plus d'informations, consultez le README.md"
# demander si on veut ouvrir le README.md
echo "Voulez-vous ouvrir le README.md ? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
then
xdg-open /path/to/README.md
fi
echo "Nous allons enregistrer l historique de cette installation..."
cat /installation_history.txt
echo "Historique enregistre dans installation_history.txt"
sleep 0.5
echo "Bonne journee !"
sleep 0.5
exit 0
```