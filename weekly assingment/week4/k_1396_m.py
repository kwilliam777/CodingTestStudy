class UndergroundSystem:

    def __init__(self):
        self.ids = {}
        self.times = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ids[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.ids[id][0],stationName) not in self.times:
            self.times[(self.ids[id][0],stationName)] = [t-self.ids[id][1]]
        else:
            self.times[(self.ids[id][0],stationName)].append(t-self.ids[id][1])
           
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.times[(startStation,endStation)])/len(self.times[(startStation,endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)