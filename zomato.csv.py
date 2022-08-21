#applying EDA on Zomato dataset to get some insights of data

import pandas as pd
import numpy as np
import matplotlib .pyplot as plt
import seaborn as sns
#importing the zomato dataset
df=pd.read_csv (r"C:\Users\Asus\OneDrive - IIT Kanpur\Desktop\zomato.csv",encoding="latin-1")
#printing the dataset
print(df)
#printting the shape of the dataset
print(df.shape)
#printing all the columns in the dataset
print(df.columns)
#printing the information of the dataset
print(df.info())
#print the description of the dataset
#all the neumerical columns will show the mean,max,percentile value
print(df.describe())
#printing the null columns with null values from the columns
print(df.isnull().sum())
# as there are null values in "Cuisines" column
# we have another datasheet in which country with code
df_country=pd.read_csv(r"C:\Users\Asus\OneDrive - IIT Kanpur\Desktop\Country-Code.csv")
print(df_country)
#to print top 5 country from file
print(df_country .head())
#combining the two file
final_df=pd.merge(df,df_country,on="Country Code",how= "left")
print(final_df.head())
#now we will count how many country have how many orders
country_order=final_df["Country"].value_counts()
#printing the top 5 country with order
print(country_order.head())
#from above we can see that India has highest number of order for Zomato
#plotting the pie chart of top 3 country with order value
plt.suptitle ("Zomato dataset visualization")
plt.subplot(1,2,1)
plt.title ("pie chart showing top 3 country")
scat=np.array([0.2,0,0])
plt.pie(country_order[:3],labels=country_order.index[:3],autopct= "%1.2f%%",explode= scat,shadow=True)
#scat=np.array([0.2,0,0])
plt.legend (country_order.index[:3])
#plotting bar graph for number of orders
plt.subplot(1,2,2)
plt.title ("bargraph showing top 5 country order ")
color=np.array(["red","orange","yellow","green","pink"])
plt .bar(country_order .index[:5],country_order[:5],color=color )
plt.legend (country_order.index[:5])
plt.show()
#creatings another dataframe so that we can compare that for other countries
ratings=final_df.groupby (["Aggregate rating","Rating color","Rating text"]).size().reset_index().rename(columns={0:"values"})
print(ratings)
sns.barplot(x="Aggregate rating",y="values",data=ratings)
plt.show()
sns.barplot(x="Aggregate rating",y="values",hue="Rating color",data=ratings,palette=["white","red","orange","yellow","green","green"])
plt.show()
sns.countplot (x="Rating color",data=ratings,palette=["white","red","orange","yellow","green","green"])
plt.show()
#analyzing which country has given how many 0 ratings
zero_rat=final_df[final_df["Rating color"]=="White"].groupby ("Country").size().reset_index()
print(zero_rat )
#which country use which currency for payment
curr_count=final_df[["Country","Currency"]].groupby (["Country","Currency"]).size().reset_index()
print(curr_count)
#which country has online delivery
online=final_df[["Has Online delivery","Country"]].groupby (["Has Online delivery","Country"]).size().reset_index()
print(online )
#checking which city has various orders
city=final_df.groupby ("City").size ().reset_index()
print(city)
print(final_df ["Cuisines"])
#as cuisines has 9 null values we can  drop these values
final_df.dropna(inplace= True)
final_df.reset_index(inplace= True)
print(final_df.info())