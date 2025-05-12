import csv

from Color import Color
from Clothes import Clothes


def load_colors():
    file = open(file='Colors.csv', mode='r', encoding='utf-8')
    return [Color(row) for row in csv.reader(file, delimiter=',')]


global_colors = load_colors()
global_clothes = Clothes()
IMAGES_DIRECTORY = 'images/'
