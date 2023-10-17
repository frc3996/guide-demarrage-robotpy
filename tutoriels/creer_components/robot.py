#!/usr/bin/env python3

"""
Example création d'un composante ('component')
"""

import rev
import wpilib
from common import gamepad_helper as gh
from components import convoyeur_driver  # Le fichier avec notre component
from magicbot import MagicRobot


class MyRobot(MagicRobot):
    """
    Après avoir créer notre composante 'convoyeur_driver' de bas niveau dans './components/convoyeur_driver.py',
    utiliser leur nom suivi d'un trait souligné (_) pour injecter des objets au composantes.

    Utilisez le signe = dans la fonction 'createObjects' pour vous assurer que les données sont biens transmises à leur composantes.

    Pour plus d'information (en anglais): https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    """

    # Ici on définie l'objet qui nous permet d'interragir avec le component
    convoyeur: convoyeur_driver.Convoyeur

    def createObjects(self):
        """
        C'est ici que les composants sont vraiment créé avec le signe =.
        Les composants avec un préfix connu tel que "convoyeur_" vont être injectés.
        """
        self.convoyeur_config = convoyeur_driver.ConvoyeurConfig(vitesse_max=0.5)
        self.convoyeur_moteur = rev.CANSparkMax(5, rev.CANSparkMax.MotorType.kBrushless)
        self.convoyeur_actuateur = wpilib.DigitalInput(0)

        # General
        self.gamepad1 = wpilib.Joystick(0)

    def disabledPeriodic(self):
        """Mets à jours le dashboard, même quand le robot est désactivé"""
        pass

    def autonomousInit(self):
        """Cette fonction est appelée une seule fois lorsque le robot entre en mode autonome."""
        pass

    def autonomous(self):
        """Pour les modes auto de MagicBot, voir le dossier ./autonomous"""
        super().autonomous()

    def teleopInit(self):
        """Cette fonction est appelée une seule fois lorsque le robot entre en mode téléopéré."""
        pass

    def teleopPeriodic(self):
        """Cette fonction est appelée de façon périodique lors du mode téléopéré."""
        # Forcer le convoyeur à tourner
        if self.gamepad1.getRawButton(gh.BUTTON_A):
            self.convoyeur.forcer_a_tourner()


if __name__ == "__main__":
    wpilib.run(MyRobot)
