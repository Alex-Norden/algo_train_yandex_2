"""
Дома и магазины
"""
def get_max_distance(types):
	n = 10
	dists = [0] * n

	dist = n
	for i in range(n):
		_type = types[i]
		if _type == 2:
			dist = 0
		elif _type == 1:
			dists[i] = dist

		dist += 1

	dist = n
	for i in range(n - 1, -1, -1):
		_type = types[i]
		if _type == 2:
			dist = 0
		elif _type == 1:
			if dist < dists[i]:
				dists[i] = dist

		dist += 1

	# print(*dists)
	return max(dists)


# =======================test=======================
assert get_max_distance([2, 0, 1, 1, 0, 1, 0, 2, 1, 2]) == 3
# =======================/test=======================


def main():
	types = tuple(map(int, input().split()))
	print(get_max_distance(types))


if __name__ == "__main__":
	main()