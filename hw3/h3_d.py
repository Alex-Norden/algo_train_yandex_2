"""
Угадай число

Вы должны вывести (через пробел, в порядке возрастания) все числа, которые мог задумать Август.
"""
import sys


def get_nums():
	n = int(input())
	used_yes = set(range(1, n + 1)) #[1..n]
	used_no = set()

	while True:
		s = input()
		if s == "HELP":
			break

		nums = set(map(int, s.split()))
		verdict = input()
		if verdict == "YES":
			used_yes.intersection_update(nums)
		else: #NO
			used_no.update(nums)

	used_yes.difference_update(used_no)
	return sorted(used_yes)


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_nums()

def _assert(in_txt, out_txt):
	ans_true = list(map(int, out_txt.split()))
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP"""
out_txt_1 = "1 3 5"
# --------------------------
in_txt_2 = """10
1 2 3 4 5 6 7 8 9 10
YES
1
NO
2
NO
3
NO
4
NO
6
NO
7
NO
8
NO
9
NO
10
NO
HELP
"""
out_txt_2 = "5"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_nums()
	print(*ans)


if __name__ == "__main__":
	main()

"""
if 'yes' -> 'yes' update
if 'no' -> 'no' update
diff
print sorted
"""