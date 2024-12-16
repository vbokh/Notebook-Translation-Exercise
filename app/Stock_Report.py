from pandas import read_csv
from plotly.express import line
from alpha_service import API_KEY  # Importing API_KEY, dotenv setup handled there

def fetch_stocks_csv(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&outputsize=full&datatype=csv"
    df = read_csv(request_url)
    return df

if __name__ == "__main__":
    # SELECT A SYMBOL
    symbol = input("Please input a symbol (e.g. 'NFLX'): ") or "NFLX"
    print("SYMBOL:", symbol)

    # FETCH THE DATA
    df = fetch_stocks_csv(symbol)

    print(df.columns)
    print(len(df))
    print(df.head())

    # Challenge A
    #
    # What is the most recent adjusted closing price? And the corresponding date?
    print("-------------------------")
    print("LATEST CLOSING PRICE:")
    first_row = df.iloc[0]
    print(f"${first_row['adjusted_close']} as of {first_row['timestamp']}")

    # Challenge B
    #
    # What is the average, median, min, and max adjusted closing price
    # (over the latest 100 available days only)?
    recent_df = df.iloc[0:100]  # Use slicing or df.head(100)
    print(len(recent_df))

    print("-------------------------")
    print("RECENT STATS...")
    print(f"MEAN PRICE: ${recent_df['adjusted_close'].mean():.2f}")
    print(f"MEDIAN PRICE: ${recent_df['adjusted_close'].median():.2f}")
    print(f"MIN PRICE: ${recent_df['adjusted_close'].min():.2f}")
    print(f"MAX PRICE: ${recent_df['adjusted_close'].max():.2f}")
    # Quantiles for additional insight
    print(f"75TH PERCENTILE: ${recent_df['adjusted_close'].quantile(.75):.2f}")
    print(f"25TH PERCENTILE: ${recent_df['adjusted_close'].quantile(.25):.2f}")

    # Challenge C
    #
    # Plot a line chart of adjusted closing prices over time (all time).
    fig = line(
        x=df["timestamp"],
        y=df["adjusted_close"],
        title=f"Stock Prices ({symbol})",
        labels={"x": "Date", "y": "Stock Price ($)"},
    )
    fig.show()
