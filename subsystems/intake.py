import ctre
from commands2 import SubsystemBase
from wpilib import DoubleSolenoid

class IntakeSubsystem(SubsystemBase):
    spintake: ctre.VictorSPX
    solenoid: DoubleSolenoid

    def __init__(self) -> None:
        super().__init__()

        self.spintake = ctre.WPI_VictorSPX()
        self.solenoid = DoubleSolenoid

    def 
