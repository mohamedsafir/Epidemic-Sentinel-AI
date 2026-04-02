
# 🛡️ Epidemic Sentinel AI: Global Spread Predictor

### **Track C: Epidemic Spread Prediction (Epidemiology + AI)**
An AI-driven forecasting engine and interactive dashboard designed to predict infectious disease outbreaks using the Johns Hopkins COVID-19 Time Series dataset.

---

## 📖 Project Overview
**Epidemic Sentinel AI** is a prototype developed to assist public health preparedness. By integrating historical outbreak data with time-series forecasting, the system identifies high-risk **"Hotspots"** and predicts case growth trends over a 14-day window.

The goal is to move beyond simple data visualization and provide **biologically meaningful insights** by analyzing the acceleration of transmission rates across different geographic regions.

---

## 🛠️ Tech Stack & Tools

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **UI Framework** | Streamlit (Interactive Dashboard) |
| **Data Engine** | Pandas, NumPy (Data Wrangling & Normalization) |
| **AI/Forecasting** | Statsmodels (Holt-Winters Exponential Smoothing) |
| **Visualization** | Plotly Express (Geospatial Risk Maps & Time-Series Charts) |
| **Data Source** | Johns Hopkins University (CSSE) GitHub Repository |

---

## ⚙️ Installation & Setup
Follow these steps to run the prototype locally:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/Epidemic-Sentinel-AI.git](https://github.com/YOUR_GITHUB_USERNAME/Epidemic-Sentinel-AI.git)
   cd Epidemic-Sentinel-AI
   ```
**Create a Virtual Environment (Recommended):**
``` Bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
**Install Dependencies:**
```Bash
pip install -r requirements.txt
```
**Launch the Dashboard:**
```Bash
streamlit run app.py
```

---

**### ✨ Key Features :**

**Live Data Ingestion:** Automates fetching of the most recent daily confirmed cases from the JHU global repository.

**Predictive Modeling:** Implements a Univariate Time-Series model (ETS) to forecast future infection spikes.

**Interactive Global Risk Map:** A Choropleth visualization that dynamically identifies hotspots based on current infection density.

**Regional Deep-Dive:** Allows users to select specific countries/regions to analyze localized growth patterns and cumulative trends.

**Biological Insights:** A logic-based module that interprets statistical "Case Acceleration" as a high-risk outbreak signal.

---

**### 🧬 Technical Workflow**
The system architecture follows a clean, three-tier pipeline:

**1) Data Layer:**

Fetches raw CSV data from the JHU CSSE GitHub.

Preprocesses "Wide Format" data into "Long Format" time-series.

Aggregates data by ```Country/Region``` and handles missing values via linear interpolation.

**2) Analysis Layer (The AI Engine):**

Uses Exponential Smoothing (ETS) to capture both trend and seasonality in the spread.

Calculates the Rate of Change to identify if an outbreak is accelerating (Potential Hotspot) or decelerating (Flattening the curve).

**3) View Layer (Streamlit UI):**

Renders a responsive sidebar for user control.

Outputs interactive Plotly charts with hover-tooltips for precise data reading.

---

**### 🚀 Scalability & Future Scope**
To evolve this prototype into a production-grade SaaS product:

**Mobility Integration:** Incorporate Google Mobility Reports to adjust transmission factors based on population movement.

**Vaccination Impact:** Layer in "Our World in Data" vaccination statistics to model the deceleration of spread in immunized regions.

**Deep Learning:** Upgrade the forecasting engine to an LSTM (Long Short-Term Memory) network for complex multi-variate analysis.

---

**### 👨‍💻 Developed By**
**Mohamed SAFIR N.**
Master of Computer Applications (MCA)

