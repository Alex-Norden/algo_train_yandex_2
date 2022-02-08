"""
Форум

Выведите название темы, к которой относится наибольшее количество сообщений.
Если таких тем несколько, то выведите первую в хронологическом порядке
"""
import sys


def get_topic_title():
	n = int(input())

	msgs = [0] * (n + 1)
	topics = []
	cnt = {}

	def get_topic_index(parent):
		while msgs[parent] != 0:
			parent = msgs[parent]
		return parent #found topic

	for i in range(1, n + 1):
		parent = int(input())
		if parent == 0:
			title = input()
			input()
			topics.append((i, title))
			cnt[i] = 1
		else:
			input()
			cnt[get_topic_index(parent)] += 1
		msgs[i] = parent

	max_count = 0
	for i, count in cnt.items():
		if count > max_count:
			max_count = count

	for i, title in topics:
		count = cnt[i]
		if count == max_count:
			return title #only first


# =======================test=======================
def _test(text):
	import io
	sys.stdin = io.StringIO(text)
	return get_topic_title()

def _assert(in_txt, out_txt):
	ans_true = out_txt
	ans = _test(in_txt)
	assert ans == ans_true, f"{ans} != {ans_true}"

in_txt_1 = """7
0
Олимпиада по информатике
Скоро третья командная олимпиада?
0
Новая компьютерная игра
Вышла новая крутая игра!
1
Она пройдет 24 ноября
1
В Санкт-Петербурге и Барнауле
2
Где найти?
4
Примет участие более 50 команд
6
Интересно, какие будут задачи"""
out_txt_1 = "Олимпиада по информатике"
# --------------------------
in_txt_2 = """1
0
topic 1
body 1"""
out_txt_2 = "topic 1"

_assert(in_txt_1, out_txt_1)
_assert(in_txt_2, out_txt_2)
# =======================/test=======================


def main():
	sys.stdin = sys.__stdin__
	ans = get_topic_title()
	print(ans)


if __name__ == "__main__":
	main()

"""
считать сообщения
для сообщения найти первое(родительское), т.е. тему
найти макс. кол. сообщений
вывести все с макс. кол-ом
"""