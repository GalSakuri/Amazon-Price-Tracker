# Amazon Price Tracker & Notifier

A simple Python script that scrapes the current price of a specified Amazon product and sends you an email alert when the price drops below your target.

---

## Features

- Fetches the live price of an Amazon product page  
- Compares against a user‑specified target price  
- Sends an email notification via Gmail SMTP when the price falls below the target  

---

## Requirements

- Python 3.7+  
- A Gmail account (for SMTP alerts)  
- An Amazon product URL  

---

## Setup

1. **Clone this repository**  
   ```bash
   git clone https://github.com/<your‑username>/amazon-price-tracker.git
   cd amazon-price-tracker

2.	Create & edit a .env file
In the project root, create a file named .env containing:
```bash
    MY_EMAIL=your‑gmail-address@gmail.com
    MY_PASSWORD=your‑gmail‑app‑password
```
 - MY_EMAIL: the Gmail address you’ll send from (and to)
 - MY_PASSWORD: an App Password generated in your Google Account (not your regular login password)

---

## Usage
1.	Run the script
```bash
    python main.py
```

 2.	Enter your target price when prompted:
```bash
    What your tagert price for that product? : 120 
```

 3. The script will:
	-	Scrape the current price from the Amazon product page
	-	If the price is lower than your target, send an email to your MY_EMAIL

---

## Customization
  - Change product URL
    In main.py, update the Product_URL constant to any Amazon product page URL.
	-	Modify headers
    If scraping fails, you can adjust the headers dict to mimic a different browser or locale.

---

## How it works
  -	Load environment variables via python-dotenv.
	-	Fetch page HTML using requests with custom headers.
  -	Parse price with BeautifulSoup, extracting the element with class a-offscreen.
	-	Compare the scraped price (float) to your entered target.
  - Send email using Gmail’s SMTP server if the condition is met.

---

License

This project is open‑source and free to use under the MIT License.
