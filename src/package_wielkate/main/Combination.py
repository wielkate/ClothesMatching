class Combination:
    def __init__(self, row):
        self.color_name = row[0]
        self.monochrome = [item.strip() for item in row[1].split(',')]
        self.analogous = [item.strip() for item in row[2].split(',')]
        self.complementary = [item.strip() for item in row[3].split(',')]
