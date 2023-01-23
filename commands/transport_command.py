from commands2 import CommandBase
from subsystems.transport import TransportSubsystem

class TransportCommand(CommandBase):
    transport: TransportSubsystem

    def __init__(self, subsystem: TransportSubsystem) -> None:
        super().__init__()

        self.transport = subsystem

        self.addRequirements(self.transport)

    def execute(self) -> None:
        if self.transport.innerball_input():
            self.transport.disable_innerbelt()
        else: 
            self.transport.enable_innerbelt()

        if self.transport.hasbothball_input():
            self.transport.disable_outerbelt()
        else:
            self.transport.enable_outerbelt()

#innerinput is true turn off inner 
# if both true turn off outer