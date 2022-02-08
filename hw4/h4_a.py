"""
Толя-Карп и новый набор структур, часть 2

Выведите в порядке возрастания НОМЕРА ЦВЕТА пары чисел,
каждая в новой строке: номер цвета и сумму всех чисел данного цвета
"""
import sys


def get_colors_sum():
	n = int(input())
	color2sm = {}
	for _ in range(n):
		d, a = map(int, input().split())
		if d in color2sm:
			color2sm[d] += a
		else:
			color2sm[d] = a

	ans_list = []
	for color, sm in sorted(color2sm.items()):
		# print(color, sm)
		ans_list.append(f"{color} {sm}")
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_colors_sum()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """7
1 5
10 -5
1 10
4 -2
4 3
4 1
4 0"""
out_txt_1 = """1 15
4 2
10 -5"""
# --------------------------
in_txt_2 = """5
5 -10000
-5 100000000000
10 2000000000000
-5 -300000000000
0 10000000000000"""
out_txt_2 = """-5 -200000000000
0 10000000000000
5 -10000
10 2000000000000"""

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_colors_sum()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()