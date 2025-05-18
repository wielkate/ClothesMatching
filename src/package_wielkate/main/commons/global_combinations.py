import csv

from src.package_wielkate.main.Combination import Combination
from src.package_wielkate.main.commons.constants import COMBINATIONS_CSV


def load_combinations():
    file = open(file=COMBINATIONS_CSV, mode='r', encoding='utf-8')
    return [Combination(row) for row in csv.reader(file, delimiter=',')]


global_combinations = load_combinations()
