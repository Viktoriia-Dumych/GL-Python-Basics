# Implement python script that calculate visible color of star based on its temperature.
# The colors can be blue, white, yellow, orange and red.
# Input of the script should be dictionary where key is name of the star and value is a temperature.
# Output of the script should be colors separated by newlines that has at least one star in it spectrum and star names separated by comma.
# Script should have at least two functions: one for calculating values and one for printing it.


COLOR_SPECTRUM = {
    "purple": [28000, 49999],
    "blue": [10000, 27999],
    "white": [7500, 9999],
    "yellow": [5000, 7499],
    "orange": [3500, 4999],
    "red": [2000, 3499]
}


def color_detection(stars):
    stars_colors = {}
    for star_name, star_temperature in stars.items():
        for color, temperature_range in COLOR_SPECTRUM.items():
            if temperature_range[0] <= star_temperature <= temperature_range[1]:
                stars_colors[star_name] = color

    return stars_colors


def print_result(stars_data):
    summary = {}
    for name, color in stars_data.items():
        if color not in summary.keys():
            summary[color] = [name]
        else:
            summary[color].append(name)

    for color, stars in summary.items():
        print(color.capitalize() + ": ", end='')
        print(*stars, sep=", ")


print_result(color_detection(
    {
        "Spica": 25000,
        "Vega": 10000,
        "Sun": 6000,
        "Aldebaran": 4000,
        "Betelgeuse": 3000,
        "Rigel": 15000,
        "Sirius B": 24000,
        "Mira": 3000,
        "Meissa": 35000,
        "Orionis": 27500,
        "Scorpii": 17200,
        "Crucis": 16300,
        "Bellatrix": 21800,
        "Hydri": 11000,
        "Var B": 9000,
    }
))

