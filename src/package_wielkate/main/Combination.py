def get_list(row):
    return [item.strip() for item in row.split(',')]


class Combination:
    def __init__(self, row):
        self.color_name = row[0]
        self.monochrome = get_list(row[1])
        self.analogous = get_list(row[2])
        self.complementary = get_list(row[3])
