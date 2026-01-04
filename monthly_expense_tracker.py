import pandas as pd
import numpy  as np

data={
    "Date": pd.date_range(start="2026-01-01", periods=10),

    "category":["food","rent","college_fees","bills","shoping",
                "outing","travel","study_material","food","travel"],
    "amount":[2000,3500,1000,500,500,500,200,600,200,300]            
}

df= pd.DataFrame(data)

print("expense data:")
print(df)

total_expense =np.sum(df["amount"])
print("\n total Monthly Expense:",total_expense)

category_expense= df.groupby("category")["amount"].sum()
print("\n category_wise Expense:")
print(category_expense )

highest_category_expense= category_expense.idxmax()
print("\nhighest expnese category:",highest_category_expense)

lowest_category_expense=category_expense.idxmin()
print("\nlowest expanese category:",lowest_category_expense)

avrage_daily = np.mean(df["amount"])
print("\n average daily expense:",avrage_daily)

