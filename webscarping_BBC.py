#!/usr/bin/env python
# coding: utf-8

# In[9]:


from bs4 import BeautifulSoup
import requests
import csv


# In[34]:


url = "https://www.bbc.com/news"


# In[35]:


# fetch the content from url
response = requests.get(url)
html = response.content


# In[36]:


# Parse HTML content
soup = BeautifulSoup(html, 'html.parser')


# In[55]:


# Find elements containing headlines
elements = soup.find_all(["h2", "a"])


# In[67]:


# Create a CSV file and write the data
with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Headline', 'URL'])
    
    for element in elements:
        headline_text = element.text.strip()
        headline_url = element.get('href')
        writer.writerow([headline_text, headline_url])
    
print("Data scraping complete and saved to headlines;csv.")


# In[ ]:




