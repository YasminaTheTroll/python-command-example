from commands2 import SubsystemBase
from rev import CANSparkMax

class ShooterSubsystem(SubsystemBase):
    flywheel_motor: CANSparkMax

    def __init__(self, flywheel_motor: int) -> None:
        super().__init__()

        self.flywheel_motor = CANSparkMax(flywheel_motor, CANSparkMax.MotorType.kBrushless)

    def enable(self) -> None:
        self.flywheel_motor.set(0.5)

    def disable(self) -> None:
        self.flywheel_motor.set(0)