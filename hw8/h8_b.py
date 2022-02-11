"""
Родословная: предки и потомки

В генеалогическом древе у каждого человека, кроме
родоначальника, есть ровно один родитель.

Каждом элементу дерева сопоставляется целое
неотрицательное число, называемое высотой.
У родоначальника высота равна 0, у любого другого
элемента высота на 1 больше, чем у его родителя.

Даны два элемента в дереве.
Определите, является ли один из них потомком другого.
"""
import sys
from collections import defaultdict, deque


def check_parents():
	def check_parent(man1, man2):
		def is_parent(parent, child):
			q = deque([parent])
			while q:
				man = q.popleft()
				if man == child:
					return True
				q.extend(p2childs[man])

		if is_parent(man1, man2):
			return 1
		if is_parent(man2, man1):
			return 2
		return 0

	p2childs = defaultdict(list)

	n = int(sys.stdin.readline().strip())
	for _ in range(n - 1):
		child, parent = sys.stdin.readline().strip().split()
		p2childs[parent].append(child)

	ans_list = []
	for line in sys.stdin:
		man1, man2 = line.strip().split()
		ans_list.append(check_parent(man1, man2))
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return check_parents()

def _assert(in_txt, out_txt):
	ans_true = list(map(int, out_txt.split()))
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
Anna Nicholaus_I
Peter_II Peter_I
Alexei Paul_I"""
out_txt_1 = "1 2 0 "

_assert(in_txt_1, out_txt_1)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = check_parents()
	print(*ans)


if __name__ == "__main__":
	main()

"""
т.к.граф ориентированный, то можно не исп. мн-во visited

ищем сначала среди детей первого, затем второго
"""