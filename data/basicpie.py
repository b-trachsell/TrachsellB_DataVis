import matplotlib.pyplot as plt

hours = [4, 8, 2]
activities = ['sleep','work', 'play']
colors = ['red','blue', 'yellow']

plt.pie(hours, labels=activities, colors=colors, startangle=45, autopct= '%.1f%%')

plt.show()