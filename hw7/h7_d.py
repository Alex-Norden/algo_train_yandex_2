"""
Наполненность котятами

Для каждого отрезка узнать его наполненность котятами —
сколько котят сидит на отрезке
"""
import sys
from collections import defaultdict


def get_cats():
	BEGIN, CAT, END = (1, 2, 3)

	n, m = map(int, input().split())
	coords = map(int, input().split())

	events = []
	l_list = [None] * m

	for lr_index in range(m):
		l, r = map(int, input().split())
		events.append((l, BEGIN, lr_index))
		events.append((r, END, lr_index))
		l_list[lr_index] = l

	for coord in coords:
		events.append((coord, CAT, 0))

	len_events = len(events)
	events.sort()

	cnt = defaultdict(int) #counter for prev cats
	cats = 0

	ans_list = [None] * m
	for i in range(len_events):
		e_type = events[i][1]
		if e_type == BEGIN:
			cnt[events[i][0]] = cats #l
		elif e_type == CAT:
			cats += 1
		elif e_type == END:
			lr_index = events[i][2]
			l = l_list[lr_index]
			ans_list[lr_index] = cats - cnt[l]

	# print(*ans_list)
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_cats()

def _assert(in_txt, out_txt):
	ans_true = list(map(int, out_txt.split()))
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """4 5
1 2 3 5
1 4
1 5
2 5
3 3
0 0"""
out_txt_1 = "3 4 3 1 0 "

_assert(in_txt_1, out_txt_1)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_cats()
	print(*ans)


if __name__ == "__main__":
	main()

"""
опр. котят на отрезке

запоминаем сколько было вначале
в конце вычитаем тех, что были вначале

*вывод в исх порядке
"""