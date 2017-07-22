import urllib.request

class Html_Downloader(object):
	def download(self, url):
		if url is None:
			return None

		response = urllib.request.urlopen(url)

		if response.getcode() != 200:
			return None

		return response.read()