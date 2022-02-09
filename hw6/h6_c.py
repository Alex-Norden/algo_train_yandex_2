"""
Корень кубического уравнения

a*x^3 + b*x^2 + c*x + d = 0, где a != 0
"""
import sys


def solution(a, b, c, d):
	def check(x):
		x2 = x*x
		return a*x*x2 + b*x2 + c*x >= -d

	def lbinsearch():
		l = -10**10
		r = 10**10
		for _ in range(100):
			mid = (l + r) / 2
			if check(mid):
				r = mid
			else:
				l = mid
		return r

	def rbinsearch():
		l = -10**10
		r = 10**10
		for _ in range(100):
			mid = (l + r) / 2
			if check(mid):
				l = mid
			else:
				r = mid
		return l

	increasing = bool(a > 0)
	return lbinsearch() if increasing else rbinsearch()


# =======================test=======================
eps = 1e-5
assert abs(1.0000036491 - solution(1, -3, 3, -1)) <= eps
assert abs(-1.0000000111 - solution(-1, -6, -12, -7)) <= eps
# =======================/test=======================


def main():
	sys.stdin = open("cubroot.in", "r")
	sys.stdout = open("cubroot.out", "w")

	a, b, c, d = map(int, sys.stdin.readline().strip().split())

	print(solution(a, b, c, d))


if __name__ == "__main__":
	main()