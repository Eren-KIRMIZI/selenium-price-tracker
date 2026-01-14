import pandas as pd
from datetime import datetime
from bot import create_driver, scrape_book
from products import PRODUCTS

CSV_PATH = "data/prices.csv"


def load_old_data():
    try:
        return pd.read_csv(CSV_PATH)
    except FileNotFoundError:
        return pd.DataFrame(columns=["date", "site", "name", "price"])


def save_data(df):
    df.to_csv(CSV_PATH, index=False)


def main():
    driver = create_driver()
    old_data = load_old_data()
    new_rows = []

    for product in PRODUCTS:
        data = scrape_book(driver, product)
        data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_rows.append(data)

        previous = old_data[
            old_data["name"] == data["name"]
        ]

        if not previous.empty:
            last_price = previous.iloc[-1]["price"]

            if data["price"] < last_price:
                print(f"İNDİRİM VAR → {data['name']} | {last_price}£ → {data['price']}£")
            elif data["price"] > last_price:
                print(f"ZAM GELDİ → {data['name']} | {last_price}£ → {data['price']}£")
            else:
                print(f"FİYAT SABİT → {data['name']}")

    driver.quit()

    new_df = pd.concat([old_data, pd.DataFrame(new_rows)], ignore_index=True)
    save_data(new_df)


if __name__ == "__main__":
    main()
