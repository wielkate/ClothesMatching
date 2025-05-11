import csv

from Color import Color


def load_colors():
    file = open(file='Colors.csv', mode='r', encoding='utf-8')
    return [Color(row) for row in csv.reader(file, delimiter=',')]


global_colors = load_colors()
