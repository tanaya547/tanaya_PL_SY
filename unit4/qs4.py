import numpy as np
import pandas as pd
prices = np.array([300, 450, 600, 750, 500])
print("Average Book Price:", np.mean(prices))
data = {
    "Book": ["Python", "Java", "Data Science",
             "DBMS", "Cybersecurity"],
    "Price": prices
}
df = pd.DataFrame(data)

print("\nBook Price Details:")
print(df)

print("\nBooks costing more than 500:")
print(df[df["Price"] > 500])

"""
Output 

Average Book Price: 520.0

Book Price Details:
           Book  Price
0        Python    300
1          Java    450
2  Data Science    600
3          DBMS    750
4  Cybersecurity    500

Books costing more than 500:
           Book  Price
2  Data Science    600
3          DBMS    750
"""
