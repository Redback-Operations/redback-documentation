# REQUIREMENTS GATHERING SUMMARY REPORT
## PROJECT 1, 2, 3, 4, 5

_(Week 1, T2, 2024)_

### 1. Data Sources and Formats

| Project   | Current Data Sources                        | Future Data Sources | Data Formats           |
|-----------|---------------------------------------------|---------------------|------------------------|
| Project 1 | VR sensors                                   | -                   | JSON (assumed)         |
| Project 2 | External data IoT devices via ThingSpeak     | To be provided      | To be provided         |
| Project 3 | .fit files (Garmin, Strava)                 | -                   | CSV                    |
| Project 4 | OpenCV, supervision                         | Quantitative data from video/camera stream | Not specified  |
| Project 5 | User sessions, temporary data               | User logins, projects, responses, rewards system | JSON  |

### 2. Data Volume, Frequency, and Performance

| Project   | Data Volume           | Frequency        | Performance                  |
|-----------|-----------------------|------------------|------------------------------|
| Project 1 | A couple megabytes     | Every 10 seconds | No latency, speed, scalability requirement |
| Project 2 | 5-10GB                 | Real-time        | Not specified                |
| Project 3 | 50MB                   | -                | Not specified                |
| Project 4 | Normal to medium       | Real-time        | Not specified                |
| Project 5 | Small                  | Real-time        | Real-time access             |

### 3. Data Quality and Cleanup

| Project   | Data Quality           | Cleanup Required |
|-----------|------------------------|------------------|
| Project 1 | -                      | -                |
| Project 2 | To be provided         | To be provided   |
| Project 3 | Varies, mostly clean   | -                |
| Project 4 | To be assessed         | To be assessed   |
| Project 5 | No missing values or cleanup needed | -        |

### 4. Data Shape and Real-Time Needs

| Project   | Data Shape             | Real-Time Needs  |
|-----------|------------------------|------------------|
| Project 1 | Semi-structured         | -                |
| Project 2 | Structured or semi-structured (To be confirmed) | Real-time (To be confirmed) |
| Project 3 | Structured (CSV)        | -                |
| Project 4 | Real-time              | Real-time        |
| Project 5 | Research                | Real-time        |

### 5. Pain Points and Data Warehouse Need

| Project   | Pain Points            | Data Warehouse Need            |
|-----------|------------------------|---------------------------------|
| Project 1 | -                      | SQL server and API access       |
| Project 2 | ThingSpeak limitations | Needed for improvement          |
| Project 3 | No current need for data warehouse | Good practice but unnecessary |
| Project 4 | Need for pre-setup warehouse | Helpful for faster setup   |
| Project 5 | Lack of backend knowledge | External data solution needed |

### 6. Data Warehouse Setup Ideas

| Project   | Setup Ideas                            |
|-----------|----------------------------------------|
| Project 1 | SQL server, API access                 |
| Project 2 | Ideas for preprocessing                |
| Project 3 | SQL database, API                      |
| Project 4 | Prefer MongoDB, API for UI streaming   |
| Project 5 | External data solution, integration with EC2 |

---

## Projects with Similar Requirements

### Real-Time Data Needs
- **Project 2:** Requires real-time data for tasks like fall detection (To be confirmed).
- **Project 4:** Uses real-time streaming data from video/camera stream.
- **Project 5:** Needs real-time access for its live service.

### Data Warehouse Requirement
- **Project 1:** SQL server setup and API access.
- **Project 2:** Data warehouse needed to overcome ThingSpeak limitations.
- **Project 4:** Data warehouse setup would help in faster implementation.
- **Project 5:** External data solution with data warehouse team support.



### Data Formats
- **Project 1:** Assumed to use JSON format.
- **Project 5:** Uses JSON format for data configuration.

### Pain Points with Current Data Methods
- **Project 2:** Limited functionalities with ThingSpeak.
- **Project 4:** Pre-setup warehouse would speed up the process.
- **Project 5:** Lack of backend knowledge in the team.

### Ideas for Data Warehouse Setup
- **Project 1:** SQL server and API.
- **Project 4:** Prefers MongoDB with API for UI streaming.
- **Project 5:** External data solution integrated with EC2.