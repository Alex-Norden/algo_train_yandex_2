"""
Родословная: LCA

В генеалогическом древе определите для двух элементов
их наименьшего общего предка.
Наименьшим общим предком элементов A и B является
такой элемент C, что С является предком A, C является
предком B, при этом глубина C является наибольшей из возможных.
При этом элемент считается своим собственным предком.
"""
import sys


def get_min_parents():
	def get_min_parent(man1, man2):
		man = man1
		visited = set([man])
		while man in child2parent:
			man = child2parent[man]
			visited.add(man)

		man = man2
		while man not in visited:
			man = child2parent[man]

		return man

	child2parent = {}

	n = int(sys.stdin.readline().strip())
	for _ in range(n - 1):
		child, parent = sys.stdin.readline().strip().split()
		child2parent[child] = parent

	ans_list = []
	for line in sys.stdin:
		man1, man2 = line.strip().split()
		ans_list.append(get_min_parent(man1, man2))
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_min_parents()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
Alexander_I Nicholaus_I
Peter_II Paul_I
Alexander_I Anna"""
out_txt_1 = """Paul_I
Peter_I
Anna"""

_assert(in_txt_1, out_txt_1)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_min_parents()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()

"""
запустить поиск от детей
сначала найти всех предков для первого
затем искать предков для второго
	продолжать пока не обнаружено совпадение (точно будет, т.к. элемент считается своим предком)
"""