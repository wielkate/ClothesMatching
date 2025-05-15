class Combination:
    def __init__(self, row):
        self.color_name = row[0]
        self.monochrome = [item.strip() for item in row[1].split(',')]
