"""
Выборы в США

Выведите фамилии всех кандидатов в лексикографическом порядке,
затем, через пробел, количество отданных за них голосов
"""
import sys


def get_votes_count():
	name2votes = {}

	for line in sys.stdin:
		name, votes = line.strip().split()
		votes = int(votes)
		if name in name2votes:
			name2votes[name] += votes
		else:
			name2votes[name] = votes

	ans_list = [f"{name} {votes}" for name, votes in sorted(name2votes.items())]
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_votes_count()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """McCain 10
McCain 5
Obama 9
Obama 8
McCain 1"""
out_txt_1 = """McCain 16
Obama 17"""
# --------------------------
in_txt_2 = """ivanov 100
ivanov 500
ivanov 300
petr 70
tourist 1
tourist 2"""
out_txt_2 = """ivanov 900
petr 70
tourist 3"""
# --------------------------
in_txt_3 = "bur 1"
out_txt_3 = "bur 1"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_votes_count()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()