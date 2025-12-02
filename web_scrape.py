# A web scraper for 'Technolife' website products to fetch and display product names and prices.
# It allows users to add new product URLs, view saved URLs, and scrape product details.
# It saves the URLs in a JSON file for persistent storage.
#Some product URLs has been already added for testing purpose.
#--------------------------------------------------------------------------------------

#import necessary libraries
import requests
import bs4
import json

# Function to save URLs to a JSON file
def save_url(urls):
    with open("all_urls.json", "w", encoding="utf-8") as f:
        json.dump(urls, f, ensure_ascii=False, indent=4)

# Function to load URLs from a JSON file
def load_urls():
    try:
        with open("all_urls.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No saved URLs found. Try by adding new URLs first.")
        return []

# Function to load URLs from a JSON file in a list
all_urls = load_urls()

# Welcome message
print("Welcome To 'Technolife' Website Product's Price Web Scraper")

# Main loop
while True:
    # Display menu
    print("1.Add new url")
    print("2.Show results")
    print("3.Exit")
    choice = input("Enter your choice: ")

# Handle user choice
    if choice == "1":

        # Get new URL from user
        user_url = input("Enter url to scrape(it has to be from ThecnoLife Website and \nit has to be a product's page link(like the default links)): ")
        try:
            r = requests.get(user_url)
            all_urls.append(user_url)
            save_url(all_urls)
            print("✅ Url Successfully Saved")
        except requests.exceptions.RequestException as e:
            print(f"❌Failed to fetch the URL: {e}")

    elif choice == "2":

        # Show results for all saved URLs
        for i, url in enumerate(all_urls, start=1):
            try:
                r = requests.get(url)
                data = r.text
                soup = bs4.BeautifulSoup(data,"html.parser")
                selector_key = (r"#__next > div.w-full > main > div > div > article.flex.w-full.items-start.justify-between.gap-8 > "
                                    r"section.relative.mt-10.w-\[309px\].pl-4.xl\:w-\[392px\].\32 xl\:mr-3.\32 xl\:mt-0.\32 xl\:min-h-\[678px\].\32 xl\:w-96.\32 xl\:pl-0 >"
                                    r" div > div.min-w-0.max-w-\[293px\].xl\:max-w-\[376px\].grow.\32 xl\:w-full.\32 xl\:max-w-4xl.\32 xl\:grow-0 >"
                                    r" div > div.rounded-2xl.shadow-1200.\32 md\:\!px-4.\32 md\:\!pt-4.xl\:\!p-6.relative.w-full.p-6.transition-all.bg-white >"
                                    r" div.flex.w-full.flex-col.items-center > div.flex.w-full.justify-end.px-4.pb-4.pt-5 >"
                                    r" div > div > div > p.text-\[19px\].font-semiBold.\!leading-5.xl\:text-\[22px\].text-primary-shade-1")
                price_sel = soup.select(selector_key)
                heading = soup.select("#pdp_name")
                myPrice = price_sel[0]
                product_name = heading[0]
                print(f"📍{i}. Name: {product_name.text} \n Price: {myPrice.text} Toman")
            except Exception as e:
                print(f"❌Failed to scrape the URL {url}: {e}")

    # Exit the program
    elif choice == "3":
        print("Goodbye👋...")
        break

    # Handle invalid choice
    else:
        print("❌Invalid Choice❌")