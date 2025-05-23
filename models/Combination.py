def parse_list(row):
    return [item.strip() for item in row.split(',')]


class Combination:
    def __init__(self, record):
        self.color_name = record[0]
        self.monochrome = parse_list(record[1])
        self.analogous = parse_list(record[2])
        self.complementary = parse_list(record[3])
