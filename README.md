# 🛡️ Insurance Cross-Sell Prediction Model 🛡️

Welcome to the Insurance Cross-Sell Prediction project! This repository contains a machine learning model designed to predict whether a customer who has already purchased health insurance will be interested in purchasing vehicle insurance. This project is a powerful tool for insurance companies to optimize their marketing strategies, improve customer targeting, and boost revenue through effective cross-selling.

# PROBLEM STATEMENT
Your client is an Insurance company that has provided Health Insurance to its customers now they need your help in building a model to predict whether the policyholders (customers) from past year will also be interested in Vehicle Insurance provided by the company.

An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that the customer needs to pay regularly to an insurance company for this guarantee.

For example, you may pay a premium of Rs. 5000 each year for a health insurance cover of Rs. 200,000/- so that if, God forbid, you fall ill and need to be hospitalised in that year, the insurance provider company will bear the cost of hospitalisation etc. for upto Rs. 200,000. Now if you are wondering how can company bear such high hospitalisation cost when it charges a premium of only Rs. 5000/-, that is where the concept of probabilities comes in picture. For example, like you, there may be 100 customers who would be paying a premium of Rs. 5000 every year, but only a few of them (say 2-3) would get hospitalised that year and not everyone. This way everyone shares the risk of everyone else.

Just like medical insurance, there is vehicle insurance where every year customer needs to pay a premium of certain amount to insurance provider company so that in case of unfortunate accident by the vehicle, the insurance provider company will provide a compensation (called ‘sum assured’) to the customer.

Building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue. 

Now, in order to predict, whether the customer would be interested in Vehicle insurance, you have information about demographics (gender, age, region code type), Vehicles (Vehicle Age, Damage), Policy (Premium, sourcing channel) etc.

## 🌟 WHY THIS PROJECT?

Cross-selling is a critical strategy for insurance companies to maximize customer lifetime value. However, not all customers are interested in additional products. This project helps:

Identify High-Potential Customers: Predict which customers are most likely to purchase vehicle insurance.

Optimize Marketing Efforts: Focus resources on customers with the highest likelihood of conversion.

Increase Revenue: Drive sales by targeting the right audience with personalized offers.

By leveraging machine learning, this project provides actionable insights to transform your cross-selling strategy.

## 📊 DATASET

"The dataset contains information about customers, including demographics, vehicle details, and whether they have purchased vehicle insurance. Key features include:

Age: Age of the customer.
Gender: Gender of the customer.
Previously_Insured: Whether the customer already has vehicle insurance.
Vehicle_Age: Age of the vehicle.
Annual_Premium: Annual premium amount.
Response: Target variable (1 = customer is interested, 0 = customer is not interested)."

source of dataset(https://www.analyticsvidhya.com/datahack/contest/janatahack-cross-sell-prediction/)

# 🛠️ APPROCH
Here’s how we tackled the problem:

# Data Preprocessing:

Handled missing values and outliers.

Encoded categorical variables (e.g., gender, vehicle age).

Scaled numerical features for better model performance.

Exploratory Data Analysis (EDA):

Analyzed customer demographics and their impact on cross-selling.

Visualized relationships between features and the target variable.

Identified key trends (e.g., younger customers are more likely to respond).

# Feature Engineering:

Created new features (e.g., customer segment based on age and premium).

Selected the most relevant features using correlation analysis and feature importance.

# Model Selection:

Tested multiple machine learning algorithms, including:

Logistic Regression

Random Forest

Gradient Boosting (XGBoost, LightGBM)

Evaluated models using metrics like Accuracy, Precision, Recall, F1-Score, and ROC-AUC.

# Model Deployment:

Fast API : using Fast API creating a user interface for prediction.

# TECHNOLOGIES USED

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Imblearn, random forest, decission tree etc...

Tools: Jupyter Notebook, Git, GitHub, vscode

# 📈 RESULT

"The XGBoost model achieved the best performance with an ROC-AUC score of 0.80. Key insights from the model include:

Customers with older vehicles are more likely to purchase vehicle insurance.

Customers who have not previously purchased insurance are more likely to respond positively to cross-selling offers."

## 🌱 FUTURE WORKS:

We welcome contributions from the community! If you’d like to contribute:

1. Fork the repository.

2. Create a new branch for your feature/bugfix.

3. Submit a pull request with a detailed description of your changes.

# 📧 CONTACT ME:

1) Email:   rajanarendra.ponnada@gmail.com

2) LinkedIn: SRINIVASA RAJA NARENDRA PONNADA

3) GitHub: rajanarendra24


                                                                 





