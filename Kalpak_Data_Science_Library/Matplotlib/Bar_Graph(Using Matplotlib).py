import matplotlib.pyplot as plt
#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
years = ['2004', '2005', '2006', '2007']
patients =  [27.3, 28.2, 30.3, 30.4]

plt.xlabel("Years")
plt.ylabel("Patients")
plt.title("Cancer patients")

plt.bar(years,patients)
plt.show()
