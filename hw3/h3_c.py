"""
Уникальные элементы

Дан список.
Выведите те его элементы, которые встречаются в списке только один раз
Элементы нужно выводить в том порядке, в котором они встречаются в списке
"""
def get_uniq(a):
	from collections import defaultdict
	cnt = defaultdict(int)

	for x in a:
		cnt[x] += 1

	return [x for x, count in cnt.items() if count == 1]


# =======================test=======================
assert get_uniq([1, 2, 2, 3, 3, 3]) == [1]
assert get_uniq([4, 3, 5, 2, 5, 1, 3, 5]) == [4, 2, 1]
# =======================/test=======================


def main():
	a = map(int, input().split())
	print(*get_uniq(a))


if __name__ == "__main__":
	main()