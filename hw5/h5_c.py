"""
Каждому по компьютеру

Выведите на первой строке число P - количество групп,
которые удастся распределить по аудиториям.
На второй строке выведите распределение групп по аудиториям –
N чисел, i-е число должно соответствовать номеру аудитории,
в которой должна заниматься i-я группа.
(Нумерация как групп, так и аудиторий, начинается с 1)
"""
import sys


def find_rooms():
	n, m = map(int, input().split())
	x = map(int, input().split())
	y = map(int, input().split())

	groups = [(xi, i) for i, xi in enumerate(x)]
	rooms = [(yj, j) for j, yj in enumerate(y)]

	groups.sort()
	rooms.sort()

	total_count = 0
	ans_list = [0] * n

	i = 0
	for j in range(m):
		g_size, g_ind = groups[i]
		r_size, r_ind = rooms[j]
		if g_size < r_size:
			total_count += 1
			ans_list[g_ind] = r_ind + 1
			i += 1 #next group

	# print(total_count)
	# print(*ans_list)
	return [total_count, ans_list]


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return find_rooms()

def _assert(in_txt, out_txt):
	lines = out_txt.split("\n")
	ans_true = [int(lines[0]), list(map(int, lines[1].split()))]
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """1 1
1
2"""
out_txt_1 = """1
1"""
# --------------------------
in_txt_2 = """1 1
1
1"""
out_txt_2 = """0
0"""

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = find_rooms()
	print(ans[0])
	print(*ans[1])


if __name__ == "__main__":
	main()