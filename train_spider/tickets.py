import requests
import time
from stations import Station


# text = 'D 绍兴 上海 20170910'
all_model = ['G','D','C','Z','T','K']
fast_model = ['G','D','C']
slow_model = ['Z','T','K']
COMMEN_ERROR = '查询出现错误，请检查格式重新输入'
MODEL_ERROR = '输入车型有误，请检查格式重新输入'
FORMAT_ERROR = '查询格式有误，请检查格式重新输入'
TIME_ERROR = '查询时间有误，请检查格式重新输入'
URL_ERROR = '数据接口异常，请联系作者更新'
HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
		'Cookie':'RAIL_DEVICEID=FQJZUWd1RdRp_pptqEVpCW2wILTp2QvuGVEBBjEQUrI91OXYaYajp3j3lPkogs_5bfbAapw2WXcLtsyTeplE1po3OHLWtkCvJPvRPzYKk4DTUJ_NKPE-c49WKc6vl5jEnE6d81Inm8np5A36EeeInArAOvunIEd8'
		# 'Cookie':('JSESSIONID=88B44190EFEF0469C7E19B33B15B8BEE; '
		# 		'route=6f50b51faa11b987e576cdb301e545c4; '
				# 'BIGipServerotn=804258314.64545.0000; '
				# 'fp_ver=4.5.1; '
				# 'RAIL_EXPIRATION=1505221983857; '
				# 'RAIL_DEVICEID=LkRpgNI0_P0XagbwcBqyjGuuGRDWiO0AVKpBjCPshxVb67Z1IQTP4DfBjWeD6bdzjNntQp3Q653oX3yy4mjTS3crmkiWz7E00TAxsfUEk8cF1i74G0xUJ66shorxgHOtOyD_TGIYjsH9NhMSdb1lhiKwDqCAjE4s; '
				# '_jc_save_fromStation=%u7ECD%u5174%u5317%2CSLH; '
				# '_jc_save_toStation=%u4E0A%u6D77%u5357%2CSNH; '
				# '_jc_save_fromDate=2017-09-10; '
				# '_jc_save_toDate=2020-09-30; '
				# '_jc_save_wfdc_flag=dc')
		# 'Cookie':'JSESSIONID=7C32B765C92A6849A20B1B6A5B747C3D; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=972030474.38945.0000; fp_ver=4.5.1; RAIL_EXPIRATION=1505351730882; RAIL_DEVICEID=FQJZUWd1RdRp_pptqEVpCW2wILTp2QvuGVEBBjEQUrI91OXYaYajp3j3lPkogs_5bfbAapw2WXcLtsyTeplE1po3OHLWtkCvJPvRPzYKk4DTUJ_NKPE-c49WKc6vl5jEnE6d81Inm8np5A36EeeInArAOvunIEd8; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2017-09-10; _jc_save_toDate=2017-09-10; _jc_save_wfdc_flag=dc'
	}

