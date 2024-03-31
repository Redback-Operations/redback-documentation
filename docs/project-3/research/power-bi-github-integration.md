# Power BI & GitHub Integration

## Introduction

**Power BI** and **GitHub** are powerful tools in data analysis and software development, respectively. Integrating Power BI with GitHub allows users to visualise and analyse data hosted on GitHub repositories. The primary advantage of this integration is the seamless update process. Any modifications made to the data in GitHub are easily synchronised with the Power BI dashboard, eliminating the need to establish a new connection for each update.

This guide provides a step-by-step guide approach to establish a direct connection between Power BI and GitHub, enabling efficient data analysis and reporting.

## Step-by-Step Guide

### Finding Data in GitHub

1.  Identify the repository containing the data you wish analyse, and navigate to the data file you wish to use.
    

![image-20240319-042842.png](./attachments/image-20240319-042842.png)

2.  Click **Raw**.
    

![image-20240319-042850.png](./attachments/image-20240319-042850.png)

3.  Copy the URL.
    

![image-20240319-042902.png](./attachments/image-20240319-042902.png)

### Connecting GitHub Data to Power BI

1.  Open Power BI and select **Get Data**.
    
2.  Choose **Web** as the data source.
    

![image-20240319-042914.png](./attachments/image-20240319-042914.png)

3.  Paste the copied URL from GitHub and click **OK**.
    

![image-20240319-042922.png](./attachments/image-20240319-042922.png)

4.  Check the data load appears correct and adjust parameters as required. Use the Power Query Editor in Power BI to transform or modify the data as needed.
    

![image-20240319-042932.png](./attachments/image-20240319-042932.png)

5.  Load the data to create reports and visualisations.
    

![image-20240319-042940.png](./attachments/image-20240319-042940.png)

## Useful Resources

*   Power BI Documentation: [Power BI documentation - Power BI | Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/)
    
*   GitHub Help Documentation: [GitHub Docs](https://docs.github.com/en)