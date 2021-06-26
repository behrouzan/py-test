import pandas as pd

# nba = pd.read_csv('files/nba_data.csv')

# print(type(nba))
# print(len(nba))  # len() is python built-in func

# print(nba.shape)  # shape is an attribute of DataFrame
# The result is a tuple containing the number of rows and columns

# print(nba.head)
# print(nba.tail)
# print(nba.info())

# =================================================
# pandas has int64, float64 and object as data types
# there is also categorical data type which is more complicated
# object is “a catch-all for columns that Pandas doesn’t recognize as any other specific type.”
#  In practice, it often means that all of the values in the column are strings.
# =================================================

# print(nba.describe())
# print(nba['gameorder'].describe())

# .describe() only analyzes numeric columns by default
# but you can provide other data types if you use the include parameter

# print(nba.describe(include=np.object))

# above code uses np.object which is now a part of python built in commands
# we can use object itself
# looks like without 'object' it also works for object columns
# print(nba["game_id"].describe(include=object))
# print(nba["game_id"].describe())

# .describe() won’t try to calculate a mean or a standard deviation for the object columns
# since they mostly include text stri

# print(nba.loc[nba["fran_id"] == "Lakers", "team_id"])      # select on column
# print(nba.loc[nba["fran_id"] == "Lakers", ("team_id", "date_game")])   # select multiple column
# print(nba.loc[nba["fran_id"] == "Lakers"].value_counts())    # selects all columns

# print(nba.loc[nba["team_id"] == "MNL", "date_game"].min())
# print(nba.loc[nba["team_id"] == "MNL", "date_game"].max())
# print(nba.loc[nba["team_id"] == "MNL", "date_game"].agg(("min", "max")))


# pandas Series vs numpy array
# pd_arr = pd.Series([3, 4, 5, 6])
# np_arr = np.array([3, 4, 5, 6])

# print(pd_arr)  # this is a numpy 2-D array
# print(np_arr)

# print(pd_arr.values)  # this is a numpy array
# print(pd_arr.index)

# the values of a Series object are actually n-dimensional arrays
# pandas uses numpy behind the scenes

# a pandas Series has both abilities in indexing ==>> by numeric index is default
# series1 = pd.Series([1, 2, 3, 4], index=["one", "two", "three", "four"])
# print(series1[1])
# print(series1["two"])

# creating pandas series using python dictionary
# series2 = pd.Series({"Amsterdam": 5, "Tokyo": 8})  # ere we can pass a dictionary
# print(series2["Tokyo"])
# print(series2[0])

# we can use dictionary functions in series
# print(series2.keys())
# print("Tokyo" in series2)

# combine Series to create DataFrame
city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8, "Shiraz": 12})
city_revenues = pd.Series([4200, 8000, 6500], index=["Amsterdam", "Toronto", "Tokyo"])


city_data = pd.DataFrame({"revenue": city_revenues, "employee_count": city_employee_count})
print(city_data)

print(city_employee_count.index)   # index for Series
print(city_data.index)   # index for dataFrame
print(city_data.values)

print(city_data.axes)   # get axes of a Data Frame
print(city_data.axes[0])
print(city_data.axes[1])

print(city_revenues.axes)   # these are numpy  ==>> get axes of a Series
