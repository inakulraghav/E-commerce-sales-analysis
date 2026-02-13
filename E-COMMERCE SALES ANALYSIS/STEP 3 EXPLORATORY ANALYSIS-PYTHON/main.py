import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

def modification(ax,title="title",xlabel="x",ylabel="y",grid=False):
    if grid:
        ax.grid(True)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


 


file_path =r"C:\Users\Lenovo\OneDrive\Desktop\Projects\RESUME READY\STEP 2 DATA CLEANING (PYTHON)\Cleaned_data.csv"

df=pd.read_csv(file_path)
df=df.drop_duplicates()

# data type fix 
# Numerical columns 
float_cols = ["discount", "cost_price", "selling_price","payment_amount_of_order", "refund_amount"]
int_cols = ["order_id", "customer_id", "age", "quantity"]

df[float_cols] = df[float_cols].apply(pd.to_numeric, downcast="float")
df[int_cols] = df[int_cols].apply(pd.to_numeric, downcast="integer")

# Categorical columns 
cat_cols = ["order_status", "gender", "city", "country","product_name","category", "sub_category", "delivery_status","payment_method","payment_status", "item_returned", "return_reason"]

df[cat_cols] = df[cat_cols].astype("category")

# Datetime columns
date_cols = ["order_date", "signup_date", "shipped_date","delivered_date", "payment_date", "return_date"]

df[date_cols] = df[date_cols].apply(pd.to_datetime)



# dropping column
df.drop(columns=["order_month","order_year"],inplace=True)



# column creation
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
df["age_group"]=pd.cut(df["age"],bins=bins,labels=labels,right=False)

df=df.rename(columns={"selling_price":"MRP"})
df["selling_price"] = df["MRP"]*(1-df["discount"]/100)    

df["margin"]=(df["selling_price"]-df["cost_price"])
df["profit"]=(df["selling_price"]-df["cost_price"])*df["quantity"]

df["marginrate"]=(df["margin"]/df["selling_price"])*100

df["total_amount"]=df["selling_price"]*df["quantity"]


# 1 - Time-Based Trends

monthlysales=df.groupby(df["order_date"].dt.strftime("%b-%y"))["total_amount"].sum().reset_index().set_index("order_date")
monthlysales.index = pd.to_datetime(monthlysales.index, format="%b-%y")
monthlysales=monthlysales.sort_index()
# print(monthlysales)

monthlyorders=df.groupby(df["order_date"].dt.strftime("%b-%Y"))["order_id"].sum()
monthlyorders.index =pd.to_datetime(monthlyorders.index,format="%b-%Y")
monthlyorders=monthlyorders.sort_index()
# print(monthlyorders)




# 2 - Product & Category Performance

categorywisesales=df.groupby("category")["total_amount"].sum().sort_values(ascending=False).head(3)
# print(categorywisesales)

highmarginproducts=df.groupby("product_name")["margin"].mean().sort_values(ascending=False).head()
# print(highmarginproducts)
lowmarginproducts=df.groupby("product_name")["margin"].mean().sort_values(ascending=False).tail()
# print(lowmarginproducts)



#3 - Customer Behavior

top5customers=df.groupby("customer_id")["total_amount"].sum().sort_values(ascending=False).head()
# print(top5customers)

highestsalesbyagegroup=df.groupby("age_group")["total_amount"].sum().sort_values(ascending=False).head()
# print(highestsalesbyagegroup)



# 4 - Profitability Lens
categorywisemargin=df.groupby("category")["marginrate"].mean()
# print(categorywisemargin)
# print(df[["margin","selling_price","cost_price"]])



# 5 - Delivery & Operations
df["delivery_time"]=(df["delivered_date"]-df["order_date"]).dt.days
df["delivery_time"]=df["delivery_time"].fillna(df["delivery_time"].mean())






plt.rcParams.update({
    'figure.figsize': (12, 6),
    'axes.titlesize': 16,     
    'axes.labelsize': 12,        
})



p1=plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=2)
p2=plt.subplot2grid((3,3),(2,0),rowspan=1,colspan=2)
p3=plt.subplot2grid((3,3),(0,2),rowspan=1,colspan=3)
p4=plt.subplot2grid((3,3),(1,0),rowspan=1,colspan=2)
p5=plt.subplot2grid((3,3),(2,2),rowspan=1,colspan=1)
p6=plt.subplot2grid((3,3),(1,2),rowspan=1,colspan=1)

p1.plot(monthlysales.astype(str).index,monthlysales.values,marker = "o",color="black")
p2.plot(monthlyorders.astype(str).index,monthlyorders.values,marker = "o",color="black")
p3.barh(categorywisesales.index,categorywisesales.values,color =[
    '#8B7355',  # Burnt sienna
    '#A0522D',  # Sienna
    '#D2691E',  # Chocolate
    '#CD853F',  # Peru
    '#DAA520',  # Golden rod
    '#B8860B',  # Dark golden rod
    '#BC8F8F',  # Rosy brown
],edgecolor="black")

p4.bar(highmarginproducts.index,highmarginproducts.values,color =[
    '#8B7355',  # Burnt sienna
    '#A0522D',  # Sienna
    '#D2691E',  # Chocolate
    '#CD853F',  # Peru
    '#DAA520',  # Golden rod
    '#B8860B',  # Dark golden rod
    '#BC8F8F',  # Rosy brown
],edgecolor="black")

