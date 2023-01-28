from commands2 import CommandBase
from subsystems.intake import IntakeSubsystem

class IntakeCommand(CommandBase):
    intake: IntakeSubsystem

    def __init__(self, subsystem: IntakeSubsystem) -> None:
        super().__init__()

        self.intake = subsystem

        self.addRequirements(self.intake)

    def initialize(self) -> None:
        self.intake.enable_sole()
        self.intake.enable_spintake()

    def end(self, interrupted: bool) -> None:
        self.intake.disable_sole()
        self.intake.disable_spintake()