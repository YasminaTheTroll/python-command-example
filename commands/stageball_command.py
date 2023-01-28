from subsystems.transport import TransportSubsystem
from commands2 import CommandBase

class StageBallCommand(CommandBase):
    transport: TransportSubsystem

    def __init__(self, subsystem: TransportSubsystem):
        super().__init__()

        self.transport = subsystem

        self.addRequirements(self.transport)

    def execute(self) -> None:
        self.transport.enable_innerbelt()
        self.transport.enable_outerbelt()

    def end(self) -> None:
        self.transport.disable_innerbelt()
        self.transport.disable_outerbelt()