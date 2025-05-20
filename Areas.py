class rectangle:
    def __init__(self, l ,w):
        self.lenght = l 
        self.width = w
    def rectangle_area(self):
        return self.lenght * self.width

newrectangle=rectangle(12 ,10)
print ("AREA OF RECTANGLE IS : ", newrectangle.rectangle_area())