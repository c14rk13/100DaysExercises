import colorgram


def extract_colors(file_name):
    rgb_list = []  # List of rgb tuples
    colors = colorgram.extract(file_name,20)

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if not (r > 240 and g > 240 and b > 240): # Only get colors that are not white/background
            rgb_color = (color.rgb.r, color.rgb.g, color.rgb.b)
            rgb_list.append(rgb_color)

    return rgb_list


color_list = extract_colors.py("Hirst_ColorPalette.jpg")