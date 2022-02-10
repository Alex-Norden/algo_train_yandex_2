"""
Минимальное покрытие

На прямой задано некоторое множество отрезков с целочисленными координатами концов [Li, Ri]
Выберите среди данного множества подмножество отрезков, целиком покрывающее отрезок [0, M],
(M — натуральное число), содержащее наименьшее число отрезков
"""
import sys


def get_min_count():
	M = int(input())

	arr = []
	while True:
		l, r = map(int, input().split())
		if l == r == 0:
			break

		if r > 0 and l < M:
			arr.append((l, r))

	n = len(arr)
	arr.sort()

	ans_list = []
	i = 0
	x = 0

	while i < n and x < M:
		max_r = 0
		while i < n:
			l, r = arr[i]
			if l > x:
				break

			if r > max_r:
				max_r = r
				best_i = i

			i += 1

		if max_r:
			l, r = arr[best_i]
			ans_list.append(f"{l} {r}")
			x = r
		else:
			break

	if x < M:
		# print("No solution")
		return "No solution"
	else:
		# print(len(ans_list))
		# print(*ans_list, sep="\n")
		return "{}\n{}".format(len(ans_list), "\n".join(ans_list))


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_min_count()

def _assert(in_txt, out_txt):
	ans_true = out_txt
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """1
-1 0
-5 -3
2 5
0 0"""
out_txt_1 = "No solution"
# --------------------------
in_txt_2 = """1
-1 0
0 1
0 0"""
out_txt_2 = """1
0 1"""
# --------------------------
in_txt_3 = """10
-1 2
1 9
8 12
10 15
-1 0
0 0"""
out_txt_3 = """3
-1 2
1 9
8 12"""

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_min_count()
	print(ans)


if __name__ == "__main__":
	main()

"""
искл. отрезки целиком лежащие за пределами

Найдём такой отрезок, который начинается левее или в X, а заканчивается как можно правее
Установим X равным его правой границе
Будем продолжать, пока либо не найдётся такого отрезка, либо пока X не достиг M

если X не достиг M, то решений нет
"""