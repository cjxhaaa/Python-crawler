from tickets import SearchTickets,SearchDetailTickets


if __name__ == '__main__':
	text = input('请输入您要查询的列车信息：')
	t = str(text).split(' ')
	print(t)
	if len(t) == 4:
		S = SearchDetailTickets(text)
		print(S.get_train_info())
	elif len(t) == 3:
		S = SearchTickets(text)
		print(S.get_train_info())