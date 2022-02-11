"""
Бусинки

Определить, какое максимальное количество последовательно
соединенных бусинок присутствует в полученной фигуре

*нет замкнутых фигур
"""
import sys
from collections import deque


def _solution_slow(n, g):
	def get_len(start_v):
		dists = [0] * n
		dists[start_v] = 1
		q = deque([start_v])

		while q:
			cur_v = q.popleft()
			for neigh_v in g[cur_v]:
				if not dists[neigh_v]:
					dists[neigh_v] = dists[cur_v] + 1
					q.append(neigh_v)
		return max(dists)

	max_len = 1
	for v in range(n):
		max_len = max(max_len, get_len(v))

	return max_len

def _solution_fast(n, g):
	def farthest(start_v):
		dists = [0] * n
		dists[start_v] = 1
		q = deque([start_v])

		res_v = start_v
		max_dist = 0

		while q:
			cur_v = q.popleft()
			for neigh_v in g[cur_v]:
				if not dists[neigh_v]:
					dists[neigh_v] = dists[cur_v] + 1
					q.append(neigh_v)

					if dists[neigh_v] > max_dist:
						max_dist = dists[neigh_v]
						res_v = neigh_v

		return res_v, max_dist

	v, _ = farthest(0)
	_, diameter = farthest(v)
	return diameter

def get_max_count():
	n = int(input())

	g = [[] for _ in range(n)]

	for _ in range(n - 1):
		u, v = map(int, input().split())
		u -= 1
		v -= 1
		g[u].append(v)
		g[v].append(u)

	# return _solution_slow(n, g)
	return _solution_fast(n, g)


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_max_count()

def _assert(in_txt, out_txt):
	ans_true = int(out_txt)
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """2
1 2"""
out_txt_1 = "2"
# --------------------------
in_txt_2 = """5
2 1
2 3
2 4
2 5"""
out_txt_2 = "3"
# --------------------------
in_txt_3 = """10
1 2
2 3
3 4 
4 5
1 6
6 10
10 9
9 8
8 7"""
out_txt_3 = "10"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_max_count()
	print(ans)


if __name__ == "__main__":
	main()

"""
граф представляет собой дерево, т.к. выполняются 2 свойства из 3-х:
	|V| = |E| + 1
	ацикличен

1-й способ
	O(n*n)
	от каждой бусинки до конца (находим для неё самую большую длину (расстояние))
	обновить макс. длину
2-й способ
	O(n)
	от случайной вершины ищется самая далекая - это начало диаметра
	от начала диаметра ищется самая далекая - это конец
"""