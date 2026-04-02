import streamlit as st
import pandas as pd
import plotly.express as px
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import datetime

# 1. Setup & Data Loading
st.set_page_config(page_title="Epidemic Sentinel AI", layout="wide")
st.title("🛡️ Epidemic Spread Prediction & Risk Analysis")

@st.cache_data
def load_data():
    # Primary Dataset: Johns Hopkins COVID-19 Time Series
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    df = pd.read_csv(url)
    return df

df_raw = load_data()

# 2. Sidebar Filters
countries = df_raw['Country/Region'].unique()
selected_country = st.sidebar.selectbox("Select Country", countries, index=len(countries)//2)
forecast_days = st.sidebar.slider("Forecast Days", 7, 30, 14)

# 3. Data Processing for Selected Country
country_data = df_raw[df_raw['Country/Region'] == selected_country].iloc[:, 4:].sum()
country_data.index = pd.to_datetime(country_data.index)
df_country = pd.DataFrame({'Cases': country_data})

# 4. Modeling (Predictive Model)
model = ExponentialSmoothing(df_country['Cases'], trend='add', seasonal=None).fit()
forecast = model.forecast(forecast_days)
forecast_index = pd.date_range(start=df_country.index[-1] + datetime.timedelta(days=1), periods=forecast_days)
df_forecast = pd.DataFrame({'Forecast': forecast}, index=forecast_index)

# 5. Dashboard Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Infection Trend: {selected_country}")
    fig = px.line(df_country, y='Cases', title="Historical Data vs Prediction")
    fig.add_scatter(x=df_forecast.index, y=df_forecast['Forecast'], name="AI Prediction", line=dict(dash='dash', color='red'))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric("Current Total cases", f"{int(df_country['Cases'].iloc[-1]):,}")
    predicted_increase = int(df_forecast['Forecast'].iloc[-1] - df_country['Cases'].iloc[-1])
    st.metric("Predicted Increase (Next 2 Weeks)", f"+{predicted_increase:,}", delta_color="inverse")
    
    st.info("**Biological Insight:** Prediction based on exponential growth patterns. High acceleration indicates a potential new hotspot.")

# 6. Global Risk Map (Hotspot Detection)
st.divider()
st.subheader("🌍 Global Outbreak Risk Map")
latest_date = df_raw.columns[-1]
fig_map = px.choropleth(df_raw, 
                        locations="Country/Region", 
                        locationmode="country names",
                        color=latest_date, 
                        hover_name="Country/Region",
                        title="Infection Density Map",
                        color_continuous_scale=px.colors.sequential.YlOrRd)
st.plotly_chart(fig_map, use_container_width=True)
