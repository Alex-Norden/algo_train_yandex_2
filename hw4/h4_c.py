"""
Частотный анализ

Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке
"""
import sys
from collections import defaultdict


def get_words():
	fdict = defaultdict(int)

	for line in sys.stdin:
		for word in line.strip().split():
			fdict[word] -= 1

	res_list = [(count, w) for w, count in fdict.items()]
	res_list.sort()

	ans_list = [res_list[i][1] for i in range(len(res_list))]
	return ans_list


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_words()

def _assert(in_txt, out_txt):
	ans_true = out_txt.split("\n")
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme"""
out_txt_1 = """damme
is
name
van
bond
claude
hi
my
james
jean
what
your"""
# --------------------------
in_txt_2 = """oh you touch my tralala
mmm my ding ding dong"""
out_txt_2 = """ding
my
dong
mmm
oh
touch
tralala
you"""
# --------------------------
in_txt_3 = "ai ai ai ai ai ai ai ai ai ai"
out_txt_3 = "ai"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
_assert(in_txt_3, out_txt_3)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_words()
	print(*ans, sep="\n")


if __name__ == "__main__":
	main()

"""
подсчитать частоты слов в тексте
отсортировать список (count, word)
т.к. частоты нужно сортировать по убыванию, а слово по возрастанию (лексикографически), то будем минусовать
"""