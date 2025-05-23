import logging
from collections import Counter

import cv2
import numpy as np
from PIL import Image

from commons.constants import IMAGES_DIRECTORY
from commons.global_colors import global_colors

logger = logging.getLogger(__name__)


def delta_e_ciede2000(lab1, lab2):
    """
    Calculate the Delta E (CIEDE2000) between two LAB colors.
    lab1 and lab2 must be (L, a, b) tuples or lists.
    """

    L1, a1, b1 = lab1
    L2, a2, b2 = lab2

    # Step 1: Calculate C, h for both colors
    C1 = np.sqrt(a1 ** 2 + b1 ** 2)
    C2 = np.sqrt(a2 ** 2 + b2 ** 2)
    C_bar = (C1 + C2) / 2

    G = 0.5 * (1 - np.sqrt((C_bar ** 7) / (C_bar ** 7 + 25 ** 7)))
    a1_prime = (1 + G) * a1
    a2_prime = (1 + G) * a2

    C1_prime = np.sqrt(a1_prime ** 2 + b1 ** 2)
    C2_prime = np.sqrt(a2_prime ** 2 + b2 ** 2)

    h1_prime = np.degrees(np.arctan2(b1, a1_prime)) % 360
    h2_prime = np.degrees(np.arctan2(b2, a2_prime)) % 360

    delta_L_prime = L2 - L1
    delta_C_prime = C2_prime - C1_prime

    delta_h_prime = 0
    if C1_prime * C2_prime != 0:
        if abs(h2_prime - h1_prime) <= 180:
            delta_h_prime = h2_prime - h1_prime
        elif h2_prime <= h1_prime:
            delta_h_prime = h2_prime - h1_prime + 360
        else:
            delta_h_prime = h2_prime - h1_prime - 360

    delta_H_prime = 2 * np.sqrt(C1_prime * C2_prime) * np.sin(np.radians(delta_h_prime / 2))

    L_bar_prime = (L1 + L2) / 2
    C_bar_prime = (C1_prime + C2_prime) / 2

    if C1_prime * C2_prime != 0:
        if abs(h1_prime - h2_prime) <= 180:
            h_bar_prime = (h1_prime + h2_prime) / 2
        elif h1_prime + h2_prime < 360:
            h_bar_prime = (h1_prime + h2_prime + 360) / 2
        else:
            h_bar_prime = (h1_prime + h2_prime - 360) / 2
    else:
        h_bar_prime = h1_prime + h2_prime

    T = 1 - 0.17 * np.cos(np.radians(h_bar_prime - 30)) \
        + 0.24 * np.cos(np.radians(2 * h_bar_prime)) \
        + 0.32 * np.cos(np.radians(3 * h_bar_prime + 6)) \
        - 0.20 * np.cos(np.radians(4 * h_bar_prime - 63))

    delta_theta = 30 * np.exp(-((h_bar_prime - 275) / 25) ** 2)
    R_C = 2 * np.sqrt((C_bar_prime ** 7) / (C_bar_prime ** 7 + 25 ** 7))
    S_L = 1 + ((0.015 * ((L_bar_prime - 50) ** 2)) / np.sqrt(20 + ((L_bar_prime - 50) ** 2)))
    S_C = 1 + 0.045 * C_bar_prime
    S_H = 1 + 0.015 * C_bar_prime * T
    R_T = -np.sin(2 * np.radians(delta_theta)) * R_C

    delta_E = np.sqrt(
        (delta_L_prime / S_L) ** 2 +
        (delta_C_prime / S_C) ** 2 +
        (delta_H_prime / S_H) ** 2 +
        R_T * (delta_C_prime / S_C) * (delta_H_prime / S_H)
    )

    return delta_E


def rgb2lab(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    def pivot_rgb(c):
        c = c / 255.0
        return (c / 12.92) if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    # 1. RGB → Linear RGB
    r_lin = pivot_rgb(rgb[0])
    g_lin = pivot_rgb(rgb[1])
    b_lin = pivot_rgb(rgb[2])

    # 2. Linear RGB → XYZ
    X = r_lin * 0.4124 + g_lin * 0.3576 + b_lin * 0.1805
    Y = r_lin * 0.2126 + g_lin * 0.7152 + b_lin * 0.0722
    Z = r_lin * 0.0193 + g_lin * 0.1192 + b_lin * 0.9505

    # Normalize by reference white D65
    X /= 0.95047
    Y /= 1.00000
    Z /= 1.08883

    def pivot_xyz(t):
        return t ** (1 / 3) if t > 0.008856 else (7.787 * t + 16 / 116)

    fx = pivot_xyz(X)
    fy = pivot_xyz(Y)
    fz = pivot_xyz(Z)

    # 3. XYZ → LAB
    L = (116 * fy) - 16
    a = 500 * (fx - fy)
    b = 200 * (fy - fz)

    return L, a, b


def closest_color_name(rgb):
    min_colors = {}
    for color in global_colors:
        diff = delta_e_ciede2000(rgb2lab(rgb), color.lab)
        min_colors[diff] = color.name
    return min_colors[min(min_colors.keys())]


def get_dominant_color_name(image: Image.Image) -> tuple[int, int, int]:
    # Convert to RGBA to ensure alpha is available
    image = image.convert("RGBA")
    np_image = np.array(image)

    # Flatten to a list of (R, G, B) ignoring fully transparent pixels
    pixels = [
        (r, g, b)
        for r, g, b, a in np_image.reshape(-1, 4)
        if a > 0 and (r, g, b) != (0, 0, 0)  # ignore background
    ]

    if not pixels:
        return 0, 0, 0  # fallback if no visible pixels

    # Count the most common color
    dominant_color = Counter(pixels).most_common(1)[0][0]
    return closest_color_name(dominant_color)


def remove(image: Image.Image) -> Image.Image:
    # Convert PIL to OpenCV image
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    # Use Canny edge detection to find object edges
    edges = cv2.Canny(gray, threshold1=50, threshold2=150)

    # Dilate and close gaps in edges to create solid contours
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # Find contours and assume the largest one is the object
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(gray)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(mask, [largest_contour], -1, (255,), thickness=cv2.FILLED)

    # Smooth the mask
    mask = cv2.GaussianBlur(mask, (7, 7), 0)
    mask = cv2.normalize(mask, None, 0, 255, cv2.NORM_MINMAX)

    # Create alpha channel from the mask
    alpha = mask.astype(np.uint8)

    # Merge BGR image with alpha channel
    b, g, r = cv2.split(cv_image)
    rgba = cv2.merge((r, g, b, alpha))

    # Convert back to PIL Image
    return Image.fromarray(rgba)


def remove_bg(filename):
    image = Image.open(filename)
    return remove(image)


def process_image_with_name(image):
    logger.info(f'Processing image with name {image}')
    image_without_bg = remove_bg(IMAGES_DIRECTORY + image)
    return get_dominant_color_name(image_without_bg)
