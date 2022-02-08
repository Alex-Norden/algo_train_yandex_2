"""
Автомобильные номера

Выпишите номера автомобилей, согласующиеся с максимальным количеством свидетелей
Если таких номеров несколько, то выведите их в том же порядке,
в котором они были заданы на входе
"""
import sys


def get_car_numbers():
	m = int(input())
	s1_list = [None] * m
	for i in range(m):
		s1_list[i] = set(input())

	n = int(input())
	src_list = [None] * n
	for i in range(n):
		src = input()
		s2 = set(src)

		count = 0
		for s1 in s1_list:
			if len(s2.intersection(s1)) == len(s1):
				count += 1
		src_list[i] = (src, count)

	max_count = 0
	for i in range(n):
		count = src_list[i][1]
		if count > max_count:
			max_count = count

	ans_list = []
	for i in range(n):
		count = src_list[i][1]
		if count == max_count:
			# print(src_list[i][0])
			ans_list.append(src_list[i][0])
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_car_numbers()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """3
ABC
A37
BCDA
2
A317BD
B137AC"""
out_txt_1 = "B137AC"
# --------------------------
in_txt_2 = """2
1ABC
3A4B
3
A143BC
C143AB
AAABC1"""
out_txt_2 = """A143BC
C143AB"""

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_car_numbers()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()

"""
преобразовать показания и номера в множества
пройтись по номерам
	посчитать со сколькими показаниями согласуется
найти максимум по кол-ву показаний
вывести все номера с макс. кол. показаний в исх. порядке
"""