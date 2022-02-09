"""
Номер левого и правого вхождения

Определить в заданном массиве номер самого левого и
самого правого элемента, равного искомому числу
"""
import sys


def get_left_right_bounds():
	n = int(input())
	a = tuple(map(int, input().split()))
	m = int(input())
	q_list = tuple(map(int, input().split()))

	ans_list = [None] * m

	def lbinsearch(target):
		l = -1
		r = n
		while r - l > 1:
			mid = (l + r) // 2
			if a[mid] >= target:
				r = mid
			else:
				l = mid
		return r

	def rbinsearch(target):
		l = -1
		r = n
		while r - l > 1:
			mid = (l + r) // 2
			if a[mid] <= target:
				l = mid
			else:
				r = mid
		return l

	for i, q in enumerate(q_list):
		left_bound = lbinsearch(q)
		right_bound = rbinsearch(q)
		if left_bound > right_bound:
			ans_list[i] = "0 0"
		else:
			ans_list[i] = f"{str(left_bound + 1)} {str(right_bound + 1)}"

	# print("\n".join(ans_list))
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_left_right_bounds()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """4
1 2 2 3
4
4 3 2 1"""
out_txt_1 = """0 0
4 4
2 3
1 1"""
# --------------------------
in_txt_2 = """10
1 2 3 4 5 6 7 7 8 9
10
7 3 3 1 3 7 9 7 7 10"""
out_txt_2 = """7 8
3 3
3 3
1 1
3 3
7 8
10 10
7 8
7 8
0 0"""
# --------------------------
in_txt_3 = """10
1 3 3 3 3 6 8 8 9 10
10
2 9 6 4 2 9 3 7 9 7"""
out_txt_3 = """0 0
9 9
6 6
0 0
0 0
9 9
2 5
0 0
9 9
0 0"""

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_left_right_bounds()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()

"""
из-за большого вывода необходимо его кэшировать
"""