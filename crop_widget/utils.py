from fractions import gcd


def aspect_ratio(width, height):
    g = gcd(width, height)
    return "{}:{}".format(width/g, height/g)
