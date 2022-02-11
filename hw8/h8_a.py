"""
Бинарное дерево (вставка, поиск, обход)

Обрабатывать запросы трёх видов:
ADD n
	если числа еще нет в дереве, вставлять его и выводить «DONE»
	иначе оставлять дерево как было и выводить «ALREADY»
SEARCH
	«YES» (если значение найдено в дереве)
	«NO» (если не найдено).
	Дерево при этом не меняется
PRINTTREE
	выводить все дерево
"""
import sys


cmd2index = {
	"ADD": 1,
	"SEARCH": 2
}


class Node:
	def __init__(self, key=None, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right


class BST:
	def __init__(self):
		self.root = None #корень дерева

	def height(self):
		def _height(node):
			if node is None:
				return 0
			l_h = _height(node.left)
			r_h = _height(node.right)
			h = l_h if l_h > r_h else r_h
			return h + 1

		return _height(self.root)

	def add_node(self, x):
		def _add(node, x):
			if x < node.key:
				if node.left:
					return _add(node.left, x)
				else:
					node.left = Node(x)
					return "DONE"
			elif x > node.key:
				if node.right:
					return _add(node.right, x)
				else:
					node.right = Node(x)
					return "DONE"
			return "ALREADY"

		if self.root:
			return _add(self.root, x)
		else:
			self.root = Node(x)
			return "DONE"

	def search_node(self, x): #True/None
		def _search(node, x):
			if x < node.key:
				if node.left:
					return _search(node.left, x)
			elif x > node.key:
				if node.right:
					return _search(node.right, x)
			else:
				return True

		if self.root:
			found = _search(self.root, x)
		else:
			found = False

		return "YES" if found else "NO"

	def sorted_data(self):
		"""
		при добавлении в стек увел. высоту
		при извлечении считывать
		"""
		node = self.root

		stack = []
		h = -1

		while stack or node:
			if node is not None:
				h += 1
				stack.append((node, h))
				node = node.left
			else:
				node, h = stack.pop()
				yield f"{'.' * h}{node.key}"
				node = node.right

	def get_tree(self):
		return self.sorted_data()


def get_ans_list():
	tree = BST()

	for line in sys.stdin:
		args = line.strip().split()
		cmd = args[0]

		cmd_index = cmd2index.get(cmd)
		if cmd_index == 1:
			yield tree.add_node(int(args[1]))
		elif cmd_index == 2:
			yield tree.search_node(int(args[1]))
		else:
			yield from tree.get_tree()


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return list(get_ans_list())

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """ADD 2
ADD 3
ADD 2
SEARCH 2
ADD 5
PRINTTREE
SEARCH 7"""
out_txt_1 = """DONE
DONE
ALREADY
YES
DONE
2
.3
..5
NO"""

_assert(in_txt_1, out_txt_1)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_ans_list()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()

"""
добавление
	если значение меньше, то искать крайнее место слева
	если больше - справа
"""