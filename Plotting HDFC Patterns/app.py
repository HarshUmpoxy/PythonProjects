import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the CSV file into a DataFrame
df = pd.read_csv('hdfcbank.csv')

# Convert the 'Date' column to a datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date
df = df.sort_values('Date')

# Prepare the data for linear regression
X = df.index.values.reshape(-1, 1)
y = df['Close'].values

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict closing prices using the model
predicted_prices = model.predict(X)

# Plot the actual closing prices and the predicted trend line
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Actual Closing Prices')
plt.plot(df['Date'], predicted_prices, label='Trend Line', linestyle='--', color='red')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('HDFC Bank Stock Price Trend')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
