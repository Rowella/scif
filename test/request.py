import requests, re, csv
with open("weather.csv",'w') as file:
    months = []
    for i in range(3,4):
        month = requests.get("http://www.bom.gov.au/climate/dwo/20160{}/text/IDCJDW2124.20160{}.csv".format(i,i))
        months.append(month.text)

        
    for i in range(len(months)):
        days = months[i].split("\r\n")
        days = days[10:]
        for j in range(len(days)):
            days[j] = days[j][1:]
            print(days[j][1:])
        months[i] = "\r\n".join(days)
    file.write("\r\n".join(months))
