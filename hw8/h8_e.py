"""
Дерево Хаффмана

Необходимо по записи обхода определить коды
для всех листьев в порядке их обхода
"""
import sys


def build_tree(serialized):
	tree = dict(left=None, right=None, up=None, type="root")
	node = tree
	for ch in serialized:
		if ch == "D":
			new_node = dict(left=None, right=None, up=node, type="left")
			node["left"] = new_node
			node = new_node
		elif ch == "U":
			while node["type"] == "right":
				node = node["up"]
			node = node["up"]
			new_node = dict(left=None, right=None, up=node, type="right")
			node["right"] = new_node
			node = new_node
	return tree

def traverse(root, prefix):
	if not root["left"] or not root["right"]:
		return ["".join(prefix)]

	prefix.append("0")
	leaf_codes = traverse(root["left"], prefix)
	prefix.pop()

	prefix.append("1")
	leaf_codes.extend(traverse(root["right"], prefix))
	prefix.pop()
	return leaf_codes

def get_leaf_codes(s):
	tree = build_tree(s)
	return traverse(tree, [])

def get_all_leaf_codes():
	n = int(input())

	ans_list = []
	for _ in range(n):
		codes = get_leaf_codes(input())
		ans_list.append(str(len(codes)))
		ans_list.extend(codes)
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_all_leaf_codes()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """2
DUDDUU
DU"""
out_txt_1 = """4
0
100
101
11
2
0
1"""

_assert(in_txt_1, out_txt_1)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_all_leaf_codes()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()