"""
Префиксные суммы

В этой задаче вам нужно будет много раз отвечать
на запрос «Найдите сумму чисел на отрезке в массиве»
"""
import sys


def get_sums():
	n, q = map(int, input().split())
	a = map(int, input().split())

	psum = [0] * (n + 1)
	for i, ai in enumerate(a):
		psum[i + 1] = psum[i] + ai

	for _ in range(q):
		l, r = map(int, input().split())
		l -= 1
		# print(psum[r] - psum[l])
		yield psum[r] - psum[l]


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return list(get_sums())

def _assert(in_txt, out_txt):
	ans_true = list(map(int, out_txt.split("\n")))
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """4 10
1 2 3 4
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4"""
out_txt_1 = """1
3
6
10
2
5
9
3
7
4"""

_assert(in_txt_1, out_txt_1)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_sums()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()