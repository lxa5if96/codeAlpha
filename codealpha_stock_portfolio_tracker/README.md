# Stock Portfolio Tracker

A simple Python-based stock portfolio tracker that allows users to:

- View available stocks
- Buy stocks
- Track total investment
- Save portfolio data into a text file

---

## Features

- View stock prices
- Buy stocks with quantity
- Calculate total investment
- Save portfolio to `portfolio.txt`
- Beginner-friendly Python project

---

## Technologies Used

- Python

---

## Project Structure

```text
stock_portfolio_tracker/
│
├── main.py
├── portfolio.txt
└── README.md
```

---

## Available Stocks

| Stock | Price |
|---|---|
| AAPL | 180 |
| TSLA | 250 |
| MSFT | 420 |
| AMZN | 190 |
| GOOGL | 170 |

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/lxaa5if96/codeAlpha.git
```

### 2. Open project folder

```bash
cd stock_portfolio_tracker
```

### 3. Run the program

```bash
python main.py
```

---

## Example Menu

```text
1. View Stock
2. Buy Stock
3. View Total Investment
4. Save as file
5. Exit
```

---

## Example Output

```text
Enter stock name: AAPL
Enter stock quantity: 2

Stock bought Successfully.
```

---

## File Saving

Portfolio data is saved in:

```text
portfolio.txt
```

Example:

```text
AAPL - quantity:2 - price per stock:180
-----------------------------------------
Total Investment: 360
```

---

## Author

ASIF

---

## Future Improvements

- Add stock selling feature
- Add real-time stock prices using APIs
- Add GUI interface
- Store data using database
- Add profit/loss tracking