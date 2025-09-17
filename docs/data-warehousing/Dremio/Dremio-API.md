---
sidebar_position: 3
sidebar_label: Dremio API
---

# How to access data stored in dremio datawarehouse (for data analysts)

:::info
**Document Creation:** 21 September, 2024. **Last Edited:** 21 September, 2024. **Authors:** Kaleb.
<br></br> **Document Code:** DRE2. **Effective Date:** 21 September, 2024. **Expiry Date:** 21 September, 2025.
:::

### Making a SQL request to dremio in jupyter
The first step in ensuring you have the correct packages installed. Required for this guide can be downloaded with this command.
```sh
pip install requests pandas
```
<br></br>

Then import these into your notebook. 
```python
import requests
import json
import pandas as pd
```
<br></br>

After that declare the api url exactly as below.
```python
api_url = "http://10.137.0.149:5001/dremio_query"
```
<br></br>


Then declare the headers.
```python
headers = {
    "Content-Type": "application/json"
}
```
<br></br>


Then the sql query you wish to query the database with.
```python
sql_query = {
    "sql": "SELECT * FROM \"project-3\" \"extended_activities\" LIMIT 10;"
}
```

As of writing this documentation, users of this api are restricted to using only ``` SELECT ``` queries to prevent malicous use. There is also two usable sources being project-3 and project-2 though the tables within those sources are subject to change in which this documentation will likely be updated with a directory guide.
<br></br>

Then send the post request and store the response.
```python
response = requests.post(api_url, headers=headers, data=json.dumps(sql_query))
```
<br></br><br></br>

Parse the JSON reponse.
```python
result = response.json()
```
<br></br>

Finally convert it into data frame.
```python
df = pd.DataFrame(result['rows'])
```
<br></br>

Which you can use just like any other dataframe like:
```python
display(df)
```