p5.barh(lowmarginproducts.index,lowmarginproducts.values,color =[
    '#8B7355',  # Burnt sienna
    '#A0522D',  # Sienna
    '#D2691E',  # Chocolate
    '#CD853F',  # Peru
    '#DAA520',  # Golden rod
    '#B8860B',  # Dark golden rod
    '#BC8F8F',  # Rosy brown
],edgecolor="black")

p6.bar(top5customers.index.astype(str),top5customers.values,color =[
    '#8B7355',  # Burnt sienna
    '#A0522D',  # Sienna
    '#D2691E',  # Chocolate
    '#CD853F',  # Peru
    '#DAA520',  # Golden rod
    '#B8860B',  # Dark golden rod
    '#BC8F8F',  # Rosy brown
],edgecolor="black")



for ax in [p1,p2,p4]:
    ax.tick_params(axis="x",rotation=5)
p5.tick_params(axis="x",rotation=90)

# modifications
modification(p1, title="Monthly sales", xlabel="Months", ylabel="Sales", grid=True)
modification(p2, title="Monthly Orders", xlabel="Months", ylabel="Orders", grid=True)
modification(p3, title="Sales By Category", xlabel="Sales", ylabel="Category")
modification(p4, title="High Margin Products", xlabel="Products", ylabel="Margin")
modification(p5, title="Low Margin Products", xlabel="Margin", ylabel="Products")
modification(p6, title="Top Customers", xlabel="Customers", ylabel="Sales")


plt.suptitle("E-Com Dash",font="Arial" ,fontsize=18)
plt.tight_layout()
plt.show()












p7=plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=3)
p8=plt.subplot2grid((3,3),(1,0),rowspan=1,colspan=1)
p9=plt.subplot2grid((3,3),(1,1),rowspan=1,colspan=1)
p10=plt.subplot2grid((3,3),(1,2),rowspan=1,colspan=1)
p11=plt.subplot2grid((3,3),(2,0),rowspan=1,colspan=3)

p7.bar(highestsalesbyagegroup.index,highestsalesbyagegroup.values,color=["blue","teal","grey","black","beige"])
# print(df[["MRP","discount","selling_price","quantity","total_amount","cost_price","margin","marginrate"]])

p8.scatter(df["discount"],df["marginrate"],c=df["marginrate"],cmap="RdYlGn")
# print(df[["category","MRP","discount","selling_price","quantity","total_amount","cost_price","margin","marginrate"]])

p9.barh(categorywisemargin.index,categorywisemargin.values,color=["blue","teal","grey","black","beige"])

p10.hist(df["delivery_time"],bins=3,color=["pink"])

returndf=df[df["item_returned"]=="YES"]
nonreturndf=df[df["item_returned"]=="NO"]
p11.boxplot([returndf["delivery_time"],nonreturndf["delivery_time"]],labels=["Returned","Not Returned"],
    patch_artist=True,
    showmeans=True,
    meanline=True,
    showfliers=True,
    flierprops=dict(marker='o', markersize=5, alpha=0.5)
)

modification(p7, title="Sales By Age", xlabel="Age Group", ylabel="Sales")
modification(p8, title="Discount VS Margin Rate", xlabel="Discount Rate", ylabel="Margin Rate")
modification(p9, title="Margin By Category", xlabel="Margin", ylabel="Category")
modification(p10, title="Delivery Time", xlabel="Days")
modification(p11, title="Delivery Time Vs Return", xlabel="Products", ylabel="Days")





plt.suptitle("E-Com Dash-2",font="Arial" ,fontsize=18)
plt.tight_layout()
plt.show()




# some other charts


p12=plt.subplot2grid((3,3),(0,0),rowspan=1,colspan=3)
p13=plt.subplot2grid((3,3),(1,0),rowspan=1,colspan=1)
p14=plt.subplot2grid((3,3),(1,1),rowspan=1,colspan=1)
p15=plt.subplot2grid((3,3),(1,2),rowspan=1,colspan=1)
p16=plt.subplot2grid((3,3),(2,0),rowspan=1,colspan=3)

top5city=df.groupby("city")["total_amount"].sum()
p12.bar(top5city.index,top5city.values,color=["beige","teal","pink","purple","blue"])

paymentsmethodcount=df["payment_method"].value_counts()
p13.pie(paymentsmethodcount.values,labels=paymentsmethodcount.index,colors=["red","yellow","green","purple","teal"],autopct="%0.1f%%",startangle=45)
p13.set_title("Payemnt Method Used")

categorywisereturnrate=df.groupby("category")["item_returned"].apply(lambda x : ((x=="YES").sum()/x.count())*100)
p14.bar(categorywisereturnrate.index,categorywisereturnrate.values,color=["red","yellow","green","purple","teal"])

p15.scatter(df["discount"],df["profit"],c=df["profit"],cmap="RdYlGn")

dayswisesale=df.groupby(df["order_date"].dt.strftime("%a"))["order_id"].sum()
p16.plot(dayswisesale,color="black",marker="o")

modification(p12, title="Top Cities By Sales", xlabel="City", ylabel="Sales")
modification(p14, title="Categories Wise Return Rate", xlabel="Category", ylabel="Return Rate")
modification(p15, title="Discount VS Profit", xlabel="Discount", ylabel="Profit")
modification(p16, title="Peak Days", xlabel="Days",ylabel="Sales")


plt.suptitle("E-Com Dash-3",font="Arial" ,fontsize=18)
plt.tight_layout()
plt.show()

# print(df.shape)
# df.info()


df.to_csv("Cleaned.csv",index=False)



