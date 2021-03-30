from math import sqrt
import pandas as pd


## [Point]
class Point:
    x: float
    y: float


    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    
    def getDistanceTo(self, point):
        return sqrt((point.x - self.x)**2 + (point.y - self.y)**2)


    def duplicate(self):
        return Point(self.x, self.y)


    def toString(self):
        return f'({self.x}, {self.y})'



## [main]
def main():
    x = [1, 1, 5, 4, 4, 8, 8, 2]
    y = [5, 2, 8, 8, 9, 3, 2, 1]
    df = pd.DataFrame([x, y], columns = ['x', 'y'])
    




# Call main function
main()