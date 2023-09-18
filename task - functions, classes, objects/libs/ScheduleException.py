class ScheduleException(Exception):
    def __init__(self, errorCode):
        self.message = "Lecture schedule is not available. Service response: {}".format(errorCode)
        super().__init__(self.message)