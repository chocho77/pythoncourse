import math

def area_of_circle(radius:float) -> float:
    # Area of circle formula : area = pi * r * r
    PI = math.pi
    area = radius * radius * PI

    return area




if __name__ == '__main__':
    in_radius_circle = float(input("Enter a radius of circle:"))
    area_of_circle_v = area_of_circle(in_radius_circle)
    print(f"Area of circle = {area_of_circle_v}")


