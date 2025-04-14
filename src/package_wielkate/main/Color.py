from skimage.color import rgb2lab

class Color:
    def __init__(self, row):
        self.name = row[0]
        self.r = int(row[1])
        self.g = int(row[2])
        self.b = int(row[3])
        self.lab = rgb2lab([self.r / 255, self.g / 255, self.b / 255])
        self.rgb = (self.r, self.g, self.b)