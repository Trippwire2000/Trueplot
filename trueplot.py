from matplotlib import pyplot as plt
from pandas import read_csv
import pandas as pd
import tkinter as tk

root = tk.Tk()
root.title = 'Plot Boy'

def go():

	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()

	axislist = [ax1, ax2]
	getter = [y1.get(), y2.get()]

	for i, y in zip(axislist, getter):

		print(str(i), str(y))
		if y == 'Gold AUD':
			i.plot(gold['DATE'], gold['Gold AUD'], label = 'Gold AUD', color = 'm')
			continue

		elif y == 'Gold USD':
			i.plot(gold['DATE'], gold['Gold USD'], label = 'Gold USD', color = 'm')
			continue

		elif y == 'Silver AUD':
			i.plot(silver['DATE'], silver['Silver AUD'], label = 'Silver AUD', color = 'g')
			continue

		elif y == 'Silver USD':
			i.plot(silver['DATE'], silver['Silver USD'], label = 'Silver USD', color = 'g')
			continue

		elif y == 'Platinum AUD':
			i.plot(platinum['DATE'], platinum['Platinum AUD'], label = 'Platinum AUD', color = 'y')
			continue

		elif y == 'Platinum USD':
			i.plot(platinum['DATE'], platinum['Platinum USD'], label = 'Platinum USD', color = 'y')
			continue

		elif y == 'Oil, Brent USD':
			i.plot(oil['DATE'], oil['Oil Brent USD'], label = 'Brent Crude Oil', color = 'k')
			continue

		elif y == 'Oil, WTI USD':
			i.plot(oil['DATE'], oil['Oil WTI USD'], label = 'WTI', color = 'r')
			continue

		elif y == 'Unemployment % USA':
			i.plot(unemployed['DATE'], unemployed['Unemployment % USA'], label = 'USA unemployment %', color = 'b')
			continue

		elif y == 'SP500 USD':
			i.plot(sp500['DATE'], sp500['SP500 USD'], label = 'SP500', color = 'b')



	#plt.legend()
	ax1.legend(loc = 0)
	ax2.legend(loc = 1)
	fig.tight_layout()
	plt.show()


dslist = ['Gold AUD', 'Gold USD', 'Silver AUD', 'Silver USD', 'Platinum AUD', 'Platinum USD', 'SP500 USD', 'Oil, Brent USD', 'Oil, WTI USD', 'Unemployment % USA' ]


y1 = tk.StringVar(root)
y1.set(dslist[0])
y1drop = tk.OptionMenu(root, y1, *dslist)
y1drop.pack(expand = True, fill = 'both')

y2 = tk.StringVar(root)
y2.set(dslist[2])
y2drop = tk.OptionMenu(root, y2, *dslist)
y2drop.pack(expand = True, fill = 'both')


go_button = tk.Button(root, text = 'Plot chart', command = go)
go_button.pack(expand = True, fill = 'both')

gold = read_csv('gold.csv', usecols = ['DATE', 'Gold AUD', 'Gold USD'])
silver = read_csv('silver.csv', usecols = ['DATE', 'Silver USD', 'Silver AUD'])
platinum = read_csv('platinum.csv', usecols = ['DATE', 'Platinum AUD', 'Platinum USD'])
sp500 = read_csv('sp-500.csv', usecols = ['DATE', 'SP500 USD'])
oil = read_csv('oil.csv', usecols = ['DATE', 'Oil Brent USD', 'Oil WTI USD'])
unemployed = read_csv('usa_unemployment.csv', usecols = ['DATE', 'Unemployment % USA'])


gold_raw = gold.fillna(method = 'ffill')
sp500 = sp500.fillna(method = 'ffill')
oil = oil.fillna(method = 'ffill')
silver = silver.fillna(method = 'ffill')
platinum = platinum.fillna(method = 'ffill')
#silver_raw = silver_raw.fillna(axis = 0, how = 'any')
#platinum_raw = platinum_raw.fillna(axis = 0, how = 'any')



unemployed['DATE'] = pd.to_datetime(unemployed.DATE, format = '%Y')
gold['DATE'] = pd.to_datetime(gold.DATE, format = '%d/%m/%y')
sp500['DATE'] = pd.to_datetime(sp500.DATE, format = '%Y-%m-%d')
oil['DATE'] = pd.to_datetime(oil.DATE, format = '%Y-%m-%d')
silver['DATE'] = pd.to_datetime(silver.DATE, format = '%d/%m/%y')
platinum['DATE'] = pd.to_datetime(platinum.DATE, format = '%d/%m/%y')



root.mainloop()







# ax2.plot(oil['DATE'], oil['Oil Brent USD'], label = 'Brent Crude Oil', color = 'k')
# ax1.plot(oil['DATE'], oil['Oil WTI USD'], label = 'WTI', color = 'r')
# ax1.plot(unemployed['DATE'], unemployed['Unemployment % USA'], label = 'USA unemployment %')
# ax2.plot(silver['DATE'], silver['Silver USD'], label = 'Silver USD', color = 'g')
# ax1.plot(platinum['DATE'], platinum['Platinum USD'], label = 'Platinum USD', color = 'y')
# plt.plot(gold['DATE'], gold['Gold AUD'], label = 'Gold AUD')
# ax1.plot(gold['DATE'], gold['Gold USD'], label = 'Gold USD')
# ax2.plot(sp500['DATE'], sp500['SP500 USD'], label = 'SP500')