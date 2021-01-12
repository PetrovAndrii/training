

class Stations:

    def __init__(self, from_station, to_station):
        self.from_station = from_station
        self.to_station = to_station



    def __repr__(self):
        return "%s:%s" % (self.from_station, self.to_station)