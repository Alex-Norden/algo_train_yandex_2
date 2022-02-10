"""
Полярные прямоугольники

Задано несколько полярных прямоугольников.
Найдите площадь их пересечения.

Помните, что пересечение полярных прямоугольников
может состоять из нескольких частей!
"""
import sys
from math import pi


def get_area():
	END, BEGIN = (1, 2)
	PI2 = pi * 2

	n = int(input())

	e = []
	r_left = 0
	r_right = 1e6

	for _ in range(n):
		r1, r2, a1, a2 = map(float, input().split())
		if a1 > a2:
			e.append((0, BEGIN))
			e.append((PI2, END))

		e.append((a1, BEGIN))
		e.append((a2, END))

		if r1 > r_left:
			r_left = r1

		if r2 < r_right:
			r_right = r2

	len_events = len(e)
	e.sort()
	c_rect = 0
	t_angle = 0.0

	for i in range(len_events):
		if c_rect == n:
			t_angle += e[i][0] - e[i - 1][0]

		e_type = e[i][1]
		if e_type == BEGIN:
			c_rect += 1
		else:
			c_rect -= 1

	# print(t_angle)
	if r_left > r_right:
		S = 0.0
	else:
		# S = Smax - Smin
		S = (r_right * r_right - r_left * r_left) * t_angle / 2

	return S


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_area()

def _assert(in_txt, out_txt):
	ans_true = float(out_txt)
	ans = _test(in_txt)
	eps = 1e-6
	assert abs(ans - ans_true) <= eps, f"{ans} | {ans_true}"

in_txt_1 = """2
1 3 0 3
2 4 1.5 4.5"""
out_txt_1 = "3.750000000"
# --------------------------
in_txt_2 = """2
1 2 0 3
1 2 2 1"""
out_txt_2 = "3.0000000000"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_area()
	print(ans)


if __name__ == "__main__":
	main()

"""
события на круге с доп размерностью

разрезаем отрезки проходящие через 0 на 2
"смотрим на пред. промежуток"
если кол-во пересекающихся прямоуг-ов было равно общему кол-ву, увел. угол сектора

опр угол сектора
выч. min/max радиус (наиб. среди левых, наим. среди правых)
S = Smax - Smin
"""