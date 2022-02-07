"""
Изготовление палиндромов
"""
def get_min_cost(s):
	n = len(s)
	l = (n + 1) // 2
	r = n - 1
	count_replace = n - l

	for i in range(l, n):
		if s[i] == s[r - i]:
			count_replace -= 1

	return count_replace


# =======================test=======================
assert get_min_cost("a") == 0
assert get_min_cost("ab") == 1
assert get_min_cost("cognitive") == 4
# =======================/test=======================


def main():
	s = input()
	print(get_min_cost(s))


if __name__ == "__main__":
	main()