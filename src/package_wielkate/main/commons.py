import csv

from Color import Color
from Combination import Combination


def load_colors():
    file = open(file='Colors.csv', mode='r', encoding='utf-8')
    return [Color(row) for row in csv.reader(file, delimiter=',')]

def load_combinations():
    file = open(file='Combinations.csv', mode='r', encoding='utf-8')
    return [Combination(row) for row in csv.reader(file, delimiter=',')]

global_colors = load_colors()
global_combinations = load_combinations()
