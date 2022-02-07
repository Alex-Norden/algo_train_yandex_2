"""
Дипломы в папках
"""
def get_min_sec(a):
	return sum(a) - max(a)


# =======================test=======================
assert get_min_sec([2, 1]) == 1
assert get_min_sec([1, 10, 5, 4, 6]) == 16
# =======================/test=======================


def main():
	n = int(input())
	a = tuple(map(int, input().split()))
	print(get_min_sec(a))


if __name__ == "__main__":
	main()

"""
не просматривать самую толстую папку
"""