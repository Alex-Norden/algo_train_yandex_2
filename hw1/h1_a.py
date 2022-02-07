"""
Interactor
"""
def get_total_code(r, i, c):
	if i == 0:
		return 3 if r != 0 else c
	elif i == 1:
		return c
	elif i == 4:
		return 3 if r != 0 else 4
	elif i == 6:
		return 0
	elif i == 7:
		return 1
	else:
		return i


# =======================test=======================
assert get_total_code(0, 0, 0) == 0
assert get_total_code(-1, 0, 1) == 3
assert get_total_code(42, 1, 6) == 6
assert get_total_code(44, 7, 4) == 1
assert get_total_code(1, 4, 0) == 3
assert get_total_code(-3, 2, 4) == 2
# =======================/test=======================


def main():
	r = int(input())
	i = int(input())
	c = int(input())
	print(get_total_code(r, i, c))


if __name__ == "__main__":
	main()