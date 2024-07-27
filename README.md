# Solar Irradiance Forecasting System

This project forecasts solar irradiance using various machine-learning models. Our research develops a CNN-LSTM with Bayesian optimization using an attention mechanism
for day-ahead hourly solar irradiance forecasting. This model integrates various meteorological attributes and spatial relationships to enhance accuracy, leveraging spatial and
temporal data to provide reliable forecasts.


## Data
For this project, solar irradiance data was collected from NASA's POWER PROJECT, specifically tailored to the geographical location of Jalandhar, Punjab, India. 
The dataset encompasses historical solar irradiance measurements spanning several years, providing a rich source of information for model development and
evaluation. Additionally, meteorological data such as temperature, humidity, wind speed, and atmospheric pressure were obtained to incorporate environmental factors
influencing solar irradiance variability in the region
This includes the following features:
- Temperature
- Pressure
- Relative Humidity
- Solar Zenith Angle
- Wind Speed
- Wind Direction
- Dew Point
- Precipitable Water
- Clearness Index

The target variable is Global Horizontal Irradiance (GHI).


## Target Location

The target location for this project is NIT Jalandhar, Punjab, with the following coordinates:
- Latitude: 31.3966
- Longitude: 75.54

## Models

The following models are implemented:
- Linear Regression
- Attention Model
- CNN Model
- CNN with Cross-Validation
- LSTM-based RNN


## Hexagon Grid System

We propose using a hexagonal grid system to capture the spatial variability of solar irradiance effectively. Hexagons provide more uniform coverage and reduce spatial
distortions compared to traditional square grids. Each hexagon represents a distinct spatial unit where data is collected and analyzed, ensuring better spatial feature
extraction. This approach enables more accurate and reliable forecasts by more effectively capturing the intricate spatial patterns of solar irradiance.


##  Conclusions and Future Scope
- Advances in forecasting accuracy can yield economic benefits, such as reduced operational costs for energy providers and increased investment in
solar energy projects.
- Enhanced solar energy utilization promotes environmental sustainability by decreasing reliance on fossil fuels and lowering greenhouse gas.

## Installation

To install the dependencies, run:
```sh
pip install -r requirements.txt


