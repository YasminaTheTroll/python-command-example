from subsystems.intake import IntakeSubsystem
from wpilib import Timer
from commands2 import CommandBase

class TimerIntakeCommand(CommandBase):
    intake: IntakeSubsystem
    timer: Timer

    def __init__(self, subsystem: IntakeSubsystem, sec: float) -> None:
        super().__init__()
        self.intake = subsystem
        self.addRequirements(self.intake)
        self.sec = sec
        self.timer = Timer()

    def initialize(self) -> None:
        self.timer.start()
        self.intake.enable_sole()
        self.intake.enable_spintake()

    def end(self, interrupted: bool) -> None:
        self.timer.reset()
        self.timer.stop()
        self.intake.disable_sole()
        self.intake.disable_spintake()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.sec)