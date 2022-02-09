"""
Сумма трёх

Если таких не существует, выведите единственное число -1
Иначе выведите на одной строке три числа
Элементы массивов нумеруются с нуля
Если ответов несколько, выведите лексикографически минимальный
"""
import sys


def three_sum():
	def find_min_indices(a, b, c, n1, n2, n3, s):
		max_num = s - 2
		# clear duplicate
		used = set()
		for i in range(n1):
			if a[i] > max_num or a[i] in used:
				a[i] = 0
			else:
				used.add(a[i])

		used.clear()
		for j in range(n2):
			if b[j] > max_num or b[j] in used:
				b[j] = 0
			else:
				used.add(b[j])

		used.clear()
		for k in range(n3):
			if c[k] > max_num or c[k] in used:
				c[k] = 0
			else:
				used.add(c[k])

		# value, src_index
		nums1 = [(ai, i) for i, ai in enumerate(a) if ai]
		nums2 = [(bj, j) for j, bj in enumerate(b) if bj]
		nums3 = [(ck, k) for k, ck in enumerate(c) if ck]

		nums1.sort()
		nums2.sort()
		nums3.sort()

		# new_sizes
		n1 = len(nums1)
		n2 = len(nums2)
		n3 = len(nums3)

		min_inds = (n1, n2, n3) #invalid

		for i in range(n1):
			s2 = s - nums1[i][0]

			j = 0
			k = n3 - 1

			while j < n2 and k > -1:
				sm2 = nums2[j][0] + nums3[k][0]
				if sm2 == s2:
					inds = (nums1[i][1], nums2[j][1], nums3[k][1])
					if inds < min_inds:
						min_inds = inds

					j += 1
					k -= 1
				elif sm2 < s2:
					j += 1
				elif sm2 > s2:
					k -= 1

		if min_inds == (n1, n2, n3):
			return (-1, )
		return min_inds

	s = int(input())
	n1, *a = map(int, input().split())
	n2, *b = map(int, input().split())
	n3, *c = map(int, input().split())

	return find_min_indices(a, b, c, n1, n2, n3, s)


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return three_sum()

def _assert(in_txt, out_txt):
	ans_true = tuple(map(int, out_txt.split()))
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """3
2 1 2
2 3 1
2 3 1"""
out_txt_1 = "0 1 1"
# --------------------------
in_txt_2 = """10
1 5
1 4
1 3"""
out_txt_2 = "-1"
# --------------------------
in_txt_3 = """5
4 1 2 3 4
3 5 2 1
4 5 3 2 2"""
out_txt_3 = "0 1 2"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = three_sum()
	print(*ans)


if __name__ == "__main__":
	main()

"""
почистить большие числа и дубликаты
отсортировать
пока есть куда увел/уменьш, считаем сумму и проверяем
при совпадении сдвигаем J, K
"""