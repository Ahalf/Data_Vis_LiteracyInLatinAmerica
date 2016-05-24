import matplotlib.pyplot as plt 
import numpy as np 
import csv

totalData = open("/Users/adamhalfaker/Documents/Literacyrates.csv", 'r')
reader = csv.reader(totalData)

#saves reader object data into myData list
myData =[]
for r in reader:
	myData.append(r)
totalData.close()

literacyData = []
numberOfCountries = []
countryNames = []
for array in myData:
	#removes header
	if array == ['Rank', 'Country Name', 'Literacy Rate (%)']:
		myData.remove(array)
	else:
		for i in range(len(array)):
			#saves list from 1 to n of total #of countries
			if i == 0:
				numberOfCountries += [float(array[i])]	
			elif i == 1:
				#saves country name for x -axis labeling
				countryNames += [array[i]]
			elif i == 2:
				#saves this for y axis labeling
				literacyData += [float(array[i])]
#Creates list of circle dimensions which will go into s in plt.scatter
area = []
for element in literacyData:
	areaElement = float(0.00)
	areaElement = (np.pi * element/10) ** 2 
	area.append(areaElement)

#Plot setup
x = numberOfCountries 
y = literacyData
circleArea = 75
colors = np.random.rand(len(numberOfCountries))
plt.xticks(x, countryNames, rotation = 'vertical')
plt.scatter(x, y, s = circleArea, c = colors, alpha = 0.5)
plt.title("Literacy rates in Latin American and Caribbean Countries (ages 15-24)")
plt.xlabel("Latin American and Caribbean Countries")
plt.ylabel("Literacy Rate (%)")
plt.show()




