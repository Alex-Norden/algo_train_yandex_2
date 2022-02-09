"""
Правильная, круглая, скобочная
"""
def is_correct(s):
	def _is_correct(s):
		count = 0

		for ch in s:
			if ch == "(":
				count += 1
			else:
				if count > 0:
					count -= 1
				else:
					return False

		return count == 0

	return "YES" if _is_correct(s) else "NO"


# =======================test=======================
assert is_correct("(())()") == "YES"
assert is_correct("(()))()") == "NO"
# =======================/test=======================


def main():
	print(is_correct(input()))


if __name__ == "__main__":
	main()