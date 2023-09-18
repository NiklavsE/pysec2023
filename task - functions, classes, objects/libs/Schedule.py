import time

class Schedule(object):
    scheduleMap = {}

    def __init__(self):
        pass

    def addEvent(self, event):
        # unix timestamp
        key = time.mktime(event.date.timetuple())
        
        if (key not in self.scheduleMap):
            self.scheduleMap[key] = [event]
        else:
            self.scheduleMap[time.mktime(event.date.timetuple())].append(event)
    
    def listEventsForDate(self, date):
        key = time.mktime(date.timetuple())

        if (key not in self.scheduleMap):
            return []
        
        return self.scheduleMap[time.mktime(date.timetuple())]



