# Optimization of service predictability and customer satisfaction of Taxi company in Chicago

## Overview
This project is a comprehensive Data Analysis and Business Intelligence initiative focused on understanding the variability of taxi trip durations on a critical high-demand route in Chicago: The Loop (Downtown) to O'Hare International Airport (ORD), specifically on Saturdays. The core objective was to statistically validate the influence of external factors—namely, rainy weather—on travel time, providing actionable insights for transportation companies to optimize service predictability and customer satisfaction.

## Project Goal & Hypothesis
- Goal:
To determine if there is a statistically significant change in the average trip duration from the Loop to O'Hare when comparing Saturdays with good weather versus Saturdays with rain.

- Hypotheses:
  - Null Hypothesis ($\text{H}_0$): The mean trip duration is the same on rainy Saturdays and good-weather Saturdays.
  - Alternative Hypothesis ($\text{H}_A$): The mean trip duration is significantly different on rainy Saturdays and good-weather Saturdays.

## Methodology & Data Processing
The analysis followed a two-step approach:
- Data Extraction (SQL):
  - Used advanced SQL queries to filter the trips table for all Saturday trips originating in the Loop (pickup_location_id: 50) and ending at O'Hare (dropoff_location_id: 63).
  - Joined the data with the weather_records table to categorize each trip's start time as either 'Good' (no rain/storm) or 'Bad' (rain/storm).
  - See SQL code examples for trip filtering and weather categorization.
- Statistical Validation (Python):
  - The extracted data was loaded into a Jupyter Notebook (notebook_sprint_8.ipynb).
  - Welch's t-test for two independent samples was performed on the duration_seconds for the 'Bad' weather group and the 'Good' weather group.
  - Justification: Welch's t-test was chosen over the standard t-test because it does not assume equal variances between the two samples, making it more robust for real-world travel data.
  - A significance level ($\alpha$) of $0.05$ was used.

## Key Findings & Actionable Insights
- Finding
  1. Statistical Significance: The Null Hypothesis ($\text{H}_0$) was rejected ($p \text{-value} \ll 0.05$).
  2. Duration Difference: Trips on rainy Saturdays showed a higher mean duration compared to trips on good-weather Saturdays.
  3. Passenger Preferences: Since this is an airport route, passenger preference centers around predictability and reliability to meet flight schedules.
- Insight
  1. Rain is a critical external factor that reliably increases travel time on this route.
  2. The service provider can quantify this difference (e.g., $+15\% \text{ travel time}$) to proactively adjust ETAs.
  3. Unpredictability due to weather is a service failure point that must be managed.

## Recommendations
Based on the data-driven evidence, the following recommendations are proposed:
- Dynamic ETA Adjustments: Automatically increase the Estimated Time of Arrival (ETA) for Loop-to-O'Hare trips by a predefined factor (e.g., the calculated difference in means) whenever rain is forecasted for a Saturday.
- Proactive Communication: Implement a system to notify passengers about the expected delay due to weather, managing their expectations and improving perceived reliability.
- Resource Allocation: Optimize fleet dispatching to ensure a higher supply of available vehicles in the Loop area on rainy Saturdays to account for longer trip cycle times.

## Technologies Used
- SQL: Data Extraction, Filtering, and Conditional Logic (CASE statements, JOINs, EXTRACT(DOW)).
- Python: Data manipulation (Pandas), Statistical Testing (SciPy.stats), Data Visualization (Matplotlib, Seaborn).
- Environment: Jupyter Notebooks.Version Control: Git, GitHub.

## Files in this Repository
- extraction.txt: contains the code for table extraction from URL.
- taxi_analysis.ipynb: The main analysis file containing all the Python code for data loading, descriptive statistics, the execution of the Welch's t-test, visualizations, and final conclusions.
- sql_queries.txt: Contains the exact SQL script used for the data extraction phase.
