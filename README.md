# Delivery Time Prediction

## Overview

The **Delivery Time Prediction** project aims to predict delivery times for various logistics operations using machine learning techniques. This project leverages historical delivery data and various influencing factors such as distance, traffic conditions, weather, and more to provide accurate delivery time estimates. The goal is to optimize delivery processes, improve customer satisfaction, and reduce delays.

## Project Structure

- `data/`: Contains the datasets used for training and testing the models.
- `notebooks/`: Jupyter notebooks showcasing exploratory data analysis (EDA), feature engineering, and model experimentation.
- `src/`: Source code for data preprocessing, model training, and evaluation.
- `models/`: Serialized models for quick inference and deployment.
- `requirements.txt`: List of dependencies required to run the project.
- `README.md`: Project documentation and setup instructions.

## Key Features

- **Data Preprocessing**: Includes handling missing values, outliers, and data transformations.
- **Feature Engineering**: Constructs meaningful features like traffic density, delivery distance, time of day, and weather conditions.
- **Machine Learning Models**: Uses algorithms like Random Forest, Gradient Boosting, and XGBoost to predict delivery times.
- **Model Evaluation**: Utilizes performance metrics such as MAE, RMSE, and R² for model evaluation.
- **Deployment Ready**: The project is structured to allow easy deployment with the serialized models.

## Requirements

The project requires Python 3.9 or higher and the following dependencies, which are listed in the `requirements.txt` file:

- `numpy`
- `pandas`
- `scikit-learn`
- `xgboost`
- `matplotlib`
- `seaborn`

## Setup Instructions

### 1. Create new Virtual Environment
It is recommended to `create a new virtual environment` to avoid any conflicts with other projects:

```bash
conda create -p env python=3.9 -y
```

### 2. Activate virtual Environment
Activate the `virtual environment` you just created:

```bash
conda activate env/
```

### 3. Install requirements file
Install all the necessary libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Run the Project
You can explore the code and experiment with the data by running the Jupyter notebooks located in the notebooks/ folder. Additionally, you can execute the main project script for model training and evaluation.

```bash
jupyter notebook notebooks/EDA_and_Model_Training.ipynb

```

## Usage
After setting up the environment and installing the required dependencies, you can use the following steps to train and evaluate the model:

- **Data Preparation:** Preprocess the raw data by cleaning, transforming, and generating features.

- **Model Training:** Run the training scripts to generate models and evaluate their performance.

- **Inference:** Use the pre-trained models available in the models/ directory for delivery time predictions.

