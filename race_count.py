import requests, json

def main():
	domain = "https://ergast.com/api/f1/"
	extension = "/results.json"
	total_count = 0
	dict = {}
	for x in range(1950,2019):
		race_count = 0
		year = domain + str(x) + '/'
		for num in range(1,22):
			url = year + str(num) + extension
			request_data = requests.get(url)
			data = request_data.json()
			total_count = int(data["MRData"]["total"])
			if total_count!=0:
				race_count += 1
		dict[str(x)] = race_count
		print(str(x) + ":" + str(race_count) + "\n")