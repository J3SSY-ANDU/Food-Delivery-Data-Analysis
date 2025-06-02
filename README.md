# 🍔 Food Delivery Data Analysis

This is a beginner-friendly data analysis project that explores food delivery data to uncover trends, detect anomalies, and gain insights about customer behavior and restaurant performance.

## 📊 Objective

The goal of this project is to practice **data cleaning**, **data manipulation**, and **data visualization** using Python. No machine learning is involved — this project focuses entirely on exploratory data analysis (EDA) and dataset preparation.

---

## 🗂️ Project Structure

```
food-delivery-data-analysis/
├── data/
│   ├── raw/             # Original dataset(s)
│   └── processed/       # Cleaned & modified version of the dataset
├── notebook.ipynb       # Main analysis notebook
├── README.md            # Project description
```

---

## 🧰 Tools & Libraries

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

---

## 🧼 Data Cleaning

- Removed duplicate order and customer IDs
- Handled missing or invalid values (e.g., "Not given" in rating column)
- Ensured numeric columns like cost, prep time, and delivery time have valid, non-negative values

---

## 🛠️ Data Manipulation

- Created custom features such as:
  - Average food preparation time by restaurant
  - Cost category (`Cheap`, `Normal`, `Expensive`) based on cuisine type using IQR
- Categorized values to enable better grouping and comparison

---

## 📈 Exploratory Data Analysis (EDA)

### 🔍 General Trends
- Count of orders by weekday vs. weekend
- Distribution of ratings
- Analysis of food preparation time and delivery time

### 📦 Outlier Detection
- Boxplots of cost, food preparation time, and delivery time
- IQR-based method to identify extreme values

### 🍽️ Cuisine & Restaurant Insights
- Cost analysis per cuisine type
- Most frequent cuisines and restaurant names
- Food prep time classified as too long or reasonable based on mean per restaurant

---

## 📌 Key Insights

- Most orders occur during the **weekend**, indicating higher customer engagement.
- Some restaurants have **unusually long food prep times** compared to their average.
- The **cost category** per cuisine helps highlight which cuisines tend to be more expensive.
- Ratings labeled "Not given" form a significant portion of the dataset and were treated accordingly.

---

## ✅ Next Steps (Future Improvements)

- Add interactive visualizations using **Plotly** or **Dash**
- Export summary reports or dashboards
- Clean further categorical inconsistencies (e.g., cuisine naming)
- Include geospatial analysis if location data becomes available

---

## 📬 Contact

Feel free to reach out if you have questions or feedback!
