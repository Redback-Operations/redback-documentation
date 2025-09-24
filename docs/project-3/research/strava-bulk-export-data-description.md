# Strava Bulk Export Data Description

This document explains the origin of the Strava data used in the Cycling analysis sub-project which was obtained through a bulk export of a team members workout data. The data contained details for multiple sports but the cycling data can be separated for analysis as part of this project.

This document describes the cycling data available with the focus on how the data can be used for building predictive ML models.

## Top level directory

The top level directory contains many .csv files - most of which are not relevant or only slightly relevant for our analyses. There is often around 40+ such files and only a small number contain information that we will use:

1.  **activities.csv**: A summary tab;e of the workouts included in the doeanload. This contains many summary fields such as duration, distance, average and maximum speed, average and maximum power, and average and maximum cadence. It also includes a link to a .fit, .gpx to .tcx file for the workout that contains the specific data recorded for that individual workout.
    
    **Note:** The average speed is on recorded if there is a device for the workout measuring speed. It is not calculated from elapsed moving time and duration if there has been no speed recording device.
    
2.  **bikes.csv**: Details of bikes that the account holder has entered into their Strava account.
    
3.  **comments.csv**: Comments that have been recorded by the user for any of the recorded workouts. This is free form text and the comments can be anything from a description of the workout to saying hello to a fellow Strava user.
    
4.  **profile.csv**: Information about the account holder including name, email address, state, country, sex and weight.
    

Strava will provide estimates for some fields in the activities.csv file rather than actual measurements. This is true for average power and we want to exclude any entries that are not actual measurements for this field. The underlying .fit file will show actual measured values where they exist.

## Sub-directories

The download also creates four sub-directories:

1.  **activities**: Contains the .fit, .gpx to .tcx files for each workout where they have been recorded.
    
2.  **clubs**: Details of any Clubs the account holder has defined or joined.
    
3.  **media**: Any photos or videos that the account holder has uploaded with their workouts.
    
4.  **routes**: Any routes that the account holder has defined in Strava.
    

Of these sub-directories, the one that is used by our project is the **activities** directory.

## Activity file fields

The fields included in the .fit files for rides with power data measured are:

1.  **altitude**: Altitude above sea level (m).
    
2.  **cadence**: Pedal cadence, indicating the rate at which a cyclist is pedaling in revolutions per minute (RPM).
    
3.  **combined\_pedal\_smoothness**: A measure of how smoothly the cyclist is pedaling, indicating pedaling efficiency.
    
4.  **distance**: The cumulative distance traveled during the cycling activity (m).
    
5.  **enhanced\_altitude**: An enhanced measure of altitude (m).
    
6.  **enhanced\_speed**: Speed calculated using GPS or sensor data, typically measured in kilometres per hour (km/h).
    
7.  **gps\_accuracy**: The accuracy level of the GPS signal (m).
    
8.  **grade**: The incline or decline grade of the road, expressed as a percentage.
    
9.  **heart\_rate**: The cyclist's heart rate in beats per minute (BPM).
    
10.  **left\_right\_balance**: The balance between the left and right pedal strokes.
    
11.  **left\_torque\_effectiveness**: The efficiency of torque application during the left pedal stroke.
    
12.  **position\_lat**: The latitude coordinate from the GPS data.
    
13.  **position\_long**: The longitude coordinate from the GPS data.
    
14.  **power**: The cyclist's power output in (W).
    
15.  **right\_torque\_effectiveness**: The efficiency of torque application during the right pedal stroke.
    
16.  **speed**: The cycling speed, typically measured (km/h).
    
17.  **temperature**: The ambient temperature (Celsius).
    
18.  **timestamp**: The date and time for each recorded data point.
    

## Data features and characteristics

There are numerous unusual features of the dataset. The notable aspects are:

*   Average speed is only included in **activities.csv** when there is a speed measurement device and will not be calculated from distance and moving time.
    
*   Average power in the **activities.csv** may be calculated rather than measured and is not a reliable indicator of whether a power measurement device has been used for the activity. Instead, only Weighted Average Power.
    

## Data manipulations

The measurements for individual rides are provided in .fit.gz files. These files are compressed .fit files which is a binary file format. A Python program was created to read these files and write them out as CSVs for easier processing.

The python code and notebook related to this exploration is available at [Strava Data Exploration](https://github.com/Redback-Operations/redback-fit-sports-performance/blob/main/Cycling%20Analysis/Strava%20explorer.ipynb).

# Importing a Strava workout database

## 1. Export the data from Strava

To import a Strava workout database, you will need to export the data from Strava. This can be done by following these steps:
* Log in to your Strava account.
* Click on your profile picture in the top right corner of the screen.
* Select 'Settings' from the dropdown menu.
* Click on 'My Account' in the left-hand menu.
* Scroll down to the 'Download or Delete Your Account' section.
* Click on 'Get Started' under 'Download Your Data'.
* Select the data range you want to export and click 'Request Your Archive'.
* Wait for Strava to prepare your data and send you an email with a link to download it.
* Download the data and extract the files to a location on your computer.

## 2. Clean the data

The [Strava Data Exploration](https://github.com/Redback-Operations/redback-fit-sports-performance/blob/main/Cycling%20Analysis/Strava%20explorer.ipynb) notebook contains code to clean the data and export it to the csv format used by the prediction models.

To clean the data:

* Set the 'source_path' variable in the cell marked as 2.1 to the location of the Strava data export.
* Set the 'athlete_id' variable to the value that you want to use to identify this athlete. The example uses 'TRI001' as the data is from a triathlete and it is the first triathlete included.
* Run the three cells under the 2.1 heading to clean up the data and filter the Ride, Run and Swim data that contains enough information for the models to use.
* Run the cell under the 2.2 heading to export the data to the csv format used by the prediction models.

## 3. Load the data into the GitHub repository

Once you have cleaned the data, you can load it into the GitHub repository for use by the prediction models. This will involve checking in the 'extended_activities_athlete_id.csv' file that was created in the 2.2 cell and all the .csv.gz files for the individual session data.

Create the pull request that includes these files.
