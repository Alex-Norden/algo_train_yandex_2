"""
Таможня

Выведите одно число – наименьшее количество аппаратов,
которое нужно установить, чтобы не вызвать подозрений у Министерства
"""
import sys


def get_min_count():
	END, BEGIN = range(2)

	n = int(input())

	len_events = n * 2
	events = [None] * len_events
	for i in range(1, len_events, 2):
		t, l = map(int, input().split())
		events[i - 1] = (t, BEGIN) #coord, e_type
		events[i] = ((t + l), END)

	events.sort()

	count = max_count = 0

	for i in range(len_events):
		if events[i][1] == BEGIN:
			count += 1
			if count > max_count:
				max_count = count
		else:
			count -= 1

	return max_count


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_min_count()

def _assert(in_txt, out_txt):
	ans_true = int(out_txt)
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """3
3 2
4 2
5 2"""
out_txt_1 = "2"
# --------------------------
in_txt_2 = """5
13 4
15 1
11 5
12 3
10 3"""
out_txt_2 = "3"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_min_count()
	print(ans)


if __name__ == "__main__":
	main()

"""
чтобы опр. мин. кол. аппаратов, нужно опр. макс. кол. грузов, осматриваемых одновременно
"""