import pandas as pd
import mplfinance as mpf

def plot_candlestick(data):
    # Convert the 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Sort the data by date in ascending order
    data.sort_values(by='Date', inplace=True)

    # Set the 'Date' column as the index
    data.set_index('Date', inplace=True)

    # Plot the candlestick chart with increased chart size for wider candlesticks
    mpf.plot(data, type='candle', volume=True, show_nontrading=True,
             style='yahoo', figratio=(16, 9), figscale=1.5)

if __name__ == "__main__":
    # Replace 'absolute_file_path' with the actual absolute path to your CSV file
    file_path = 'C:/Users/HARSH KUMAR/Desktop/Python Projects/PlottingUsingPython/TSLA.csv'

    # Read the CSV file into a pandas DataFrame
    stock_data = pd.read_csv(file_path)

    # Call the function to plot the candlestick chart
    plot_candlestick(stock_data)




