#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Sep. 28, 2023
# This calculates the circumference of a circle using TAU.

TAU = 6.28


def main():
    # Get radius from user
    print("This program calculates the circumference of a circle in cm using TAU.")
    radius = float(input("Please enter a radius (cm): "))

    # Calculate circumference using TAU
    circumference = TAU * radius

    # Display circumference
    print("")
    print("The circumference of the circle is {:.2f}cm^2".format(circumference))


if __name__ == "__main__":
    main()
