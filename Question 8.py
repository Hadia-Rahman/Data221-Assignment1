# Question 8: Pandas DataFrame with Computed Column
# Create a data fram from the given data and then add a new coulomb using the existing column  print the final data frame
# Using the starter code

import pandas as pd
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}
data_frame = pd.DataFrame(data)
data_frame["D"] = data_frame["A"] + data_frame["B"] # data frame d is adding a and b together
print(data_frame)