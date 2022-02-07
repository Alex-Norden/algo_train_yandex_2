"""
Количество равных максимальному
"""
from collections import defaultdict


def get_count_max():
	cnt = defaultdict(int)
	max_val = -1

	while True:
		x = int(input())
		if x == 0:
			break

		cnt[x] += 1
		if x > max_val:
			max_val = x

	return cnt[max_val]

def _test(*arr):
	cnt = defaultdict(int)
	max_val = -1

	for x in arr:
		cnt[x] += 1
		if x > max_val:
			max_val = x

	return cnt[max_val]


# =======================test=======================
assert _test(1, 7, 9) == 1
assert _test(1, 3, 3, 1) == 2
# =======================/test=======================


def main():
	print(get_count_max())


if __name__ == "__main__":
	main()