from components import convoyeur_driver
from magicbot.state_machine import timed_state

from .base_auto import BaseAuto


class IntakeAndStop(BaseAuto):
    MODE_NAME = "IntakeAndStop"
    DEFAULT = True

    # Injection
    convoyeur: convoyeur_driver.Convoyeur

    @timed_state(duration=1, next_state="finish", first=True)
    def init(self):
        # Intake 1 seconde et arrête
        self.convoyeur.forcer_a_tourner()
