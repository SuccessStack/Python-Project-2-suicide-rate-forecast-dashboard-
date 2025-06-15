# app.py
import streamlit as st
import pandas as pd
import joblib
from PIL import Image
from prophet.plot import plot_plotly
import plotly.express as px

# Page config
st.set_page_config(page_title="US Suicide Rate Forecast", layout="wide")

# Display the banner image at the top
banner_image = Image.open("suicide_banner.png")  # 👈 Make sure this filename matches your image
st.image(banner_image, use_column_width=True)

# Theme toggle
mode = st.sidebar.radio("🌗 Theme Mode", ["Light", "Dark"])
bg_color = "#f4f6f9" if mode == "Light" else "#636060"
text_color = "#0a2f5c" if mode == "Light" else "#ffffff"

# Background styling
st.markdown(f"""
    <style>
    .main {{
        background-color: {bg_color};
        color: {text_color};
    }}
    h1, h2, h3, h4, h5, h6, p {{
        color: {text_color};
    }}
    .stDataFrame {{
        background-color: white;
        border-radius: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 US Suicide Rate Forecast Dashboard")
st.markdown("#### *Forecasting and Exploring Suicide Death Rates in the US*")

# Tabs
tab1, tab2, tab3 = st.tabs(["🔮 Forecast", "📊 Trends", "📋 Demographics"])

# --------- Load Model and Forecast ---------
model = joblib.load("suicide_forecast_model.pkl")
future = model.make_future_dataframe(periods=5, freq="Y")
forecast = model.predict(future)

# --------- Load and Clean Data ---------
df = pd.read_csv("Death_rates_for_suicide_by_sex_race_Hispanic_origin_and_age_United.csv")
df["YEAR"] = pd.to_datetime(df["YEAR"].astype(str), format="%Y", errors="coerce")
df.dropna(subset=["YEAR", "ESTIMATE"], inplace=True)

# ========================= TAB 1: Forecast =========================
with tab1:
    st.markdown("### 📈 Prophet Model Forecast (Next 5 Years)")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("📋 Forecast Table")
        st.dataframe(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail().rename(columns={
            "ds": "Year",
            "yhat": "Forecast",
            "yhat_lower": "Lower Bound",
            "yhat_upper": "Upper Bound"
        }))

    with col2:
        st.subheader("📉 Forecast Chart")
        st.plotly_chart(plot_plotly(model, forecast), use_container_width=True)

# ========================= TAB 2: Trends =========================
with tab2:
    st.markdown("### 📉 Filtered Suicide Rate Trends by Demographic")

    # 🎛️ Filters inside the tab
    col_filter1, col_filter2 = st.columns(2)
    with col_filter1:
        age_options = df["AGE"].dropna().unique()
        age_filter = st.selectbox("👤 Select Age Group", sorted(age_options), index=0)

    with col_filter2:
        race_options = df["STUB_LABEL"].dropna().unique()
        race_filter = st.selectbox("🌍 Select Demographic Group", sorted(race_options), index=0)

    # 📊 Filter and prepare data
    filtered_trend_df = df[(df["AGE"] == age_filter) & (df["STUB_LABEL"] == race_filter)]

    if filtered_trend_df.empty:
        st.warning("⚠️ No data available for this combination.")
    else:
        trend_data = (
            filtered_trend_df.groupby(filtered_trend_df["YEAR"].dt.year)["ESTIMATE"]
            .mean()
            .reset_index()
        )
        trend_data.columns = ["Year", "Average Suicide Rate"]
        trend_data["Year"] = trend_data["Year"].astype(str)  # 👈 Fix formatting here

        col_chart, col_table = st.columns(2)

        with col_table:
            st.markdown("#### 📅 Yearly Data Table")
            st.dataframe(trend_data)

        with col_chart:
            fig = px.line(
                trend_data,
                x="Year",
                y="Average Suicide Rate",
                markers=True,
                line_shape="spline",
                color_discrete_sequence=["#00BFFF"]
            )
            fig.update_layout(
                title=f"{age_filter} | {race_filter} Trend Over Time",
                height=400,
                plot_bgcolor=bg_color,
                paper_bgcolor=bg_color,
                font_color=text_color
            )
            st.plotly_chart(fig, use_container_width=True)

# ========================= TAB 3: Demographics =========================
with tab3:
    st.markdown("### 🧮 Suicide Rates by Demographic Group")

    years = sorted(df["YEAR"].dt.year.dropna().unique())
    default_index = len(years) - 1
    selected_year = st.selectbox("📅 Select Year", years, index=default_index)

    demo_type = st.radio("🔍 Choose Demographic Group", ["STUB_LABEL", "AGE"], horizontal=True)
    filtered_df = df[df["YEAR"].dt.year == selected_year]
    demo_grouped = filtered_df.groupby(demo_type)["ESTIMATE"].mean().reset_index()
    demo_grouped.columns = [demo_type, "Average Suicide Rate"]

    fig_bar = px.bar(
        demo_grouped,
        x="Average Suicide Rate",
        y=demo_type,
        orientation="h",
        color="Average Suicide Rate",
        color_continuous_scale="bluered_r",
        title=f"Suicide Rates by {demo_type.replace('_', ' ').title()} ({selected_year})"
    )
    fig_bar.update_layout(height=500)
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("📥 Download this demographic data:")
    st.download_button("⬇️ Download CSV", data=demo_grouped.to_csv(index=False), file_name="demographic_rates.csv", mime="text/csv")

# ========================= Footer =========================
st.markdown("---")
st.markdown("✅ **Data Source:** US Government Public Health Database")
st.markdown("👨‍💻 Built with ❤️ by **Success Azubogu**") 
