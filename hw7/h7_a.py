"""
Закраска прямой

На числовой прямой окрасили N отрезков
Известны координаты левого и правого концов каждого отрезка (Li и Ri)
Найти длину окрашенной части числовой прямой
"""
import sys


def get_length():
	END, BEGIN = range(2)

	n = int(input())

	len_events = n * 2
	events = [None] * len_events
	for i in range(1, len_events, 2):
		l, r = map(int, input().split())
		events[i - 1] = (l, BEGIN) #coord, e_type
		events[i] = (r, END)

	events.sort()

	count_cover = 0
	total_dist = 0

	for i in range(len_events):
		if count_cover: #>0
			total_dist += events[i][0] - events[i - 1][0]

		if events[i][1] == BEGIN:
			count_cover += 1
		else:
			count_cover -= 1

	return total_dist


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_length()

def _assert(in_txt, out_txt):
	ans_true = int(out_txt)
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """1
10 20"""
out_txt_1 = "10"
# --------------------------
in_txt_2 = """1
10 10"""
out_txt_2 = "0"
# --------------------------
in_txt_3 = """2
10 20
20 40"""
out_txt_3 = "30"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_length()
	print(ans)


if __name__ == "__main__":
	main()

"""
т.к. отрезок не может закончиться не начавшись, то count_cover не будет отриц-м
"""