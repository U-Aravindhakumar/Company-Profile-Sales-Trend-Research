'''import pandas as pd
import random
from googlesearch import search
import time

# 📦 Simulated list of 100 Tamil Nadu companies (replace with real names if needed)
company_names = [f"Company {i}" for i in range(1, 101)]

# 🏭 Sample industries and locations in TN
industries = ['IT', 'Textiles', 'Manufacturing', 'Automobile', 'Pharma', 'Education']
locations = ['Chennai', 'Coimbatore', 'Madurai', 'Tirunelveli', 'Trichy', 'Salem']
employee_range = ['10-50', '51-200', '201-500', '500-1000', '1000+']

data = []

for name in company_names:
    print(f"Searching for {name}...")
    try:
        # 🔍 Get website using Google search
        query = f"{name} Tamil Nadu official site"
        website = next(search(query, num=1, stop=1, pause=2))
    except Exception as e:
        website = "Not found"

    row = {
        "Company Name": name,
        "Industry": random.choice(industries),
        "Location": random.choice(locations),
        "Website": website,
        "Employee Size": random.choice(employee_range)
    }
    data.append(row)
    time.sleep(1)  # polite scraping

# 📄 Convert to DataFrame and save to Excel
df = pd.DataFrame(data)
df.to_excel("TamilNadu_Companies.xlsx", index=False)

print("✅ Data saved to TamilNadu_Companies.xlsx")'''

import pandas as pd
import requests
from bs4 import BeautifulSoup
input_file = "manual_company_list_expected.xlsx"
df = pd.read_excel(input_file)
df["Website Title"] = ""

for idx, row in df.iterrows():
    company = row['Company Name']
    website = row['Website']
    try:
        print(f"Scraping: {company} -> {website}")
        response = requests.get(website, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string.strip() if soup.title else "No title found"
        df.at[idx, "Website Title"] = title
    except Exception as e:
        print(f"Failed to scrape {website}: {e}")
        df.at[idx, "Website Title"] = "Error"
output_file = "scraped_company_titles.xlsx"
df.to_excel(output_file, index=False)

print("✅ Scraping completed. Results saved to", output_file)




