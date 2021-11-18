from counter import *

class Clock(object):
    """ a 24-hour clock object, made of three counter objects: one for the seconds
        (0->59), one for the minutes (0->59), and one for the hour (0->23).  """

    def __init__(self, hour, min, sec):
        """ construct counter obj, given hours minutes and seconds """
        self.hour = Counter(24)
        self.hour.setValue(hour)
        self.minutes = Counter(60)
        self.minutes.setValue(min)
        self.seconds = Counter(60)
        self.seconds.setValue(sec)

    def __str__(self):
        return self.getTime()

    def getTime(self):
        strHours = str(self.getHour())
        strMinutes = str(self.getMinutes())
        strSeconds = str(self.getSeconds())
        return "Clock: %s:%s:%s" % ("0" * (2-len(strHours)) + strHours,"0" * (2-len(strMinutes)) + strMinutes,"0" * (2-len(strSeconds)) + strSeconds)

    def setHour(self, hour):
        if hour >= 0 and hour < 24:
            self.hour.setValue(hour)

    def setMinutes(self, mins):
        if mins >= 0 and mins < 60:
            self.minutes.setValue(mins)

    def setSeconds(self, secs):
        if secs >= 0 and secs < 60:
            self.seconds.setValue(secs)

    def getHour(self):
        return self.hour.getValue()
    
    def getMinutes(self):
        return self.minutes.getValue()

    def getSeconds(self):
        return self.seconds.getValue()

    def tick(self):
        self.seconds.increment()
        if self.getSeconds() == 0:
            self.minutes.increment()
            if self.getMinutes() == 0:
                self.hour.increment()




    ###  MORE METHODS TO BE IMPLEMENTED BY YOU  ###



if __name__ == "__main__":
    c1 = Clock(12,55,21)
    print(c1)
    print("Setting time to 23:59:55...")
    c1.setHour(23)
    c1.setMinutes(59)
    c1.setSeconds(55)
    print("Hour for c1: %d" % (c1.getHour()))
    print(c1)
    for i in range(15):
        c1.tick()
        print(c1)
