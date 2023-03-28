from requests import get
from requests.exceptions import RequestException

def get_libs():
	try:
		response = get('https://api.github.com/orgs/clib-storage/repos')
		if response.status_code == 200:
			data = response.json()
			libs = []
			for lib in data:
				if lib['name'] not in ('.github', 'clib-storage.github.io'):
					libs.append(lib)
			return libs
		else:
			return None
	except RequestException:
		return None
	
def get_release(lib):
	try:
		response = get("https://api.github.com/repos/clib-storage/%s/releases"%(lib))
		if response.status_code == 200:
			data = response.json()
			if len(data) > 0:
				return data[0]
			return None
		else:
			return None
	except RequestException:
		return None
	

def download(url, filename):
	try:
		response = get(url)
		if response.status_code == 200:
			with open(filename, 'wb') as f:
				f.write(response.content)
			return True
		else:
			return False
	except RequestException:
		return False