import requests
from requests.exceptions import RequestException

def get_one_page(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile('<dd>')

def main():
	url = 'http://maoyan.com/board'
	html = get_one_page(url)
	print(html)

if __name__ == '__main__':
    main()
