"""
Точка и треугольник
"""
def is_in_triangle(d, x0, y0):
	x1, y1 = 0, 0 #A
	x2, y2 = d, 0 #B
	x3, y3 = 0, d #C

	points = (
		(x1, y1),
		(x2, y2),
		(x3, y3)
	)

	prod1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
	prod2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
	prod3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)

	if (prod1 >= 0 and prod2 >= 0 and prod3 >= 0) or \
	(prod1 <= 0 and prod2 <= 0 and prod3 <= 0):
		return 0
	else:
		min_dist = float("inf")
		nearest = None
		for i, p in enumerate(points, 1):
			dist = (p[0] - x0)**2 + (p[1] - y0)**2
			if dist < min_dist:
				min_dist = dist
				nearest = i
		return nearest


# =======================test=======================
assert is_in_triangle(5, 1, 1) == 0
assert is_in_triangle(3, -1, -1) == 1
assert is_in_triangle(4, 4, 4) == 2
assert is_in_triangle(4, 2, 2) == 0
# =======================/test=======================


def main():
	d = int(input())
	x0, y0 = map(int, input().split())
	print(is_in_triangle(d, x0, y0))


if __name__ == "__main__":
	main()

"""
считаются произведения (1, 2, 3 - вершины треугольника, 0 - точка):
(x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
(x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
(x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)

если одного знака, то точка принадлежит треугольнику
"""