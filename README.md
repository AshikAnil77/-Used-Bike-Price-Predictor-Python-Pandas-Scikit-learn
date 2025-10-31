# 🛵 Used Bike Price Predictor

> A **Machine Learning Web App** that predicts the resale value of used bikes using a **Random Forest Regressor**, deployed with **Streamlit** for an interactive experience.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ced73cb3-54ac-4108-b195-a875ee167b17" alt="Used Bike Price Predictor App Screenshot" width="80%" />
</p>

---

## 📖 About This Project

The **Used Bike Price Predictor** is designed to estimate the resale price of motorcycles based on their features like brand, age, kilometers driven, and more.  
It provides an **easy-to-use web interface** where users can input bike details and instantly get an estimated price.

### 🔍 Model Pipeline Overview
The ML workflow involves:
- 🧩 **One-Hot Encoding** for categorical variables (e.g., brand, city)
- ⚖️ **Standard Scaling** for numerical variables (e.g., kms driven, age)
- 🌲 **RandomForestRegressor** for robust non-linear regression

The model is trained, serialized with **Joblib**, and deployed using **Streamlit**.

---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|-------------|
| **Programming Language** | Python 🐍 |
| **ML Framework** | Scikit-learn |
| **Data Handling** | Pandas, NumPy |
| **Visualization / UI** | Streamlit |
| **Model Persistence** | Joblib |
| **Development** | Jupyter Notebook |

---

## 📂 Project Structure

├── 📄 app.py # Streamlit web app
├── 📄 training_notebook.ipynb # Model training & experimentation
├── 📄 your_data.csv # Dataset used for model training
├── 📄 requirements.txt # Project dependencies
├── 📄 .gitignore # Ignores environment and model files
└── 📄 README.md # You are here 🚀

---

## ⚙️ Setup & Installation

> You’ll need Python 3.8+ and Jupyter installed before proceeding.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

2️⃣ Create a Virtual Environment & Install Requirements
```bash
python -m venv myenv
source myenv/bin/activate     # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ Train the Model
```bash
Open and run all cells in training_notebook.ipynb.
```
This will generate the following model files:

bike_price_model.pkl
encoder.pkl
scaler.pkl


4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

Your browser will automatically open at
👉 http://localhost:8501

### 🧾 Future Improvements

🔮 Integrate deep learning models for advanced prediction.

🌍 Deploy to Streamlit Cloud / Hugging Face Spaces.

🧹 Add automated data cleaning and outlier detection.

📈 Include charts to visualize feature importance.


### 🌟 Acknowledgements

Streamlit
 — for easy web app deployment

Scikit-learn
 — for model development

Pandas
 — for data preprocessing

Jupyter
 — for training and experimentation
