from tickets import SearchTickets


if __name__ == '__main__':
	text = input('请输入您要查询的列车信息：')
	t = str(text).lstrip('查车票').strip().split(' ')
	print(t)
	S = SearchTickets(text)
	print(S.get_train_info())