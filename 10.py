import math

def calculate_regular_polygon_area(s, n):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area

s = float(input("Введіть довжину сторони: "))
n = int(input("Введіть кількість сторін: "))

area = calculate_regular_polygon_area(s, n)
print(f"Площа регулярного многокутника з {n} сторонами та довжиною сторони {s} дорівнює {area:.2f}")
