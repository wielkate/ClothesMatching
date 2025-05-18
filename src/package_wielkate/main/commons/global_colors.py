import csv

from src.package_wielkate.main.Color import Color
from src.package_wielkate.main.commons.constants import COLORS_CSV


def load_colors():
    file = open(file=COLORS_CSV, mode='r', encoding='utf-8')
    return [Color(row) for row in csv.reader(file, delimiter=',')]


global_colors = load_colors()
