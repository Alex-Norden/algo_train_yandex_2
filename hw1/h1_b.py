"""
Кольцевая линия метро
"""
def get_between(n, l, r):
	count1 = abs(l - r) - 1
	count2 = n - count1 - 2
	return min(count1, count2)


# =======================test=======================
assert get_between(100, 5, 6) == 0
assert get_between(10, 1, 9) == 1
# =======================/test=======================


def main():
	n, l, r = map(int, input().split())
	print(get_between(n, l, r))


if __name__ == "__main__":
	main()