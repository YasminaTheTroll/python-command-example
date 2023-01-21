from subsystems.shooter import ShooterSubsystem
import commands2

class ShooterCommand(commands2.CommandBase):
    shooter_subsystem: ShooterSubsystem

    def __init__(self, subsystem: ShooterSubsystem) -> None:
        super().__init__()
        self.shooter_subsystem = subsystem
        self.addRequirements(self.shooter_subsystem)

    def initialize(self) -> None:
        pass

    def execute(self) -> None:
        self.shooter_subsystem.enable()

    def end(self, interrupted: bool) -> None:
        self.shooter_subsystem.disable()
        print ("ending")

    def isFinished(self) -> bool:
        return False