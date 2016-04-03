import requests, re, csv
with open("weather.csv",'w') as file:
    months = []
    for i in range(3,10):
        month = requests.get("http://www.bom.gov.au/climate/dwo/20150{}/text/IDCJDW2124.20150{}.csv".format(i,i))
        months.append(month.text)
    for i in range(3):
        month = requests.get("http://www.bom.gov.au/climate/dwo/20151{}/text/IDCJDW2124.20151{}.csv".format(i,i))
        months.append(month.text)
    for i in range(1,3):
        month = requests.get("http://www.bom.gov.au/climate/dwo/20160{}/text/IDCJDW2124.20160{}.csv".format(i,i))
        months.append(month.text)

        
    for i in range(len(months)):
        days = months[i].split("\r\n")
        days = days[10:] #Ingore the starting comments about who collected the data
        for j in range(len(days)):
            days[j] = days[j][1:] #Since the starting comments come on a column before the data, the first column has to be ignored
            print(days[j][1:])
        months[i] = "\r\n".join(days)
    file.write("\r\n".join(months))
