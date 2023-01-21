import commands2

from wpilib import Timer
from subsystems.drive import DriveSubsystem

class TimerDriveCommand(commands2.CommandBase):
    drive_subsystem: DriveSubsystem
    timer: Timer

    def __init__(self, subsystem:  DriveSubsystem, sec: float) -> None:
        super().__init__()
        self.drive_subsystem = subsystem
        self.addRequirements(self.drive_subsystem)
        self.sec = sec
        self.timer = Timer()
        
    def initialize(self) -> None:
        self.timer.start()

    def execute(self) -> None:
        self.drive_subsystem.drive(0, 0.2, 0.3)

    def end(self, interrupted: bool) -> None:
        self.timer.reset()
        self.timer.stop()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.sec)