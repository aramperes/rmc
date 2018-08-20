import datetime
import random


def get_week_colors(week=None, max_gen=256):
    if not week:
        week = datetime.datetime.now().isocalendar()[1]
    seed = week + 1234
    rand = random.Random()
    rand.seed(seed)
    colors = [(rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))
              for _ in range(max_gen)]
    return colors


def is_dark(color):
    return (0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]) < 186


def hex_color(rgb):
    return '%02x%02x%02x' % rgb
