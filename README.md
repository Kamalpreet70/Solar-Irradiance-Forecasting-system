# Solar Irradiance Forecasting System

This project forecasts solar irradiance using various machine-learning models.

## Data

The data is from NIT Jalandhar and includes the following features:
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

Data files are located in the `data/` directory.

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

The model code is located in the `src/` directory.

## Hexagon Grid System

The hexagon grid system generates hexagon rings around a target location. The code is in `src/hexagon_grid_system.py`.

## Installation

To install the dependencies, run:
```sh
pip install -r requirements.txt
