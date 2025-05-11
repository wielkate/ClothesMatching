import colorsys
import csv

from commons import global_colors


def save_to_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)  # Write rows


def are_monochromatic(rgb1, rgb2, hue_threshold=10, sat_threshold=50):
    # Convert RGB to HSV
    h1, s1, v1 = colorsys.rgb_to_hsv(*[x / 255.0 for x in rgb1])
    h2, s2, v2 = colorsys.rgb_to_hsv(*[x / 255.0 for x in rgb2])

    # Convert hue to degrees (0-360), and saturation to percentage (0-100)
    h1, s1, v1 = h1 * 360, s1 * 100, v1 * 100
    h2, s2, v2 = h2 * 360, s2 * 100, v2 * 100

    # Check if hue difference is small (same color family)
    hue_match = abs(h1 - h2) <= hue_threshold or abs(h1 - h2) >= (360 - hue_threshold)

    # Check if saturation difference is reasonable
    saturation_match = abs(s1 - s2) <= sat_threshold

    return hue_match and saturation_match


def return_monochrome_colors(for_color):
    monochrome_colors = [color.name for color in global_colors if
                         are_monochromatic(color.rgb, for_color.rgb) and color.name != for_color.name]
    return ', '.join(monochrome_colors)


# main
monochrome_combinations = [[color.name, return_monochrome_colors(color)] for color in global_colors]
save_to_csv("Combinations.csv", monochrome_combinations)
