from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Sample data loading. Replace this with the path to your actual data file.
data_path = 'futureDemands/sample_sales_data.csv'
df = pd.read_csv(data_path)

# Convert Date column to datetime type and sort the dataframe by date
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Assuming 'Date' is the independent variable and 'Sales' is the dependent variable
# Convert 'Date' to ordinal form (number of days) since linear regression needs numerical values
df['Date'] = df['Date'].map(lambda x: x.toordinal())

# Splitting the dataset into training and testing sets
X = df[['Date']]
y = df['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict the test set results
y_pred = model.predict(X_test)

def ordinal_to_datetime(ordinal_dates):
    return [datetime.fromordinal(int(date)) for date in ordinal_dates]

# Convert X_train and X_test ordinal dates back to datetime
X_train_dates = ordinal_to_datetime(X_train['Date'])
X_test_dates = ordinal_to_datetime(X_test['Date'])

# Create the plots
fig, ax = plt.subplots()

# Visualizing the Training set results
ax.scatter(X_train_dates, y_train, color = 'red')
ax.plot(X_train_dates, model.predict(X_train), color = 'blue')
ax.set_title('Sales vs Date (Training set)')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
# Format the date into a readable format
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate() # Rotation

plt.show()

# Visualizing the Test set results
fig, ax = plt.subplots()
ax.scatter(X_test_dates, y_test, color = 'red')
ax.plot(X_train_dates, model.predict(X_train), color = 'blue') # use the same regression line
ax.set_title('Sales vs Date (Test set)')
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
# Format the date
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate() # Rotation

plt.show()