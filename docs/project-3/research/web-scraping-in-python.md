# Web Scraping in Python

## Introduction

Web scraping is a powerful technique used to extract data from websites, providing valuable information. It involves using software tools to navigate and interact with web pages, download and parse HTML, and extract relevant information. Web scraping allows users to gather data from various online sources, transforming unstructured web data into a structured format that can be analyzed, stored, or used for various applications. However, it's important to note that web scraping should be performed ethically and in compliance with the terms of service of the websites being accessed.

## Python Web Scraping libraries

1.  **Urllib3:**
    
    *   A powerful HTTP client library for performing HTTP requests programmatically.
        
    *   Handles HTTP headers, retries, redirects, SSL verification, connection pooling, and proxying.
        
2.  **BeautifulSoup:**
    
    *   Used to parse HTML and XML documents.
        
    *   Provides an API to navigate HTML document trees and extract tags, meta titles, attributes, text, and other content.
        
    *   Known for robust error handling.
        
3.  **MechanicalSoup:**
    
    *   Automates the interaction between a web browser and a website.
        
    *   Offers a high-level API for web scraping that simulates human behavior.
        
    *   Allows interaction with HTML forms, clicking buttons, and other user-like actions.
        
4.  **Requests:**
    
    *   A simple and powerful library for making HTTP requests.
        
    *   Designed to be easy to use with a clean and consistent API.
        
    *   Handles GET and POST requests, cookies, authentication, and other HTTP features.
        
    *   Widely used in web scraping due to its simplicity.
        
5.  **Selenium:**
    
    *   Automates web browsers like Chrome, Firefox, and Safari.
        
    *   Simulates human interaction with websites, allowing actions such as clicking buttons, filling forms, and scrolling pages.
        
    *   Used for testing web applications and automating repetitive tasks.
        
6.  **Pandas:**
    
    *   Enables storing and manipulating data in various formats (CSV, Excel, JSON, SQL databases).
        
    *   Useful for cleaning, transforming, and analyzing data extracted from websites.
        

These libraries offer diverse functionalities, from HTTP requests to HTML parsing and browser automation, making them essential tools for web scraping tasks in Python. Choose the library that best suits your specific scraping needs and project requirements.

## Web Scraping Process

### 1\. **Identify Data Sources**

*   **Select Relevant Website:** Choose a website for scraping.
    

### 2\. **Choose Web Scraping Tools**

Select appropriate Web Scraping libraries from the ones mentioned above.

### 3\. **Understand Website Structure**

*   Understand the website structure by inspecting HTML code.
    
*   Right-click on the webpage, select "Inspect," and note element class names and IDs.
    

### 4\. **Write Scraping Code**

*   Send an HTTP GET request using requests.
    
*   Parse HTML code with BeautifulSoup.
    
*   Extract relevant data and store it in a Pandas dataframe.
    
*   Add a delay between requests to avoid overwhelming the website.
    

Additional Help:

**read\_html function in Pandas**`:` Handy for extracting tabular data from HTML web pages.   
Data Source url : ['https://www.espncricinfo.com/records/tournament/team-match-results/icc-cricket-world-cup-2023-24-15338']  
The following code gets the list of all tables in the url.The tables will be indexed in the order in which they occur in the web page.

**Code:**

*   ```
    tables = pd.read\_html(url)
    ```
    

**Using BeautifulSoup**

Beautiful Soup is a Python library designed for pulling data from HTML files. It is particularly useful when dealing with web pages containing tables with links to other pages. In the scenario presented below, the 'Ground' and 'Scorecard' columns each contain links to additional webpages.

## Steps to Use BeautifulSoup:

1.  **HTTP Request:**
    
    *   Send an HTTP request to the webpage and store the HTML content as text.
        
    
    ```
    response = requests.get('url\_of\_the\_webpage') 
    html\_content = response.text
    ```
    
    **Create BeautifulSoup Object:**
    
    *   Create a BeautifulSoup object to parse the HTML using the obtained response.
        
    
    ```
    soup = BeautifulSoup(html\_content, 'html.parser')
    ```
    
    **Locate HTML Table:**
    
    *   Locate the HTML table using appropriate tags and attributes.
        
    
    ```
    table = soup.find('table', {'id': 'table1'})
    ```
    
    **Extract Links:**
    
    *   Initialize an empty list to store links.
        
    *   Iterate through the rows of the table, find all anchor tags, and append the links to the list.
        
    
    ```
    for row in table.find\_all('tr'):
        for link in row.find\_all('a',href= True):
    #Get the value of 'href' attribute (link)
            href=link\['href'\]
            links.append(href)
    ```
    
    To filter specific categories from the mixed list of links, apply slicing techniques.
    
    *   Run a loop through the list and use the `read_html` function to extract tables from each link.
        
    
    **Print Results:**
    
    *   To view the extracted links, simply print the list.
        
    
    **Note:** Detailed code for the example can be found at [https://github.com/redbackoperations/Projects/blob/main/Sports Performance Analysis/frontend/Cricket Analysis/web\_scraping\_cric\_analysis.ipynb](https://github.com/redbackoperations/Projects/blob/main/Sports%20Performance%20Analysis/frontend/Cricket%20Analysis/web_scraping_cric_analysis.ipynb)
    

### 5\. **Export Extracted Data**

*   Export scraped data as a CSV file using Pandas.
    

### 6\. **Verify Extracted Data**

*   Open the CSV file to ensure the data has been successfully scraped and stored.
    

**Dynamic Content:** For websites with dynamic loading (e.g., JavaScript-based content), consider using tools like Selenium for web scraping.

* * *

## ![(blue star)](https://ntbsoftware.atlassian.net/wiki/s/-771138381/6452/4fb6d8feb6fbd7b1ec042e4c238d3e2208ec7a44/_/images/icons/emoticons/72/1f4d8.png) Instructions - Step by Step

Web scraping involves extracting data from websites. Here's a step-by-step summary of using Python to scrape website data:

1.  Choose the Website and Webpage URL
    
2.  Inspect the website
    
3.  Installing the important libraries
    
4.  Write the Python code
    
5.  Exporting the gathered data
    
6.  Confirming the collected data
    

* * *

## Authors

This comprehensive guide on web scraping was created collaboratively by Ramya Sekar and Adarsh Kallungal Sivaram. Ramya created the page and set the initial structure, while Adarsh added valuable insights and extra information to enrich the content.