import csv
#categories: rain, light rain, cloudy, partly cloudy, fine

RAINFALL = 3
CLOUD_9 = 11
CLOUD_3 = 17

def findAverage(num1, num2):
    sumOfNum = 0
    count = 0
    if num1:
        count += 1
        sumOfNum += float(num1)
    if num2:
        count += 1
        sumOfNum += float(num2)
    if count:
        return sumOfNum/count
    else:
        return 0
        

def findCategory(row):
    cloud = findAverage(row[CLOUD_9], row[CLOUD_3])
    rain = float(row[RAINFALL])
    
    #if rain >= 16: #light rain for >= 8 hours, moderate rain for ~5 hours or heavy rain for an hour or 2
    #    return 'rain'
    if rain >= 6: #light rain for >=3 hours or moderate rain for 1-2 hours
        return 'rain'
    elif cloud >= 5.2: #cloudy defined as >=65% cloud cover, 5.2/8 = 65/100
        return 'cloudy'
    elif cloud >= 2.4: #parly cloudy defined as >= 30% cloud cover, 2.4/8 = 30/100
        return 'partly cloudy'
    else:
        return 'fine'
    


fields = ['date', 'category']
with open('weather.csv') as readFile:
    with open('categories.csv','w') as writeFile:
        weatherReader = csv.reader(readFile)
        weatherWriter = csv.DictWriter(writeFile, fieldnames=fields)
        weatherWriter.writeheader()
        for i,row in enumerate(weatherReader):
            if row:
                category = findCategory(row)
                weatherWriter.writerow({'date': row[0], 'category': category})
