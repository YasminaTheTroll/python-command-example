from commands2 import CommandBase
from subsystems.hooks import HooksSubsystem

class HooksCommand(CommandBase):
    hooks: HooksSubsystem

    def __init__(self, subsystem: HooksSubsystem) -> None:
        super().__init__()
        self.hooks = subsystem
        self.addRequirements(self.hooks)

    def initialize(self) -> None:
        self.hooks.raise_hooks()

    def end(self, interrupted: bool) -> None:
        self.hooks.lower_hooks()
