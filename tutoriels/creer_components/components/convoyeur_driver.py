from dataclasses import dataclass

import rev
import wpilib


# Classe de configuration de notre module, facultatif
@dataclass
class ConvoyeurConfig:
    vitesse_max: float = 1


class Convoyeur:
    # On définis le matériel ici, mais ne pas oublier de le déclarer dans robot.py
    # Par exemple, dans le fichier robot.py, dans la fonction `createObjects(self)`, on s'attends à retrouver les lignes:
    # convoyeur_config = ConvoyeurConfig(vitesse=0.5)
    # convoyeur_moteur = rev.CANSparkMax(5)
    # convoyeur_actuateur = wpilib.DigitalInput(0)
    config: ConvoyeurConfig
    moteur: rev.CANSparkMax
    actuateur: wpilib.DigitalInput

    def setup(self):
        """
        Appelé après l'injection
        """
        self.moteur.setOpenLoopRampRate(0.5)  # Limite l'accélération du moteur
        self.__forcer_a_tourner = False  # On crée une variable pour notre logique

    def forcer_a_tourner(self):
        """
        Force le convoyeur à tourner même si l'actuateur n'est pas activé
        """
        self.__forcer_a_tourner = True

    def execute(self):
        """
        Cette fonction est appelé à chaque itération/boucle
        C'est ici qu'on doit écrire la valeur dans nos moteurs
        """

        # on va chercher la valeur de l'actuateur
        actuateur_actif = self.actuateur.get()

        # Si l'actuateur est pressé où qu'on à reçu la commande "forcer_a_tourner_convoyeur()" le convoyeur tourne
        # Sinon, il ne tourne pas
        if actuateur_actif or self.__forcer_a_tourner:
            self.moteur.set(self.config.vitesse_max)
        else:
            self.moteur.set(0)

        # Il est important de remettre à zéro les variables utilisées
        self.__forcer_a_tourner = False
