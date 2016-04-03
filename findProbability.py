import csv, collections

categories = ['rain', 'cloudy', 'partly cloudy', 'fine']

weather = {}

def writeToFile(catDict, category, file):
    file.writerow({'weather': 'From', 'probability': category, 'count':''})
    total = catDict['total']
    for key in catDict.keys():
        if key == 'total': #The total will be used at the end
            continue
        occurances = catDict[key]
        file.writerow({'weather':key, 'probability':occurances/total*100, 'count':occurances})
    file.writerow({'weather':'total', 'probability':100, 'count':catDict['total']}) 
    file.writerow({})
                      
    
    
def printStats(catDict, category):
    total = catDict['total']
    print("Stats for {}:".format(category))
    for key in catDict.keys():
        if key == 'total': #Total will be used at the end
            continue
        occurances = catDict[key]
        print("{}: {} total, {}%".format(key, occurances, occurances/total*100))
    print("Total: {}".format(total))
    print()
    
for category in categories:
    weather[category] = {}
    for otherCat in categories:
        weather[category][otherCat] = 0 #Initialising every relation
    weather[category]['total'] = 0

with open('categories.csv') as readFile:
        categoriesReader = csv.reader(readFile)
        categoriesReader = list(categoriesReader)
        total = len(categoriesReader)
        for i,date in enumerate(categoriesReader):
            if i < total-1 and i!=0:
                otherDate = categoriesReader[i+1]
                weather[date[1]][otherDate[1]] += 1
                weather[date[1]]['total'] += 1
    



with open('probabilities.csv','w') as writeFile:
    probabilitiesWriter = csv.DictWriter(writeFile, fieldnames=['weather','probability','count'])
    probabilitiesWriter.writeheader()
    for category in categories:
        printStats(weather[category], category)
        writeToFile(weather[category], category, probabilitiesWriter)
    
