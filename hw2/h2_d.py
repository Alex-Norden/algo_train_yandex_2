"""
Лавочки в атриуме
"""
def get_needed_blocks(length, offsets):
	mid, rem = divmod(length, 2)
	has_center_block = bool(rem)

	for offset in offsets:
		if offset < mid:
			left_block = offset
		elif has_center_block and offset == mid:
			return [offset]
		elif offset >= mid:
			right_block = offset
			return [left_block, right_block]


# =======================test=======================
assert get_needed_blocks(5, [0, 2]) == [2]
assert get_needed_blocks(13, [1, 4, 8, 11]) == [4, 8]
assert get_needed_blocks(14, [1, 6, 8, 11, 12, 13]) == [6, 8]
# =======================/test=======================


def main():
	length, k = map(int, input().split())
	offsets = tuple(map(int, input().split()))
	print(*get_needed_blocks(length, offsets))


if __name__ == "__main__":
	main()

"""
если есть центральный, то нужен только он
иначе взять последний левый и первый правый
"""