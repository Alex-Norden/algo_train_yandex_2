"""
Максимальная сумма

Требуется найти непустой отрезок массива с максимальной суммой
"""
import sys


def get_max_sum():
	n = int(input())
	a = map(int, input().split())

	sm = 0
	max_sum = float("-inf")

	for x in a:
		sm += x

		if sm > max_sum:
			max_sum = sm

		if sm < 0:
			sm = 0

	return max_sum


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_max_sum()

def _assert(in_txt, out_txt):
	ans_true = int(out_txt)
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """4
1 2 3 4"""
out_txt_1 = "10"
# --------------------------
in_txt_2 = """4
5 4 -10 4"""
out_txt_2 = "9"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_max_sum()
	print(ans)


if __name__ == "__main__":
	main()