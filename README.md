# 🕷 Simple Web Scraper

A tiny and clean web scraping project built with Python.  
This script fetches data from a website and extracts useful information automatically.

---

## 🚀 Features
- Fast and lightweight
- Easy to customize
- Beginner-friendly structure
- Clean output formatting
- Uses popular scraping libraries

---

## 🛠 Requirements
Before running the project, install the following packages:

```bash
pip install requests beautifulsoup4
```

## ▶️ How to Run
- You can run this program by going to it's folder in CMD and run this command :

```
python scraper.py
```
## 📄 Example Output

```
📍1. Name: Example Name
Price: 7,200,000 Toman

📍2. Name: Example Name
Price: 4,200,000 Toman
```

## 🧠 How It Works

1. Sends an HTTP request to the website

2. Downloads the page HTML

3. Parses the HTML content

4. Extracts required data

5. Displays or saves the output

## 🌐 Current Target Website

This version of the scraper is currently configured for the **Technolife** website.

If you want to scrape other pages of Technolife or completely different websites,  
you must change the value of `selector_key` inside the code.

### 🔧 How to Customize

Inside the script, find these variables and change it to whatever selector you like:

```python
selector_key = "..." # For price of the product 
```
```python
heading_selector = "..." # For name of the product
```

# 💡 Tip

- To find the correct selector:

- Right click on the element you want

- Click **Inspect**

- Right click on the element in DevTools

- Choose **Copy** → **Copy Selector**

- Paste it into ```selector_key``` OR ```heading_selector```

Example: 
```python
selector_key = "div.product-title > h1"
```

## ⚠ Disclaimer

This project is for educational purposes only.
Do not use it to scrape websites that disallow bots or violate their terms of service.

## 📌 Author

Made with ☕ and Python by Amir

