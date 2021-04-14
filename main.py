import requests
import threading
import random
import proxyscrape as ps
import time

#Enter URL here
url = ''
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

httpcol = ps.create_collector('http-collecter', 'http')
httpscol = ps.create_collector('https-collector', 'https')

picturer = 'https://render-tron.appspot.com/screenshot/'
path = 'ss.jpg'

browsers = [
	{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
	{'User-Agent': 'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2'},
	{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'},
	{'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36'},
	{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'},
	{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'},
	{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'}
]

def view(url):
	response = requests.get(picturer + url, stream=True)
	with open(path, 'wb') as file:
		for chunk in response:
			file.write(chunk)

def send(url):
	http = httpcol.get_proxy({'type': 'http'})
	https = httpscol.get_proxy({'type': 'https'})

	http = 'http://' + http[0] + ':' + http[1]
	https = 'http://' + https[0] + ':' + https[1]

	print(http, https)

	proxies = {
		'http' : http,
		'https' : https
	}
	
	try:
		response = requests.get(url, allow_redirects=True, headers=random.choice(browsers), proxies=proxies)
		if response.status_code == 200:
			print('success')
		else:
			print(response.status_code)
	except:
		print('failed')

def spam(url):
	while True:
		thread = threading.Thread(target=(send), args=(url,))
		thread.start()
		time.sleep(0.1)


