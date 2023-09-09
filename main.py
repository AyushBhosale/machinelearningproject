import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# removing unwanted symbols
# * symbol remover
dataset=pd.read_csv("Development of average annual wages.csv")
dataset["Country"]=dataset["Country"].str.replace('*','',regex=False)
# , from year columns
yrs=["2000","2010","2020","2022"]
for yr in yrs:
    dataset[yr]=dataset[yr].str.replace(',','',regex=False)

for i in ["2000","2022"]:
    median_value = dataset[i].median()
    dataset[i].fillna(median_value,inplace=True)

# plotting graph
plt.figure(figsize=(15, 10))
for i, country in enumerate(dataset['Country']):
    plt.plot(['2000', '2010', '2020', '2022'], dataset.loc[i, ['2000', '2010', '2020', '2022']], label=country)

plt.title('Development of Average Annual Wages (2000-2022)')
plt.xlabel('Year')
plt.ylabel('Average Annual Wages (USD)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')
plt.grid(True)
plt.show()
