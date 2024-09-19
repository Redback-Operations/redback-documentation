---
sidebar_position: 5
sidebar_label: Dremio api (for data analysts)
---

## How to access data stored in dremio datawarehouse (for data analysts)
<br>

### Connecting to deakins network
First part of accessing the datawarehouse is connecting to deakins network which requires downloading and connecting to deakins network using [anyconnect VPN](https://www.deakin.edu.au/students/student-life-and-services/health-wellbeing-and-safety/safety-security/online-safety-security/secure-your-devices/vpn)

Once there select your operating system which will redirect you to a guide explaining how to download, install and connect to deakins network. (If you get a permission error saying you dont have access ensure you are logged in at the top right after the redirection)
<br>

### Making a SQL request to dremio in jupyter
The first step in ensuring you have the correct packages installed. Required for this guide can be downloaded with this command.
```sh
pip install requests pandas
```
<br>

Then import these into your notebook. 
```python
import requests
import json
import pandas as pd
```
<br>

After that declare the api url exactly as below.
```python
api_url = "http://10.137.0.149:5001/dremio_query"
```
<br>


Then declare the headers.
```python
headers = {
    "Content-Type": "application/json"
}
```
<br>


Then the sql query you wish to query the database with.
```python
sql_query = {
    "sql": "SELECT * FROM \"project-3\" \"extended_activities\" LIMIT 10;"
}
```

As of writing this documentation, users of this api are restricted to using only ``` SELECT ``` queries to prevent malicous use. There is also two usable sources being project-3 and project-2 though the tables within those sources are subject to change in which this documentation will likely be updated with a directory guide.
<br>

Then send the post request and store the response.
```python
response = requests.post(api_url, headers=headers, data=json.dumps(sql_query))
```
<br><br>

Parse the JSON reponse.
```python
result = response.json()
```
<br>

Finally convert it into data frame.
```python
df = pd.DataFrame(result['rows'])
```
<br>

Which you can use just like any other dataframe like:
```python
display(df)
```