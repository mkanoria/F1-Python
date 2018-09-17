import requests, json

count_total = 0
count_yup = 0

def generate_url_for_winner():
	num = {2003:16,2004:18,2005:19,2006:18,2007:17,2008:18,2009:17,2010:19,2011:19,2012:20,2013:19,2014:19,2015:19,2016:21,2017:20}
	domain = "https://ergast.com/api/f1/" 
	extension_winner = "/results.json"
	extension_qualifying = "/qualifying.json"	
	for x in range(2003,2018):
		year = domain + str(x) + '/'
		for y in range(1, num[x]+1):
			url_winner = year + str(y) + extension_winner
			url_qualifying = year + str(y) + extension_qualifying
			generate(url_winner, url_qualifying)

def generate(url_winner, url_qualifying):
	request_winner = requests.get(url_winner)
	data_winner = request_winner.json()
	driverId_winner = data_winner["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]['driverId']
	request_qualifying = requests.get(url_qualifying)
	data_qualifying = request_qualifying.json()
	driverId_qualifying = data_qualifying["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"][0]["Driver"]['driverId']
	check_if_same(driverId_winner, driverId_qualifying)
	

def check_if_same(driverRace, driverPole):
	global count_total
	global count_true
	if driverRace == driverPole:
		count_true += 1
		count_total += 1
		print(count_true, count_total)
	else:
		count_total += 1
		print(count_total)

def count_percentage():
	global count_total
	global count_true
	percentage = (count_true/count_total)*100
	print("Percentage: " + str(percentage))

def main():
	generate_url_for_winner()
	count_percentage()

if __name__ == '__main__':
  main()
	