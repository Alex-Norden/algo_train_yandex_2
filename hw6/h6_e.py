"""
Покрытие K отрезками

Даны n точек на прямой,
нужно покрыть их k отрезками одинаковой длины ℓ
Найдите минимальное ℓ
"""
def get_min_length(n, k, coords): #lbinsearch
	def check(length):
		begin = coords[0]
		count = 1
		for i in range(1, n):
			dist = coords[i] - begin
			if dist > length:
				count += 1
				begin = coords[i]
		return count <= k

	coords.sort()

	l = -1
	r = 10**11
	while r - l > 1:
		mid = (l + r) // 2
		if check(mid):
			r = mid
		else:
			l = mid
	return r


# =======================test=======================
assert get_min_length(6, 2, [1, 2, 3, 9, 8, 7]) == 2
# =======================/test=======================


def main():
	n, k = map(int, input().split())
	coords = list(map(int, input().split()))

	ans = get_min_length(n, k, coords)
	print(ans)


if __name__ == "__main__":
	main()