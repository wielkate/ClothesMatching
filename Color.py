from colorsys import rgb_to_hsv


class Color:
    def __init__(self, row):
        self.name = row[0]
        self.r = int(row[1])
        self.g = int(row[2])
        self.b = int(row[3])
        self.lab = self.rgb2lab()
        self.hsv = self.__get_hsv_in_degrees_and_percentage__()

    def __get_hsv_in_degrees_and_percentage__(self):
        h, s, v = rgb_to_hsv(self.r / 255, self.g / 255, self.b / 255)
        return h * 360, s * 100, v * 100

    def rgb2lab(self) -> tuple[float, float, float]:
        def pivot_rgb(c):
            c = c / 255.0
            return (c / 12.92) if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

        # 1. RGB → Linear RGB
        r_lin = pivot_rgb(self.r)
        g_lin = pivot_rgb(self.g)
        b_lin = pivot_rgb(self.b)

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
