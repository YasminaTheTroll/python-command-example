from commands2 import CommandBase
from commands.transport_command import TransportCommand

class AutoTransportCommand(TransportCommand):
    
    def isFinished(self) -> bool:
        return self.transport.hasbothball_input()
