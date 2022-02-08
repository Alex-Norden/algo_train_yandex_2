"""
Встречалось ли число раньше

Во входной строке записана последовательность чисел через пробел.
Для каждого числа выведите слово
YES (в отдельной строке), если это число ранее встречалось в посл-ти
или NO,если не встречалось.
"""
def check_used(a):
	n = len(a)
	ans_list = [None] * n
	used = set()

	for i in range(n):
		if a[i] in used:
			# print("YES")
			ans_list[i] = "YES"
		else:
			# print("NO")
			ans_list[i] = "NO"
			used.add(a[i])

	return ans_list


# =======================test=======================
assert check_used([1, 2, 3, 2, 3, 4]) == ["NO", "NO", "NO", "YES", "YES", "NO"]
# =======================/test=======================


def main():
	a = tuple(map(int, input().split()))
	print(*check_used(a), sep="\n")


if __name__ == "__main__":
	main()