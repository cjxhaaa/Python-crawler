import requests
import time
from stations import Station


# text = '查车票 D 绍兴 上海 20170910'
fast_model = ['G','D','C']
slow_model = ['Z','T','K']
HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Cookie':('JSESSIONID=88B44190EFEF0469C7E19B33B15B8BEE; '
				'route=6f50b51faa11b987e576cdb301e545c4; '
				'BIGipServerotn=804258314.64545.0000; '
				'fp_ver=4.5.1; '
				'RAIL_EXPIRATION=1505221983857; '
				'RAIL_DEVICEID=LkRpgNI0_P0XagbwcBqyjGuuGRDWiO0AVKpBjCPshxVb67Z1IQTP4DfBjWeD6bdzjNntQp3Q653oX3yy4mjTS3crmkiWz7E00TAxsfUEk8cF1i74G0xUJ66shorxgHOtOyD_TGIYjsH9NhMSdb1lhiKwDqCAjE4s; '
				'_jc_save_fromStation=%u7ECD%u5174%u5317%2CSLH; '
				'_jc_save_toStation=%u4E0A%u6D77%u5357%2CSNH; '
				'_jc_save_fromDate=2017-09-10; '
				'_jc_save_toDate=2020-09-30; '
				'_jc_save_wfdc_flag=dc')
	}

class Tickets(object):
	"""docstring for Tickets"""
	def __init__(self, arg):
		self.headers = HEADERS
		self.fast_model = fast_model
		self.slow_model = slow_model
		self.station = Station()	
		self.trains_info = []

	

	def fast_info(self,*args):
		info = ('车次:{}\n出发站:{}，目的地:{}\n出发时间:{}，到达时间:{}\n耗时:{}\n'
						'座位情况：\n一等座：{}\n二等座：{}\n无座：{}\n\n'.format(
	                args[0], args[1], args[2], args[3], args[4], args[5], args[6],args[7], args[8]))
		self.trains_info.append(info)

	def slow_info(self,*args):
		info = ('车次:{}\n出发站:{}，目的地:{}\n出发时间:{}，到达时间:{}\n耗时:{}\n'
							'座位情况：\n软卧：{}\n硬卧：{}\n硬座：{}\n无座：{}\n\n'.format(
	                args[0], args[1], args[2], args[3], args[4], args[5], args[6],args[7], args[8],args[9]))
		self.trains_info.append(info)

	def get_train_html(self):
		r = requests.get(self.url,headers=self.headers,verify=False)
		try:
			return r.json()['data']['result']
		except:
			time.sleep(2)
			print('again please')
			return self.get_train_html()
		# return r.json()
		

class SearchDetailTickets(Tickets):
	def __init__(self,text):
		super().__init__(text)
		self.url = self.__get_query_url(text)

	def __get_query_url(self,text):
		'''
		解析传入的text并生成符合12306api的url连接
		:param text: 
		:return: 
		'''
		args = str(text).split(' ')
		self.model = args[0]
		self.from_station = self.station.get_telecode(args[1])
		self.to_station = self.station.get_telecode(args[2])
		self.train_date = args[3][:4]+'-'+args[3][4:6]+'-'+args[3][-2:]
		url = ('https://kyfw.12306.cn/otn/leftTicket/queryX?'
			   'leftTicketDTO.train_date={}&'
			   'leftTicketDTO.from_station={}&'
			   'leftTicketDTO.to_station={}&'
			   'purpose_codes=ADULT').format(self.train_date,self.from_station,self.to_station)
		return url

	def get_train_info(self):
		'''
		获取微信列车查询返回文本
		:return: 
		'''
		raw_trains = self.get_train_html()
		for raw_train in raw_trains:
			data_list = raw_train.split('|')
			train_number = data_list[3]
			from_station_name = self.station.get_name(data_list[6])
			to_station_name = self.station.get_name(data_list[7])
			start_time = data_list[8]
			arrive_time = data_list[9]
			time_duration = data_list[10]
			first_class_seat = data_list[31] or '--'
			second_class_seat = data_list[30] or '--'
			soft_sleep = data_list[23] or '--'
			hard_sleep = data_list[28] or '--'
			hard_seat = data_list[29] or '--'
			no_seat = data_list[33] or '--'
			if self.model in self.fast_model and self.model == train_number[:1]:
				self.fast_info(train_number, from_station_name, to_station_name, start_time, arrive_time, 
								time_duration, first_class_seat,second_class_seat, no_seat)
				
			elif self.model in self.slow_model and self.model == train_number[:1]:
				self.slow_info(train_number, from_station_name, to_station_name, start_time, arrive_time, 
								time_duration, soft_sleep, hard_sleep, hard_seat, no_seat)
		train_info = '显示最新的5条列车信息\n\n'+''.join(self.trains_info[:5])
		return train_info


class SearchTickets(Tickets):
	def __init__(self,text):
		super().__init__(text)
		self.url = self.__get_query_url(text)		

	def __get_query_url(self,text):
		'''
		解析传入的text并生成符合12306api的url连接
		:param text: 
		:return: 
		'''
		args = str(text).split(' ')
		self.from_station = self.station.get_telecode(args[0])
		self.to_station = self.station.get_telecode(args[1])
		self.train_date = args[2][:4]+'-'+args[2][4:6]+'-'+args[2][-2:]
		url = ('https://kyfw.12306.cn/otn/leftTicket/queryX?'
			   'leftTicketDTO.train_date={}&'
			   'leftTicketDTO.from_station={}&'
			   'leftTicketDTO.to_station={}&'
			   'purpose_codes=ADULT').format(self.train_date,self.from_station,self.to_station)
		return url

	def get_train_info(self):
		'''
		获取微信列车查询返回文本
		:return: 
		'''
		raw_trains = self.get_train_html()
		for raw_train in raw_trains:
			data_list = raw_train.split('|')
			train_number = data_list[3]
			from_station_name = self.station.get_name(data_list[6])
			to_station_name = self.station.get_name(data_list[7])
			start_time = data_list[8]
			arrive_time = data_list[9]
			time_duration = data_list[10]
			first_class_seat = data_list[31] or '--'
			second_class_seat = data_list[30] or '--'
			soft_sleep = data_list[23] or '--'
			hard_sleep = data_list[28] or '--'
			hard_seat = data_list[29] or '--'
			no_seat = data_list[33] or '--'
			if train_number[:1] in self.fast_model:
				self.fast_info(train_number, from_station_name, to_station_name, start_time, arrive_time, 
								time_duration, first_class_seat,second_class_seat, no_seat)
				
			elif train_number[:1] in self.slow_model:
				self.slow_info(train_number, from_station_name, to_station_name, start_time, arrive_time, 
								time_duration, soft_sleep, hard_sleep, hard_seat, no_seat)
		train_info = '显示最新的5条列车信息\n\n'+''.join(self.trains_info[:5])
		return train_info




