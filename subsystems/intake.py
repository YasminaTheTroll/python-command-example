import ctre
import wpilib
from commands2 import SubsystemBase
from wpilib import DoubleSolenoid

class IntakeSubsystem(SubsystemBase):
    spintake: ctre.VictorSPX
    solenoid: DoubleSolenoid

    def __init__(self) -> None:
        super().__init__()

        self.spintake = ctre.WPI_VictorSPX(5)
        self.solenoid = DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 3, 4)
        self.disable_sole()

    def enable_spintake(self) -> None:
        self.spintake.set(0.1)

    def enable_sole(self) -> None:
        self.solenoid.set(DoubleSolenoid.Value.kForward)

    def disable_spintake(self) -> None:
        self.spintake.set(0)

    def disable_sole(self) -> None:
        self.solenoid.set(DoubleSolenoid.Value.kReverse)

    def toggle_sole(self) -> None:
        self.solenoid.toggle()

#When up spintake should be disabled
#When down spintake should be enabled
#Should spintake constantly be enabled when
#it is down/ is there a way to enab/disab spintake
#and up/down separately