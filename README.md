# 📊 US Suicide Rate Forecasting | Streamlit Dashboard

Welcome to the **US Suicide Rate Forecasting Dashboard** — a data-driven project aimed at understanding suicide trends across age, sex, race, and ethnicity in the United States from 1950 to 2018, with predictive modeling into the near future.

---

## 🎯 Project Objective

This project was created to:
- Analyze suicide trends across multiple demographic dimensions
- Forecast future suicide rates using statistical and machine learning models
- Raise awareness about mental health through empathetic storytelling with data

---

## 📁 Dataset Description

**Source:** CDC (Centers for Disease Control and Prevention) via Kaggle  
**Kaggle Link:** (https://www.kaggle.com/datasets/kaitlyngaynor/suicide-death-rate-in-us)

**Fields included:**
- Year
- Age group
- Sex
- Race and Hispanic origin
- Suicide death rate per 100,000 population

---

## 🔍 Key Questions Addressed

### 1. How have suicide rates changed across different demographics from 1950 to 2018?
- National suicide rates declined mid-century but began rising again in the 1990s.
- Men have consistently higher rates than women.
- The elderly (75+) had the highest rates historically, but youth and young adults are rising fast.
- White individuals consistently show the highest suicide rates.

### 2. Which groups are most at risk?
- Males, especially White non-Hispanic males aged 25–54.
- Youth (15–24) and young adults (25–34) are showing rapid increases in recent years.
- American Indian/Alaska Native populations are also disproportionately affected.

### 3. What might the future look like if current trends continue?
- Suicide rates are forecasted to rise for specific demographics, especially among younger adults.
- Persistent disparities by race and gender are likely to continue without intervention.
- These projections highlight the urgency of targeted mental health policies and education.

---

## 📌 Tools & Technologies

- **Python** – for data wrangling and transformation
- **Prophet** – for time-series forecasting
- **Streamlit** – to build the interactive dashboard
- **Plotly** – for dynamic, responsive visualizations

---

## 📊 Dashboard Features

- **Interactive Filters** – by age, race, and sex
- **Forecast Visuals** – powered by Prophet to predict future trends
- **Yearly Trends Table** – showing average suicide rates over time
- **Line and Bar Charts** – clear visuals of variations and changes
- **Responsive UI** – optimized layout for desktop and mobile

---

## 💡 Methodology

- **Data Cleaning** – removed missing values, ensured consistent date formatting
- **Feature Engineering** – created forecast-ready time-series groupings
- **Modeling** – used Prophet to fit and forecast grouped suicide rates
- **Visualization** – designed engaging charts using Plotly and Streamlit widgets

---

## 📈 How to Use the Dashboard

1. Clone or download the GitHub repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the dashboard with:  
   ```bash
   streamlit run app.py
   ```
4. Use the filters to explore trends across demographic groups.

---

## 📌 Insights Summary

- Suicide rates have increased sharply for younger adults since 2000.
- Gender remains a strong factor — males are consistently at higher risk.
- White and Native American populations exhibit higher suicide rates compared to others.
- Forecasting shows a continuing upward trend in several vulnerable groups.

---

## 🙏 Acknowledgments

- CDC for making public health data available
- Kaggle contributors for dataset organization
- Prophet by Meta for accurate and scalable time-series forecasting
- Streamlit and Plotly for simplifying data storytelling

---

## 📎 Related Hashtags

#MentalHealthAwareness #SuicidePrevention #DataScience #Streamlit #Prophet #Forecasting #StorytellingWithData #DataWithPurpose #PublicHealth

---

For questions or collaboration inquiries, feel free to reach out or open an issue!
