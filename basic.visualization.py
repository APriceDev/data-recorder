import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# check for anomalies (white space) in column names
print(df.columns)
# correct as needed
df = df.rename(columns={' temp': 'temp'})
# check all is good
print(df.columns)

# assign values
x = df.time
y = df.temp

# functional plotting method
plt.plot(x,y)

# adding Title, X and Y labels
plt.title('Time/Temp Graph')
plt.xlabel('Time')
plt.ylabel('Temperature')

plt.show()