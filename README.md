# Selenium Price Tracker

This project is a simple and extensible price tracking application built with Python and Selenium.  
It scrapes real product data from a public website and tracks price changes over time.

The project is designed to demonstrate practical web automation, data extraction, and comparison logic using Selenium.

<img width="470" height="96" alt="image" src="https://github.com/user-attachments/assets/1f80ef00-778d-464a-b72f-a6c05c98d61d" />

<img width="252" height="38" alt="image" src="https://github.com/user-attachments/assets/498ccbc3-e253-4e9c-8ccc-a86d2bbb9978" />

---
## Project Structure

selenium-price-tracker/
│
├── bot.py
├── tracker.py
├── products.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
    └── prices.csv

## Features

- Scrapes real product data from a live website
- Extracts product name and price using CSS selectors
- Tracks historical prices
- Detects price increases and decreases
- Stores data in CSV format
- Headless browser support
- Easily extendable to other websites

---

## Target Website

The project uses the following website for scraping practice:

https://books.toscrape.com/

This site is intentionally built for web scraping practice and does not block automation tools.

---

## Technologies Used

- Python
- Selenium
- WebDriver Manager
- Pandas
- CSV data storage

## Possible Improvements

- Add email or Telegram notifications
- Track the same product across multiple websites
- Store data in a database (PostgreSQL, MSSQL)
- Create a REST API for price data
- Add scheduling for automatic daily tracking
- Replace Selenium with Requests where possible for better performance
