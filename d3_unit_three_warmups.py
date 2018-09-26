def area_of_circle(radius):
    area = 3.14 * radius **2
    return area

def main():
    height = 9
    radius = 12
    volume = area_of_circle(radius) * height
    print(volume)

main()