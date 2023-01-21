from commands2 import SubsystemBase
import ctre
from wpilib import DigitalInput

class TransportSubsystem(SubsystemBase):
    outerbelt: ctre.VictorSPX
    innerbelt: ctre.VictorSPX
    outerinput: DigitalInput
    innerinput: DigitalInput

    def __init__(self) -> None:
        super().__init__()

        self.outerbelt = ctre.VictorSPX(7)
        self.innerbelt = ctre.VictorSPX(6)
        self.outerinput = DigitalInput(4)
        self.innerinput = DigitalInput(3)

    def enable_outerbelt(self) -> None:
        self.outerbelt.set(0.5)

    def enable_innerbelt(self) -> None:
        self.innerbelt.set(-0.5)

    def disable_outerbelt(self) -> None:
        self.outerbelt.set(0)

    def disable_innerbelt(self) -> None:
        self.outerbelt.set(0)

    def outerball_input(self) -> bool:
        return self.outerinput.get()

    def innerball_input(self) -> bool:
        return self.innerinput.get()
    
    def hasbothball_input(self) -> bool:
        return self.outerinput.get() and self.innerinput.get()