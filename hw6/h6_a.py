"""
Быстрый поиск в массиве

Отвечать на запросы вида “Cколько чисел
имеют значения от L до R?”
"""
import sys


def count_numbers_in_range():
	def lbinsearch(a, n, target):
		l = -1
		r = n
		while r - l > 1:
			mid = (l + r) // 2
			if a[mid] >= target:
				r = mid
			else:
				l = mid
		return r

	def rbinsearch(a, n, target):
		l = -1
		r = n
		while r - l > 1:
			mid = (l + r) // 2
			if a[mid] <= target:
				l = mid
			else:
				r = mid
		return l

	n = int(input())
	a = list(map(int, input().split()))

	a.sort()

	k = int(input())
	ans_list = [None] * k

	for i in range(k):
		left_val, right_val = map(int, input().split())
		left_bound = lbinsearch(a, n, left_val)
		right_bound = rbinsearch(a, n, right_val)
		if left_bound > right_bound:
			ans = 0
		else:
			ans = right_bound - left_bound + 1

		ans_list[i] = ans

	# print(*ans_list)
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return count_numbers_in_range()

def _assert(in_txt, out_txt):
	ans_true = list(map(int, out_txt.split()))
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """5
10 1 10 3 4
4
1 10
2 9
3 4
2 2"""
out_txt_1 = "5 2 2 0 "

_assert(in_txt_1, out_txt_1)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = count_numbers_in_range()
	print(*ans)


if __name__ == "__main__":
	main()

"""
отсортировать
бинпоиком по массиву левую и правую границы
если отрезок валидный, то вывести его длину
"""