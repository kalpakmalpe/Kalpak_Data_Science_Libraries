import matplotlib.pyplot as plt

x=['tongue','lung','mouth','tonsil']
y=['14.2','26,3','29.4','10.1']
z=['12.3','21.3','28.1','24.4']
# Plot
colors=(0,0,0,0)
plt.scatter(x, y, c=colors, alpha=0.5,marker='x')
plt.title('Scatter plot pythonspot.com')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,z,)
