import pandas as pd
import matplotlib.pyplot as plt
Data = [1,2,3,4,5,6,2]
myseries_1=pd.Series(Data)
Index = ['A','B','C','D','E','F','G']

myseries_2 = pd.Series(Data,Index)
print(myseries_2)

mydictionary = {'A':1,'B':2,'C':3,'D':4,'E':5}
myseries=pd.Series(mydictionary)
print(myseries)

mydataframe = pd.DataFrame(Data)
print(mydataframe)

mydictionary_2=pd.DataFrame({'name':['Karan','Arjun','Ram','Lakhan'],
                'company':['infy','tech-m','google','ms'],
                'Salary':[100000,70000,50000,40000]},index = [2008,2009,2010,2011])

mydictionary_3=pd.DataFrame({'name':['Karan','Arjun','Ram','Lakhan'],
                'company':['infy','tech-m','google','ms'],
                'Salary':[100000,70000,50000,40000]},index=[2006,2007,2008,2009])
print(mydictionary_2,mydictionary_3)
merge=pd.merge(mydictionary_2,mydictionary_3,on="name")
print(merge)
mydictionary_2.to_csv('data.html')
#join=mydictionary_2.join(mydictionary_3)

#print(join)

#print(x.head(3))
#print(x.tail(3))
mydictionary_2.set_index('name',inplace=True)
df_1=mydictionary_2.rename(columns={'name':'names'})
df_1.plot(marker="x")
#mydictionary_2.plot(marker="x")
plt.show()