class SearchTickets(object):
	"""docstring for Tickets"""
	def __init__(self,text):
		self.headers = HEADERS
		self.error = COMMEN_ERROR
		self.model = ''
		self.people_date = ''
		self.fast_model = fast_model
		self.slow_model = slow_model
		self.all_model = all_model
		self.station = Station()
		self.url = self.__get_query_url(text)		
		self.trains_info = []
		

	def __parse_text(self,text):
		args = str(text).split(' ')
		if len(args) == 3:
			try:
				self.from_station = self.station.get_telecode(args[0])
				self.to_station = self.station.get_telecode(args[1])
				self.train_date = args[2][:4]+'-'+args[2][4:6]+'-'+args[2][-2:]
			except:
				self.error = FORMAT_ERROR
		elif len(args) == 4:
			try:
				if args[0] in self.all_model:
					self.model = args[0]
					self.from_station = self.station.get_telecode(args[1])
					self.to_station = self.station.get_telecode(args[2])
					self.train_date = args[3][:4]+'-'+args[3][4:6]+'-'+args[3][-2:]			
				elif int(args[3]) >= 0 and int(args[3]) <= 23:
					self.from_station = self.station.get_telecode(args[0])
					self.to_station = self.station.get_telecode(args[1])
					self.train_date = args[2][:4]+'-'+args[2][4:6]+'-'+args[2][-2:]
					self.people_date = args[3]
			except:
			    self.error = FORMAT_ERROR
		
		elif len(args) == 5:
			try:
				if args[0] in self.all_model:
					if int(args[4]) >= 0 and int(args[4]) <= 23:
						self.model = args[0]
						self.from_station = self.station.get_telecode(args[1])
						self.to_station = self.station.get_telecode(args[2])
						self.train_date = args[3][:4]+'-'+args[3][4:6]+'-'+args[3][-2:]
						self.people_date = args[4]
					else:
						self.error = TIME_ERROR
				else:
					self.error = MODEL_ERROR
			except:
			    self.error = FORMAT_ERROR

		else:
			self.error = FORMAT_ERROR

	def __fast_info(self,*args):
		info = ('车次:{}\n出发站:{}，目的地:{}\n出发时间:{}，到达时间:{}\n耗时:{}\n'
			'座位情况：\n一等座：{}\n二等座：{}\n无座：{}\n\n'.format(*args))
		self.trains_info.append(info)

	def __slow_info(self,*args):
		info = ('车次:{}\n出发站:{}，目的地:{}\n出发时间:{}，到达时间:{}\n耗时:{}\n'
			'座位情况：\n软卧：{}\n硬卧：{}\n硬座：{}\n无座：{}\n\n'.format(*args))
		self.trains_info.append(info)

	def __sort_info(self,train_number,from_station_name,to_station_name,start_time,arrive_time, time_duration,first_class_seat,second_class_seat,soft_sleep,hard_sleep,hard_seat,no_seat):
		if train_number[:1] in self.fast_model:
			self.__fast_info(train_number, from_station_name, to_station_name, start_time, arrive_time, 
						time_duration, first_class_seat,second_class_seat, no_seat)	
		elif train_number[:1] in self.slow_model:
			self.__slow_info(train_number, from_station_name, to_station_name, start_time, arrive_time, 
						time_duration, soft_sleep, hard_sleep, hard_seat, no_seat)

	def __get_query_url(self,text):
		'''
		解析传入的text并生成符合12306api的url连接
		:param text: 
		:return: 
		'''
		try:
			self.__parse_text(text)
			url = ('https://kyfw.12306.cn/otn/leftTicket/queryX?'
			   'leftTicketDTO.train_date={}&'
			   'leftTicketDTO.from_station={}&'
			   'leftTicketDTO.to_station={}&'
			   'purpose_codes=ADULT').format(self.train_date,self.from_station,self.to_station)
			print('url ok')
			return url
		except:
			self.error == URL_ERROR
		
	def __get_train_html(self):
		r = requests.get(self.url,headers=self.headers,verify=False)
		try:
			return r.json()['data']['result']
		except:
			time.sleep(2)
			print('again please')
			return self.get_train_html()
		# return r.json()

	def get_train_info(self):
		'''
		获取微信列车查询返回文本
		:return: 
		'''
		if self.url:
			raw_trains = self.__get_train_html()
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
				if self.people_date == '':	
					if self.model == '':
						self.__sort_info(train_number,from_station_name,to_station_name,start_time,arrive_time, time_duration,
									first_class_seat,second_class_seat,soft_sleep,hard_sleep,hard_seat,no_seat)
					elif self.model in self.all_model:
						if self.model == train_number[:1]:
							self.__sort_info(train_number,from_station_name,to_station_name,start_time,arrive_time, time_duration,
									first_class_seat,second_class_seat,soft_sleep,hard_sleep,hard_seat,no_seat)
				else:
					if self.model == '':
						if int(start_time[:2]) >= int(self.people_date):
							self.__sort_info(train_number,from_station_name,to_station_name,start_time,arrive_time, time_duration,
									first_class_seat,second_class_seat,soft_sleep,hard_sleep,hard_seat,no_seat)
					elif self.model in self.all_model:
						if self.model == train_number[:1]:
							if int(start_time[:2]) >= int(self.people_date):
								self.__sort_info(train_number,from_station_name,to_station_name,start_time,arrive_time, time_duration,
									first_class_seat,second_class_seat,soft_sleep,hard_sleep,hard_seat,no_seat)
				
		if len(self.trains_info) == 0:
			return self.error
		else:
			train_info = '显示最新的5条列车信息\n\n'+''.join(self.trains_info[:5])
			return train_info




