# Documentation pour l'application Simple Wall Acoustic Isolation (SWAI)

## Description

L'application Simple Wall Acoustic Isolation (SWAI) est un outil simple pour calculer l'indice d'isolation acoustique d'un mur simple en utilisant [différentes méthodes](#méthodes-de-calcul). L'application permet de configurer les paramètres de calcul, de sauvegarder et de restaurer les paramètres de configuration, d'exporter les résultats des calculs dans un fichier exel et d'afficher les résultats dans un graphique.

## Fonctionnalités

- Calcul de l'indice d'isolation acoustique d'un mur simple en utilisant différentes méthodes.
- Configuration des paramètres de calcul.
- Sauvegarde et restauration des paramètres de configuration {en cours de développement}.
- Interface utilisateur simple et intuitive.
- Exportation des résultats des calculs dans un fichier exel.
- Affichage des résultats dans un graphique.

## Installation

### Code source 
#### [Installation des dependences (pour les devs)](#développement)

### Application

1. Téléchargez les fichier en cliquant sur le bouton vert `Code` en haut à droite de la page, puis en sélectionnant `Download ZIP`.
2. Décompressez le fichier dans l'emplacement de votre choix. Cela créera un dossier contenant 
    - un dossier [`src`](src) contenant le code source de l'application,
    - un dossier [`dist`](dist) contenant les fichiers compilés de l'application,
    - un dossier [`build`](build) contenant les fichiers de construction de l'application,
3. Double-cliquez sur le fichier [`main.exe`](dist/main.exe) dans le dossier [`dist`](dist) pour lancer l'application.
4. C'est tout ! Vous pouvez maintenant utiliser l'application.

## Utilisation

### Config.ini

Lorsque vous lancez l'application pour la première fois, un fichier `config.ini` est créé. Ce fichier est utilisé pour enregistrer et restaurer votre configuration. Si vous souhaitez réinitialiser les paramètres de l'application, supprimez le fichier `config.ini`.

### MATERIAUX.xlsx

Le fichier `MATERIAUX.xlsx` est utilisé pour stocker les données des matériaux. Vous pouvez ajouter, modifier ou supprimer des matériaux dans ce fichier. Les données des matériaux sont utilisées pour calculer l'indice d'isolation acoustique d'un mur simple.
Elles contient les colonnes suivantes :
- **Nom** : Nom du matériau.
- **Densité** : Densité du matériau en kg/m³.
- **Module de Young** : Module de Young du matériau en Pa.
- **Coefficient de Poisson** : Coefficient de Poisson du matériau.
- **Viscoélasticité** : Viscoélasticité du matériau.

### Interface utilisateur

#### Choix du matériau

Dans cette section, vous pouvez choisir le matériau du mur pour lequel vous souhaitez calculer l'indice d'isolation acoustique. Vous pouvez choisir un matériau dans la liste déroulante.

#### Paramètres de l'objet

Dans cette section, vous pouvez configurer les paramètres de l'objet pour lequel vous souhaitez calculer l'indice d'isolation acoustique. Vous pouvez configurer les paramètres suivants :

- **Épaisseur** : Entrez l'épaisseur du mur.
- **Hauteur** : Entrez la hauteur du mur.
- **Largeur** : Entrez la largeur du mur.

#### Commandes

Dans cette section, vous pouvez effectuer les actions suivantes :

- **Calculer** : Cliquez sur ce bouton pour calculer l'indice d'isolation acoustique du mur en utilisant les paramètres configurés.
- **Exporter** : Cliquez sur ce bouton pour exporter les résultats des calculs dans un fichier exel.
- **Supprimer** : Cliquez sur ce bouton pour réinitialiser les paramètres de calcul.

#### Résultats

Dans cette section, vous pouvez voir les résultats des calculs. Les résultats sont affichés sous forme de graphique. Vous pouvez voir l'indice d'isolation acoustique du mur en fonction de la fréquence.

#### Paramètres de calcul

Dans cette section, vous pouvez configurer les méthodes de calcul pour le calcul de l'indice d'isolation acoustique. Vous pouvez configurer les paramètres suivants :

- **[Davy](#davy)** : Cochez cette case pour activer la méthode de calcul de Davy.
- **[Sharp](#sharp)** : Cochez cette case pour activer la méthode de calcul de Sharp.
- **[ISO](#iso)** : Cochez cette case pour activer la méthode de calcul de l'ISO.
- **[Pared Simple](#pared-simple)** : Cochez cette case pour activer la méthode de calcul de la paroi simple.

### Méthodes de calcul :
Pour activer une option, cochez la case correspondante. Pour la désactiver, décochez la case.


- **Davy** : Cette méthode est basée sur la formule de Davy, qui est une méthode empirique pour calculer l'indice d'isolation acoustique d'un mur simple.

    [La formule reproduite a partir du code](#davy)
- **Sharp** : Cette méthode est basée sur la [formule de Sharp](https://en.wikipedia.org/wiki/Sound_transmission_class) 

    [La formule](#sharp)
- **ISO** : Cette méthode est basée sur [la norme ISO 12354](https://www.iso.org/obp/ui/#iso:std:iso:12354:-1:ed-1:v1:fr) 

    [La formule](#iso)
- **Pared Simple** : 

    [La formule](#pared-simple)

### Dimensions du mur

Entrez les dimensions du mur dans les champs correspondants :

- **Épaisseur** : Entrez l'épaisseur du mur.
- **Hauteur** : Entrez la hauteur du mur.
- **Largeur** : Entrez la largeur du mur.

## Expliquations

### Formules

#### Davy
Nous n'avons pas trouvé de formule de Davy, mais nous l'avons reproduite a partir du code. Voici la formule reproduite :

$$
R = \frac{-10}{N} \sum_{i=1}^{N} \log_{10}\left(\frac{A_i}{N}\right)
$$

où :

$R$ est l'indice d'isolement acoustique de la paroi (en dB),

$N$ est le nombre d'échantillons pris pour calculer la moyenne,

$A_i$​ est la transmission acoustique pour chaque échantillon $_i$, calculée à l'aide de la méthode de Davy,
La transmission acoustique $A_i$​ pour chaque échantillon est calculée à partir des caractéristiques de la paroi (densité, module de Young, viscoélasticité, etc.), des paramètres géométriques de la paroi (épaisseur, hauteur, largeur), et des fréquences $f$ considérées dans la gamme spécifiée.

#### ISO

La norme ISO 12354 est une norme internationale qui fournit des méthodes pour prédire l'isolation acoustique des éléments de construction. La formule est la suivante : 
$$
R=R_w ​+ 10\log_{10}​\left(​\frac{f_1}{f_2}\right)+C_R​+C_\Delta ​+C_\alpha +C_m​
$$

où :

- $f$ est la fréquence en Hz
- $f_0$ est la fréquence de résonance en Hz
- $xi$ est le facteur d'amortissement

#### Pared Simple

'Paroi Simple" est un concept en acoustique utilisé pour modéliser la transmission du son à travers une seule paroi. La formule de base utilisée pour cela est l'équation de la "transmission par une paroi simple" (T), qui est donnée par :

$$
R_pared_simple= \left(\frac{4Z_1Z_2}{Z_1 + Z_2}\right)^2
$$

où :

'''T''' est le coefficient de transmission de la paroi (une mesure de la quantité de son qui passe à travers la paroi),
Z1Z1​ est l'impédance acoustique du milieu d'où provient le son (par exemple, l'air),
Z2Z2​ est l'impédance acoustique du matériau constituant la paroi.

#### Sharp

La formule de Sharp est une autre équation importante en acoustique qui est utilisée pour estimer la transmission du son à travers une paroi simple. Contrairement à la formule de transmission par une paroi simple, la formule de Sharp prend en compte les effets de la masse de la paroi. Elle est souvent utilisée pour les matériaux plus lourds, comme le béton, où l'inertie de la masse joue un rôle significatif dans la transmission du son.

La formule de Sharp est donnée par :

$$
R_sharp = \left(\frac{4Z_1Z_2}{Z_1 + Z_2}\right)^2 \cdot e^{-\frac{fM}{2Z_2c}}
$$

où :

`T` est le coefficient de transmission de la paroi (une mesure de la quantité de son qui passe à travers la paroi),

`Z1`​ est l'impédance acoustique du milieu d'où provient le son (par exemple, l'air),

`Z2`​ est l'impédance acoustique du matériau constituant la paroi,

`f` est la fréquence du son,

`M` est la masse surfacique de la paroi,

`c` est la vitesse du son dans le matériau constituant la paroi.

### Pourquoi j'ai créé ce projet

Vous connaissez l'ES ? C'est une nouvelle matière du tronc commun en France. C'est une matière qui est censée nous apprendre à travailler en groupe, à faire des projets, à faire des recherches, à faire des présentations, etc. Et bien, mon groupe et moi avons décidé de faire notre 'projet experimental' sur le magnifique sujet : 
"Quelles materiaux sont les plus isolants phoniquement ?"
Et je me suis dit : "Pourquoi ne pas faire un programme qui permet de calculer l'indice d'isolation acoustique d'un mur simple ?"
Vu mes/nos connaisances en acoustique, j'ai cherché sur github un projet qui pourrait m'aider à faire ce programme. J'ai trouvé le projet [SimpleWallAcoustic Isolation](https://github.com/francobach47/SimpleWallAcousticIsolation) de [francobach47](https://github.com/francobach47/). J'ai donc décidé de prendre son code source et de le modifier pour déjà l'utiliser et pour le rendre plus simple à utiliser. J'ai donc créé ce projet.

#### Modifications apportées

- Traduction majoritaire du code source en français.
- Ajout de la possibilité de choisir l'emplacement de sauvegarde des fichiers d'exportation.
- Ajout de la possibilité de choisir le nom des fichiers d'exportation.
- Fabrication d'un fichier d'installation pour Windows/Unix.
- Construction d'une doc pour l'application.
- Ajout de la sauvegarde et de la restauration des paramètres de configuration {en cours de développement}.

## Développement

### Installation des dépendances (pour les développeurs)

#### Windows

1. Éxécutez le fichier [installWindows.bat](installWindows.bat) pour installer les dépendances nécessaires.
2. C'est tout ! Vous pouvez maintenant lancer l'application en exécutant le fichier [main.py](main.py).

#### MacOs

1. Éxécutez le fichier [installLinux.sh](installLinux.sh) pour installer les dépendances nécessaires.
    Les scripts d'installation pour MacOs et Linux sont les mêmes.(enfin normalement, je n'ai pas testé sur MacOs, donc je ne sais pas si ca fonctionne sur MacOs.)
    Au cas où ca ne fonctionne pas, vous pouvez aller voir le fichier [requirements.txt](requirements.txt) pour voir les dépendances nécessaires.
2. C'est tout ! Vous pouvez maintenant lancer l'application en exécutant le fichier [main.py](main.py).
#### Linux

1. Éxécutez le fichier [installLinux.sh](installLinux.sh) pour installer les dépendances nécessaires.
2. C'est tout ! Vous pouvez maintenant lancer l'application en exécutant le fichier [main.py](main.py).

### Compilation de l'application

Installer PyInstaller :

```bash
pip install pyinstaller
```

Compiler l'application :

```bash
pyinstaller main.py
```

Les fichiers compilés seront dans le dossier `dist`.

## Problèmes connus

- Je n'ai executé ce programme que sur Windows, donc je ne sais pas si il fonctionne sur Linux ou MacOs. Si vous avez testé ce programme sur Linux ou MacOs, n'hésitez pas à le dire.

## À faire

- Faire fonctionner la possibilité de sauvegarder et de restaurer les paramètres de configuration.
- Ajouter des options pour personnaliser les graphiques.
- (Non mais en vrai, c'est juste un projet pour simuler la physique, donc il n'y a pas grand chose à faire, mais si vous avez des idées, n'hésitez pas à les partager !)

## Crédits et remerciements

Ce projet est basé sur le projet [SimpleWallAcoustic Isolation](https://github.com/francobach47/SimpleWallAcousticIsolation) de [francobach47](https://github.com/francobach47/) et a été créé par [Lasertie](https://github.com/Lasertie) avec l'aide de [Copilot](https://copilot.github.com/). (Non mais les erreurs etait tellement grosses que je n'aurais pas pu les faire sans l'aide de Copilot, donc merci à lui ! MDR. Hé ne me jugez pas ! Je suis un bidouilleur, pas un programmeur professionnel !)

Merci à [francobach47](https://github.com/francobach47/) pour son code source qui est la base de ce projet. (Meme si il n'en sait rien, j'espère qu'il vera ce projet et qu'il sera content de voir que son travail a été utilisé pour créer un autre projet.(Bon ok, ce projet a juste une utilité educative, mais c'est deja ca))

Remarque : [francobach47](https://github.com/francobach47/) n'avait pas de licence spécifique pour son projet, donc j'ai utilisé la licence CC-BY-SA-4.0 pour ce projet. Si vous êtes le propriétaire du projet original ([francobach47](https://github.com/francobach47/)) et que vous souhaitez que je retire ce projet, veuillez m'envoyer un message et je le retirerai immédiatement(même si je ne pense pas que ce projet soit une menace pour vous, mais je comprends que vous puissiez ne pas être d'accord avec cela).

## Contributeurs

- [francobach47](https://github.com/francobach47/)
- [lasertie](https://github.com/Lasertie)
- Vous pouvez contribuer à ce projet en ouvrant des issues ou en créant des d'autres projets basés sur celui-ci.

## Licence

Ce projet est sous licence [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr).