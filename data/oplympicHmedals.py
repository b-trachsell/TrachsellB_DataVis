import csv
# Lets us read csv files
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []
# To strip the first row of info that is categroies and not data


with open ('data/mens_hockey.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0 

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				# Row 7 because that is the row in which medals are in our
				# Spreadsheet
				print ("Won a gold")
				golds.append(row[7])
				#We check if the row says gold and if it does add one to the gold array

			elif row[7] == "Silver":
				print ("Won a silver")
				silvers.append(row[7])

			else:
				print ("Won a bronze")
				bronzes.append(row[7])

			print (line_count)
			line_count += 1

# Now we can see the medal counts for some ungodly reason

print ("\nTotal Medals: ", line_count)
print("\nTotal Golds: ", len(golds))
print("\nTotal Silvers: ", len(silvers))
print("\nTotal Bronzes: ", len(bronzes))

labels = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes), ]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = [0.1, 0.1, 0.1]

plt.pie (sizes, explode=explode, colors=colors, autopct='%1.f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title( 'JKHKJASHDJKH' )
plt.xlabel( 'SJFHKJHGJKSFDGLJSN')
plt.show()


# Thank you for explaining this code idk what the fuck any of it means :)
# Like I legit Dont KNow What were doing for this fucking assignment
# Im batshit lost lmao