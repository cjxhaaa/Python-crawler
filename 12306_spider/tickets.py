'''命令行火车票查看器


Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help    显示帮助菜单
    -g           高铁
    -d           动车
    -t           特快
    -k           快速
    -z           直达

'''

from docopt import docopt
import requests
import stations
from prettytable import PrettyTable
from colorama import init,Fore

init()
def cli():
	"""command-line interface"""
	arguments = docopt(__doc__, version='Tickets 1.0')
	from_station = stations.get_telecode(arguments.get('<from>'))
	to_station = stations.get_telecode(arguments.get('<to>'))
	train_date = arguments['<date>']
	url = ('https://kyfw.12306.cn/otn/leftTicket/query?'
		   'leftTicketDTO.train_date={}&'
		   'leftTicketDTO.from_station={}&'
		   'leftTicketDTO.to_station={}&'
		   'purpose_codes=ADULT').format(train_date,from_station,to_station)
	print(url)
	options = ''.join([
		key for key,value in arguments.items() if value is True
	])
	r = requests.get(url,verify=False)
	raw_trains = r.json()['data']['result']
	pt = PrettyTable()
	pt._set_field_names('车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split())
	for raw_train in raw_trains:
		data_list = raw_train.split('|')
		train_no = data_list[3]
		from_station_name = data_list[6]
		to_station_name = data_list[7]
		start_time = data_list[8]
		arrive_time = data_list[9]
		time_duration = data_list[10]
		first_class_seat = data_list[31] or '--'
		second_class_seat = data_list[30] or '--'
		soft_sleep = data_list[23] or '--'
		hard_sleep = data_list[28] or '--'
		hard_seat = data_list[29] or '--'
		no_seat = data_list[33] or '--'
		pt.add_row([
			train_no,
			'\n'.join([Fore.LIGHTGREEN_EX + stations.get_name(from_station_name) + Fore.RESET,Fore.RED + stations.get_name(to_station_name) + Fore.RESET]),
			'\n'.join([Fore.LIGHTGREEN_EX + start_time + Fore.RESET,Fore.RED + arrive_time + Fore.RESET]),
			time_duration,
			first_class_seat,
			second_class_seat,
			soft_sleep,
			hard_sleep,
			hard_seat,
			no_seat
		])
	print(pt)


	

if __name__ == '__main__':
	cli()