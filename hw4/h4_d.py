"""
Выборы Государственной Думы

Вывести названия всех партий и количество голосов в парламенте,
полученных данной партией. Названия необходимо выводить в
том же порядке, в котором они шли во входных данных
"""
import sys


def get_places():
	places = 450
	sm = 0
	name_v = []
	name2places = {}

	for line in sys.stdin:
		*parts, votes = line.strip().split()
		name = " ".join(parts)
		votes = int(votes)

		sm += votes
		name_v.append((name, votes))

	len_names = len(name_v)
	for_one = sm / places

	for name, votes in name_v:
		count = int(votes / for_one)
		name2places[name] = count
		places -= count

	if places:
		rem_v = [(votes % for_one, votes, name) for name, votes in name_v]
		rem_v.sort(reverse=True)

		i = 0
		while places:
			name = rem_v[i][2]
			name2places[name] += 1
			places -= 1
			i += 1

	ans_list = []
	for i in range(len_names):
		name = name_v[i][0]
		# print(name, name2places[name])
		ans_list.append(f"{name} {name2places[name]}")
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_places()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """Party One 100000
Party Two 200000
Party Three 400000"""
out_txt_1 = """Party One 64
Party Two 129
Party Three 257"""
# --------------------------
in_txt_2 = """Party number one 100
Partytwo 100"""
out_txt_2 = """Party number one 225
Partytwo 225"""
# --------------------------
in_txt_3 = """Party number one 449
Partytwo 1"""
out_txt_3 = """Party number one 449
Partytwo 1"""

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_places()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()


"""
посчитать общ. сумму
циклом исп. целую часть
если места
	отсортировать по убыванию дробной части и голосов
	пока места
		отдать место
"""