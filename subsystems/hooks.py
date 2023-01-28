import wpilib
from commands2 import SubsystemBase
from wpilib import DoubleSolenoid

class HooksSubsystem(SubsystemBase):
    solenoid: DoubleSolenoid

    def __init__(self) -> None:
        super().__init__()

        self.solenoid = DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 0, 7)
        self.lower_hooks()

    def raise_hooks(self) -> None:
        self.solenoid.set(DoubleSolenoid.Value.kForward)

    def lower_hooks(self) -> None:
        self.solenoid.set(DoubleSolenoid.Value.kReverse)