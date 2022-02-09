"""
Вырубка леса
"""
def get_days(a, k, b, m, x): #lbinsearch
	def check(d):
		rest_days1 = d // k
		rest_days2 = d // m
		work_days1 = d - rest_days1
		work_days2 = d - rest_days2
		total_count = work_days1*a + work_days2*b
		return total_count >= x

	l = 0
	r = 10**20
	while r - l > 1:
		mid = (l + r) // 2
		if check(mid):
			r = mid
		else:
			l = mid
	return r


# =======================test=======================
assert get_days(1, 2, 1, 3, 10) == 8
assert get_days(1, 2, 1, 3, 11) == 9
assert get_days(19, 3, 14, 6, 113) == 4
# =======================/test=======================


def main():
	a, k, b, m, x = map(int, input().split())

	ans = get_days(a, k, b, m, x)
	print(ans)


if __name__ == "__main__":
	main()

"""
бинпоиск по ответу (кол. дней)
найти сколько дн. отдыхает
вычесть из общ. числа
кол. раб. дн. на кол. деревьев за день
если общ. кол. деревьев >= требуемого, то хорошо
"""