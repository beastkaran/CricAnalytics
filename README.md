# Cricket Match Analysis Dashboard

## Overview
This project is a **Power BI dashboard** that provides **real-time cricket match analysis** using the Cricbuzz API. It fetches live match data and presents insights on team performance, player statistics, and match trends.

Additionally, we developed a **website** that enhances the analysis by offering detailed player statistics, AI-generated strategy suggestions, and match history insights.

## Features
- **Live Data Integration**: Fetches real-time cricket match data via the **Cricbuzz API**.
- **Player & Team Analysis**: Visualizes player performance, team strategies, and match outcomes.
- **Power BI Dashboards**: Interactive reports including graphs, tables, and charts.
- **Automated Data Refresh**: Keeps the data updated at scheduled intervals.
- **Website with AI Strategy Generator**: Analyzes player strengths and weaknesses, provides AI-generated strategy tips, and includes video analysis.

## Tech Stack
- **Power BI**: For data visualization and dashboard creation.
- **Power Query (M Language)**: To process API requests.
- **Cricbuzz API (RapidAPI)**: For fetching live cricket match data.
- **JSON**: Used for handling API integration in Power BI.
- **Streamlit (Python)**: Used for frontend development.
- **AI Integration**: Provides strategy recommendations based on player statistics.

## Setup Instructions
### Prerequisites
- Install **Power BI Desktop** ([Download Here](https://powerbi.microsoft.com/)).
- Create a **RapidAPI account** and get an API key for Cricbuzz.

### Clone This Repository
```sh
git clone https://github.com/your-username/cricket-analysis-powerbi.git
cd cricket-analysis-powerbi
```

### Configure API in Power BI
1. Open **Power BI Desktop**.
2. Go to **Transform Data (Power Query Editor)**.
3. Paste the following API query in **Advanced Editor**:
   
```m
let
    url = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/9237",
    response = Web.Contents(
        url, 
        [
            Headers = [
                #"x-rapidapi-key" = "YOUR_RAPIDAPI_KEY",
                #"x-rapidapi-host" = "cricbuzz-cricket.p.rapidapi.com"
            ]
        ]
    ),
    jsonData = Json.Document(response),
    matches = try jsonData[matches] otherwise null,
    matchesTable = if matches <> null then Table.FromList(matches, Splitter.SplitByNothing(), null, null, ExtraValues.Error) else null
in
    matchesTable
```
4. Replace `YOUR_RAPIDAPI_KEY` with your **actual API key**.
5. Click **Done > Close & Apply**.

### Set Up Automatic Refresh
If using Power BI Service:
- **Publish** the report.
- Go to **Dataset Settings > Schedule Refresh**.
- Enable **refresh** and set the update frequency.

### Install Dependencies for Website Development
Run the following command to install required Python libraries:
```sh
pip install streamlit pandas numpy plotly-express
```

## Dashboard & Website Development
### Power BI Dashboard
For the dashboard, we used the **Cricbuzz API** from the free plan on **RapidAPI.com**. We built a connection between **Power BI** and the server using an API key, which allowed us to fetch live data from the Cricbuzz website.

#### Steps We Followed:
1. **Connected Power BI with the Cricbuzz API** using the API key.
2. **Extracted match data** and stored it in a CSV file.
3. **Cleaned the data**, removed inconsistencies, and renamed columns for better readability.
4. **Fetched live scorecards** but initially faced issues projecting them visually on the dashboard.
5. **Troubleshot live data visualization**—we successfully retrieved live data in an Excel sheet but struggled to display it dynamically in Power BI.
6. **Final Dashboard Output:**
   - Displayed **IPL 2024 match data** with a scoreboard.
   - Included the **points table of IPL 2024** with detailed stats of each player.
   - Showed **individual player performance per innings**.

### Website Features
We also developed a **website** that complements the Power BI dashboard by offering additional insights:
- **Player Stats & Performance History**: Compares players against each other based on past data.
- **AI-Generated Strategy Tips**: Analyzes strengths and weaknesses of players to suggest tactics.
- **Match Analysis Dashboard**: Displays match details, scores, and player stats similar to Power BI.
- **Video Analysis Support**: Highlights key moments for selected players.

### Video Retrieval Process
1. **Extracted raw match data** from **Cricsheet**.
2. **Analyzed player events** (e.g., sixes, dismissals) using **Excel**.
3. **Cleaned and processed the data** using **Streamlit** in Python.
4. **Manually searched for videos** and clipped key highlights.
5. **Named files based on event keywords** for easy retrieval.
6. **Mapped video clips to data insights** for efficient analysis.

### Challenges Faced:
- We couldn't **publish the URL** or embed the Power BI dashboard directly.
- As a workaround, we added **screenshots of the dashboard**.
- The website currently fetches **highlight videos**, but we aim to optimize this and develop a tool that can **generate AI-driven match analysis videos** in the future.

## Revenue Model
While IPL teams have access to extensive data analytics and professional data scientists, this level of analysis is not readily available for **local tournaments and cricket academies** that train young talent. Our platform is designed specifically to **bridge this gap**, offering accessible, in-depth analysis for grassroots cricket.

### Monetization Strategies:
1. **Freemium Model**: Basic data analysis and player stats are available for free. For **detailed insights and real-time scorecard dashboards**, users can subscribe to **premium plans**.
2. **B2B Model**: We offer **custom graphics dashboards** for organizations, cricket clubs, and tournament management.
3. **Brand Advertising**: We plan to partner with **cricket-related brands** for targeted advertising on our platform.
4. **Click-Based Revenue Model**: Generating revenue based on **clicks per minute** through ad engagement and user interactions.

## Usage
1. **Run Power BI Dashboard**:
   - Open Power BI Desktop.
   - Load the dataset.
   - Use filters and visualizations to analyze match statistics.
   - Enable data refresh for real-time updates.

2. **Use Website for Analysis**:
   - Run the Streamlit app using:
     ```sh
     streamlit run app.py
     ```
   - Enter player names to compare their past performances.
   - Use AI-generated strategies to plan matches.
   - View highlight videos for key moments in matches.

## Contribution
Feel free to contribute by submitting **issues, feature requests, or pull requests**. 

## License
This project is licensed under the **MIT License**.

## Contact
For any queries, reach out via:
- Karan: karannn1210@gmail.com
- Yuvraj: yuvraj1729.0@gmail.com
- Suhani: suhani190505@gmail.com
- Bhuwan: bhuwanchhabra754@gmail.com

