# Installation sur le roboRIO

Si ce n'est pas fait, commencez par les étapes d'[Installation sur l'ordinateur](/installation_ordinateur.md)

Commencez par installer la dernière version du firmware sur votre roboRIO ainsi que votre radio.

- [Pour le roboRIO 1](https://docs.wpilib.org/fr/stable/docs/zero-to-robot/step-3/imaging-your-roborio.html)
- [Pour le roboRIO 2](https://docs.wpilib.org/fr/stable/docs/zero-to-robot/step-3/roborio2-imaging.html)
- [Pour la radio](https://docs.wpilib.org/fr/stable/docs/zero-to-robot/step-3/radio-programming.html)

## Installation RobotPy

Le robot n'est généralement pas capable de se connecter à internet. Il faut donc réaliser les commandes en 2 temps: Connecté sur Internet puis ensuite connecté sur le robot.

Si le terminal vous demande votre numéro d'équipe, saisissez-le. Cette information permet de trouver votre roboRIO sur le réseau.

### Installation de Python sur le roboRIO

Ouvrez un terminal (Powershell sur Windows) et écrivez les commandes suivantes:

```shell
# Pour Windows
#  Connecté sur internet
py -3 -m robotpy-installer download-python
#  Puis connecté sur le robot
py -3 -m robotpy-installer install-python

# Pour Linux et macOS
#  Connecté sur internet
robotpy-installer download-python
#  Puis connecté sur le robot
robotpy-installer install-python
```

### Installation (ou mise à jour) de RobotPy sur le roboRIO

Ouvrez un terminal (Powershell sur Windows) et écrivez les commandes suivantes:

```shell
# Pour Windows
#  Connecté sur internet
py -3 -m robotpy-installer download robotpy[all]
#  Puis connecté sur le robot
py -3 -m robotpy-installer install robotpy[all]

# Pour Linux et macOS
#  Connecté sur internet
robotpy-installer download robotpy[all]
#  Puis connecté sur le robot
robotpy-installer install robotpy[all]
```

Une fois tout installé, validez le bon fonctionnement par le [Projet de Test](/patrons/projet_de_test/README.md)

Dans le cas où la commande `robotpy-installer install robotpy[all]` vous retourne une erreur de type `MemoryError`, c'est le roboRIO qui manque de place.

Recommencez la dernière commande en spécifiant les modules à installer plutôt que de tout installer. La liste suggérée est:

```shell
# Pour Windows, connecté sur le robot
py -3 -m robotpy-installer install robotpy robotpy-apriltag robotpy-commands-v2 robotpy-rev robotpy-navx robotpy-ctre

# Pour Linux et macOS, connecté sur le robot
robotpy-installer install robotpy robotpy-apriltag robotpy-commands-v2 robotpy-rev robotpy-navx robotpy-ctre
```

Si par la suite vous voulez installer une nouvelle librairie, simplement exécuter `robotpy-installer install nom_du_module`

[Voir les modules populaires](/installation_ordinateur.md#gestion-des-modules-robotpy)
