import click
from math import pi

# CLI setup

@click.command()
@click.help_option('-h', '--help')
@click.option(
    '-t',
    '--triangle',
    nargs=2,
    type=float,
    default=None,
    help="Set side A and side B of a triangle.")
@click.option(
    '-r',
    '--rectangle',
    nargs=2,
    type=float,
    default=None,
    help="Set side A and side B of a rectangle.")
@click.option(
    '-c',
    '--circle',
    type=float,
    default=None,
    help="Set radius of a circle.")

# the moneyshot

def main(triangle = None, rectangle = None, circle = None):
    if triangle and None not in triangle:
        tri1, tri2 = triangle
        triangle_ans = (tri1 * tri2) / 2
        print(f"Area of triangle = {triangle_ans}")

    if rectangle and None not in rectangle:
        rec1, rec2 = rectangle
        rectangle_ans = (rec1 * rec2) / 2
        print(f"Area of rectangle = {rectangle_ans}")

    if circle != None :
        circle_ans = pi * (circle ** 2)
        print(f"Area of circle = {circle_ans}")

if __name__ == '__main__':
    main()