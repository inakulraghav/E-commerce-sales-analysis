import pandas as pd
import matplotlib.pyplot as plt

# print("Hello World")

df=pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\Projects\RESUME READY\STEP 1 DATA EXTRACTION FOR PYTHON\COMBINED DATASET\FULL COMBINED DATASET.csv")
df=df.drop_duplicates()

# data type fix 
df["discount"] = pd.to_numeric(df["discount"],downcast="float")
df["cost_price"] = pd.to_numeric(df["cost_price"],downcast="float")
df["selling_price"] = pd.to_numeric(df["selling_price"],downcast="float")
df["payment_amount_of_order"] = pd.to_numeric(df["payment_amount_of_order"],downcast="float")
df["refund_amount"] = pd.to_numeric(df["refund_amount"],downcast="float")



df["order_id"] = pd.to_numeric(df["order_id"],downcast="integer")
df["customer_id"] = pd.to_numeric(df["customer_id"],downcast="integer")
df["age"] = pd.to_numeric(df["age"],downcast="integer")
df["quantity"] = pd.to_numeric(df["quantity"],downcast="integer")



df["order_status"]=df["order_status"].astype(dtype="category")
df["gender"]=df["gender"].astype(dtype="category")
df["city"]=df["city"].astype(dtype="category")
df["country"]=df["country"].astype(dtype="category")
df["product_name"]=df["product_name"].astype(dtype="category")
df["category"]=df["category"].astype(dtype="category")
df["sub_category"]=df["sub_category"].astype(dtype="category")
df["delivery_status"]=df["delivery_status"].astype(dtype="category")
df["payment_method"]=df["payment_method"].astype(dtype="category")
df["payment_status"]=df["payment_status"].astype(dtype="category")
df["item_returned"]=df["item_returned"].astype(dtype="category")
df["return_reason"]=df["return_reason"].astype(dtype="category")



df["order_date"]=pd.to_datetime(df["order_date"])
df["signup_date"]=pd.to_datetime(df["signup_date"])
df["shipped_date"]=pd.to_datetime(df["shipped_date"])
df["delivered_date"]=pd.to_datetime(df["delivered_date"])
df["payment_date"]=pd.to_datetime(df["payment_date"])
df["return_date"]=pd.to_datetime(df["return_date"])


# column creation
df["order_year"]=df["order_date"].dt.year
df["order_month"]=df["order_date"].dt.month_name()


df.info()
print(df.head())

df.to_csv("Cleaned_data.csv",index=False)





































