# -Used-Bike-Price-Predictor-Python-Pandas-Scikit-learn
A machine learning project that predicts the resale value of used bikes using a RandomForestRegressor model and deploys it as an interactive web app with Streamlit.
📖 About This Project
This project takes a dataset of used bike listings and builds a machine learning model to estimate a bike's resale price. The goal is to create a simple, user-friendly web app where a user can input a bike's features and get an instant price prediction.

The model's preprocessing pipeline involves:

One-Hot Encoding for categorical features (like brand, city, etc.).

Standard Scaling for numerical features (like kms driven, age, etc.).

🛠️ Tech Stack
Python

Scikit-learn: For the RandomForestRegressor, OneHotEncoder, and StandardScaler.

Pandas: For data loading and manipulation.

Streamlit: For creating the interactive web application.

Joblib: For saving and loading the trained model and preprocessors.

📂 File Structure
.
├── 📄 app.py                  # The main Streamlit application

├── 📄 train_model.py          # Script to train and save the models

├── 📄 bike_price_model.pkl    # Saved Random Forest model

├── 📄 encoder.pkl             # Saved OneHotEncoder

├── 📄 scaler.pkl              # Saved StandardScaler

├── 📄 your_data.csv           # (Add your dataset here)

├── 📄 requirements.txt        # List of Python dependencies

└── 📄 README.md               # You are here

🚀 How to Run
Follow these steps to get the project running on your local machine.

1. Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a virtual environment (Recommended):

Bash

python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

3. Install the required libraries:

First, create a file named requirements.txt and paste this inside:

pandas
scikit-learn
streamlit
joblib
numpy
Then, install from the file:

Bash

pip install -r requirements.txt

4. Run the Streamlit App:

Bash

streamlit run app.py

5. Open your browser! Your browser should automatically open to the app (usually at http://localhost:8501).
