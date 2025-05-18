import csv

from src.package_wielkate.main.commons.constants import COMBINATIONS_CSV
from src.package_wielkate.main.commons.global_colors import global_colors


def save_to_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def are_monochromatic(hsv1, hsv2, hue_threshold=10, saturation_threshold=10):
    """
    Check if two colors are monochromatic by comparing their HSV values.

    Parameters:
    - hsv1, hsv2: Tuples of (H, S, V) values where: H is in [0, 360], S and V are in [0, 100]
    - hue_threshold: Maximum allowed hue difference in degrees
    - saturation_threshold: Maximum allowed saturation difference in percentage
    - value_threshold: Maximum allowed brightness (value) difference in percentage

    Returns:
    - True if colors are monochromatic, False otherwise
    """
    h1, s1, v1 = hsv1
    h2, s2, v2 = hsv2

    # Check if hue difference is small (same color family)
    hue_match = abs(h1 - h2) <= hue_threshold or abs(h1 - h2) >= (360 - hue_threshold)

    # Check if saturation difference is reasonable
    saturation_match = abs(s1 - s2) <= saturation_threshold

    return hue_match and saturation_match


def monochrome_for(for_color):
    monochrome_colors = [color.name for color in global_colors if are_monochromatic(color.hsv, for_color.hsv)]
    return ', '.join(monochrome_colors)


def are_analogous(hsv1, hsv2, hue_min_threshold=10, hue_max_threshold=40, saturation_threshold=10,
                  value_threshold=10):
    """
    Check if two colors are analogous by comparing their HSV values.

    Parameters:
    - hsv1, hsv2: Tuples of (H, S, V) values where: H is in [0, 360], S and V are in [0, 100]
    - min_hue_threshold: Minimum allowed hue difference in degrees (to be different from monochrome)
    - max_hue_threshold: Maximum allowed hue difference in degrees
    - saturation_threshold: Maximum allowed saturation difference in percentage
    - value_threshold: Maximum allowed brightness (value) difference in percentage

    Returns:
    - True if colors are analogous, False otherwise
    """
    h1, s1, v1 = hsv1
    h2, s2, v2 = hsv2

    # Calculate hue difference with wrap-around
    hue_diff = abs(h1 - h2)
    hue_diff = 360 - hue_diff if hue_diff > 180 else hue_diff

    # Check thresholds
    hue_match = hue_min_threshold <= hue_diff <= hue_max_threshold
    saturation_match = abs(s1 - s2) <= saturation_threshold
    value_match = abs(v1 - v2) <= value_threshold

    return hue_match and saturation_match and value_match


def analogous_for(for_color):
    analogous_colors = [color.name for color in global_colors if are_analogous(color.hsv, for_color.hsv)]
    return ', '.join(analogous_colors)


def are_complementary(hsv1, hsv2, hue_threshold=20, saturation_threshold=20, value_threshold=20):
    """
    Check if two colors are complementary by comparing their HSV values.

    Parameters:
    - hsv1, hsv2: Tuples of (H, S, V) values where: H is in [0, 360], S and V are in [0, 100]
    - hue_threshold: Allowed deviation from 180° hue difference
    - saturation_threshold: Allowed saturation difference (in %)
    - value_threshold: Allowed brightness (value) difference (in %)

    Returns:
    - True if colors are complementary, False otherwise
    """
    h1, s1, v1 = hsv1
    h2, s2, v2 = hsv2

    # Calculate hue difference with wrap-around
    hue_diff = abs(h1 - h2)
    hue_diff = 360 - hue_diff if hue_diff > 180 else hue_diff

    # Check thresholds
    hue_match = abs(hue_diff - 180) <= hue_threshold
    saturation_match = abs(s1 - s2) <= saturation_threshold
    value_match = abs(v1 - v2) <= value_threshold

    return hue_match and saturation_match and value_match


def complementary_for(for_color):
    complementary_colors = [color.name for color in global_colors if are_complementary(color.hsv, for_color.hsv)]
    return ', '.join(complementary_colors)


# main
combinations = [
    [color.name, monochrome_for(color), analogous_for(color), complementary_for(color)]
    for color in global_colors
]
save_to_csv(COMBINATIONS_CSV, combinations)
