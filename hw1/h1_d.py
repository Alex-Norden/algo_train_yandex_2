"""
Строительство школы
"""
def get_coord(n, coords):
	mid = n // 2
	return coords[mid]


# =======================test=======================
assert get_coord(4, [1, 2, 3, 4]) == 3
assert get_coord(3, [-1, 0, 1]) == 0
# =======================/test=======================


def main():
	n = int(input())
	coords = tuple(map(int, input().split()))
	print(get_coord(n, coords))


if __name__ == "__main__":
	main()

"""
координаты уже отсортированы
ищем медианную координату
для нечётного случая - ответ однозначен
для чётного - можно координату любого из центральных домов
"""