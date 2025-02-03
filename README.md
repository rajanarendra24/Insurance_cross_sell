# Insurance Cross-Sell Prediction Model

#  PROJECT OVERVIEW:
"This project aims to predict whether a customer who has already purchased health insurance from a company will be interested in purchasing vehicle insurance (cross-selling). The goal is to help the company target the right customers and optimize their marketing efforts."
![The-Case-for-Disability-Insurance-Cross-Selling](https://github.com/user-attachments/assets/1ba0e73e-c114-4f37-91c0-fabf89fbea76)

# PROBLEM STATEMENT
Your client is an Insurance company that has provided Health Insurance to its customers now they need your help in building a model to predict whether the policyholders (customers) from past year will also be interested in Vehicle Insurance provided by the company.

An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that the customer needs to pay regularly to an insurance company for this guarantee.

For example, you may pay a premium of Rs. 5000 each year for a health insurance cover of Rs. 200,000/- so that if, God forbid, you fall ill and need to be hospitalised in that year, the insurance provider company will bear the cost of hospitalisation etc. for upto Rs. 200,000. Now if you are wondering how can company bear such high hospitalisation cost when it charges a premium of only Rs. 5000/-, that is where the concept of probabilities comes in picture. For example, like you, there may be 100 customers who would be paying a premium of Rs. 5000 every year, but only a few of them (say 2-3) would get hospitalised that year and not everyone. This way everyone shares the risk of everyone else.

Just like medical insurance, there is vehicle insurance where every year customer needs to pay a premium of certain amount to insurance provider company so that in case of unfortunate accident by the vehicle, the insurance provider company will provide a compensation (called ‘sum assured’) to the customer.

Building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue. 

Now, in order to predict, whether the customer would be interested in Vehicle insurance, you have information about demographics (gender, age, region code type), Vehicles (Vehicle Age, Damage), Policy (Premium, sourcing channel) etc.

# DATASET
source of dataset(https://www.analyticsvidhya.com/datahack/contest/janatahack-cross-sell-prediction/)
"The dataset contains information about customers, including demographics, vehicle details, and whether they have purchased vehicle insurance. Key features include:

Age: Age of the customer.
Gender: Gender of the customer.
Previously_Insured: Whether the customer already has vehicle insurance.
Vehicle_Age: Age of the vehicle.
Annual_Premium: Annual premium amount.
Response: Target variable (1 = customer is interested, 0 = customer is not interested)."

# APPROCH
"The project involves the following steps:

Data Preprocessing: Handling missing values, encoding categorical variables, and scaling numerical features.

Exploratory Data Analysis (EDA): Analyzing the dataset to understand patterns and relationships between features.

Feature Engineering: Creating new features or transforming existing ones to improve model performance.

Model Selection: Testing various machine learning models (e.g., Logistic Regression, Random Forest, XGBoost) to predict customer interest.

Model Evaluation: Using metrics like accuracy, precision, recall, F1-score, and ROC-AUC to evaluate model performance.

Fast API : using Fast API creating a user interface for prediction.

# TECHNOLOGIES USED

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Imblearn, random forest, decission tree etc...

Tools: Jupyter Notebook, Git, GitHub, vscode

# Result

"The XGBoost model achieved the best performance with an ROC-AUC score of 0.80. Key insights from the model include:

Customers with older vehicles are more likely to purchase vehicle insurance.

Customers who have not previously purchased insurance are more likely to respond positively to cross-selling offers."

# CONTACT ME:

"For any questions or suggestions, feel free to reach out to me at [ rajanarendra.ponnada@gmail.com] 
Linked in = https://www.linkedin.com/in/srinivasa-raja-narendra-ponnada-b01760246/





