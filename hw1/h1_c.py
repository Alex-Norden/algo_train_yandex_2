"""
Даты
"""
def is_success(d, m):
	if d == m:
		return 1
	elif d > 12 or m > 12:
		return 1
	return 0


# =======================test=======================
assert is_success(1, 2) == 0
assert is_success(2, 29) == 1
# =======================/test=======================


def main():
	d, m, year = map(int, input().split())
	print(is_success(d, m))


if __name__ == "__main__":
	main()