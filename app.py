import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="Healthcare Data Analytics",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# CUSTOM CSS
# -------------------------------

st.markdown("""
<style>

.main{
    background-color:#F4F8FF;
}

h1,h2,h3{
    color:#0A58CA;
}

div[data-testid="stSidebar"]{
    background-color:#EAF4FF;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 12px rgba(0,0,0,0.15);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD DATASET
# -------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("insurance.csv")
    return df

df = load_data()

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("🏥 Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "🏠 Home",
        "📊 Dashboard",
        "📈 Visualizations",
        "🤖 Machine Learning",
        "💡 Insights",
        "👩‍💻 About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("Healthcare Analytics Project")

st.sidebar.write("Developer: Aswitha")

# -------------------------------
# HOME PAGE
# -------------------------------

if page=="🏠 Home":

    st.title("🏥 Healthcare Data Analytics Dashboard")

    st.markdown("""
### Medical Insurance Cost Prediction System

This dashboard analyzes healthcare insurance data using:

- 🐍 Python
- 📊 Pandas
- 📈 Plotly
- 🌐 Streamlit
- 🤖 Machine Learning

The project helps healthcare organizations understand
medical insurance costs using interactive analytics.
""")

    st.image(
        "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1200",
        use_container_width=True
    )

    st.write("---")

    st.subheader("🚀 Project Objectives")

    col1,col2,col3=st.columns(3)

    with col1:
        st.info("""
### 📊 Data Analytics

✔ Data Cleaning

✔ Data Visualization

✔ KPI Analysis

✔ Business Insights
""")

    with col2:
        st.info("""
### 📈 Dashboard

✔ Interactive Charts

✔ Filters

✔ Heatmaps

✔ Download Data
""")

    with col3:
        st.info("""
### 🤖 Machine Learning

✔ Cost Prediction

✔ Model Training

✔ User Prediction

✔ Decision Support
""")

    st.write("---")

    st.subheader("📊 Dataset Information")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Rows",len(df))
    c2.metric("Columns",len(df.columns))
    c3.metric("Average Age",round(df.age.mean(),1))
    c4.metric("Average BMI",round(df.bmi.mean(),1))

    st.write("---")

    st.success("👇 Select any page from the sidebar to explore the project.")
    # ===================================================
# DASHBOARD PAGE
# ===================================================

elif page == "📊 Dashboard":

    st.title("📊 Dashboard Overview")

    total_patients = len(df)
    avg_age = df["age"].mean()
    avg_bmi = df["bmi"].mean()
    avg_charges = df["charges"].mean()
    smokers = len(df[df["smoker"] == "yes"])
    females = len(df[df["sex"] == "female"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Total Patients", total_patients)

    with col2:
        st.metric("💰 Average Charges", f"${avg_charges:,.2f}")

    with col3:
        st.metric("📈 Average BMI", round(avg_bmi, 2))

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("🎂 Average Age", round(avg_age, 1))

    with col5:
        st.metric("🚬 Smokers", smokers)

    with col6:
        st.metric("👩 Female Patients", females)

    st.write("---")

    st.subheader("📋 Dataset Preview")

    st.dataframe(df.head(15), use_container_width=True)

    st.write("---")

    st.subheader("📊 Dataset Summary")

    st.dataframe(df.describe(), use_container_width=True)

    st.write("---")

    st.subheader("📌 Dataset Information")

    info1, info2 = st.columns(2)

    with info1:
        st.info(f"""
Dataset Shape

Rows : {df.shape[0]}

Columns : {df.shape[1]}
""")

    with info2:
        st.success(f"""
Missing Values

{df.isnull().sum().sum()}

Duplicate Rows

{df.duplicated().sum()}
""")

    st.write("---")

    st.subheader("📖 Column Description")

    st.markdown("""
| Column | Description |
|---------|-------------|
| age | Age of patient |
| sex | Gender |
| bmi | Body Mass Index |
| children | Number of Children |
| smoker | Smoking Status |
| region | Residential Region |
| charges | Medical Insurance Charges |
""")
    import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("insurance.csv")

df = load_data()

# -----------------------------
# TITLE
# -----------------------------
st.title("📈 Healthcare Data Visualizations")

st.write("Explore the Healthcare Insurance Dataset using interactive charts.")

st.markdown("---")

# -----------------------------
# FILTERS
# -----------------------------
st.sidebar.header("🎛️ Filters")

gender = st.sidebar.multiselect(
    "Gender",
    df["sex"].unique(),
    default=df["sex"].unique()
)

smoker = st.sidebar.multiselect(
    "Smoking Status",
    df["smoker"].unique(),
    default=df["smoker"].unique()
)

region = st.sidebar.multiselect(
    "Region",
    df["region"].unique(),
    default=df["region"].unique()
)

filtered_df = df[
    (df["sex"].isin(gender)) &
    (df["smoker"].isin(smoker)) &
    (df["region"].isin(region))
]

# -----------------------------
# ROW 1
# -----------------------------
col1,col2=st.columns(2)

with col1:

    fig=px.histogram(
        filtered_df,
        x="age",
        color="sex",
        title="Age Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

with col2:

    fig=px.histogram(
        filtered_df,
        x="bmi",
        color="sex",
        title="BMI Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# ROW 2
# -----------------------------
col3,col4=st.columns(2)

with col3:

    fig=px.histogram(
        filtered_df,
        x="charges",
        title="Insurance Charges Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

with col4:

    fig=px.scatter(
        filtered_df,
        x="age",
        y="charges",
        color="smoker",
        size="bmi",
        title="Age vs Charges"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# ROW 3
# -----------------------------
col5,col6=st.columns(2)

with col5:

    fig=px.scatter(
        filtered_df,
        x="bmi",
        y="charges",
        color="smoker",
        title="BMI vs Charges"
    )

    st.plotly_chart(fig,use_container_width=True)

with col6:

    fig=px.box(
        filtered_df,
        x="smoker",
        y="charges",
        color="smoker",
        title="Charges by Smoking Status"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# ROW 4
# -----------------------------
col7,col8=st.columns(2)

with col7:

    fig=px.box(
        filtered_df,
        x="region",
        y="charges",
        color="region",
        title="Charges by Region"
    )

    st.plotly_chart(fig,use_container_width=True)

with col8:

    fig=px.box(
        filtered_df,
        x="sex",
        y="charges",
        color="sex",
        title="Charges by Gender"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# ROW 5
# -----------------------------
col9,col10=st.columns(2)

with col9:

    fig=px.pie(
        filtered_df,
        names="sex",
        hole=0.5,
        title="Gender Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

with col10:

    fig=px.pie(
        filtered_df,
        names="smoker",
        hole=0.5,
        title="Smoking Status"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# ROW 6
# -----------------------------
col11,col12=st.columns(2)

with col11:

    region_charge=filtered_df.groupby("region")["charges"].mean().reset_index()

    fig=px.bar(
        region_charge,
        x="region",
        y="charges",
        color="region",
        title="Average Charges by Region"
    )

    st.plotly_chart(fig,use_container_width=True)

with col12:

    child_charge=filtered_df.groupby("children")["charges"].mean().reset_index()

    fig=px.bar(
        child_charge,
        x="children",
        y="charges",
        color="children",
        title="Average Charges by Children"
    )

    st.plotly_chart(fig,use_container_width=True)

# -----------------------------
# CORRELATION HEATMAP
# -----------------------------
st.markdown("---")

st.subheader("🔥 Correlation Heatmap")

corr = filtered_df[["age","bmi","children","charges"]].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Blues",
    title="Correlation Matrix"
)

st.plotly_chart(fig,use_container_width=True)

st.success("20+ Interactive Visualizations Loaded Successfully ✅")
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

st.title("🤖 Medical Insurance Cost Prediction")

df = pd.read_csv("insurance.csv")

# Encode categorical columns
df_ml = df.copy()
df_ml["sex"] = df_ml["sex"].map({"male":1,"female":0})
df_ml["smoker"] = df_ml["smoker"].map({"yes":1,"no":0})
df_ml["region"] = df_ml["region"].map({
    "southwest":0,
    "southeast":1,
    "northwest":2,
    "northeast":3
})

X = df_ml.drop("charges",axis=1)
y = df_ml["charges"]

model = RandomForestRegressor(random_state=42)
model.fit(X,y)

st.subheader("Enter Patient Details")

age = st.slider("Age",18,64,30)

sex = st.selectbox("Gender",["Male","Female"])

bmi = st.slider("BMI",15.0,55.0,25.0)

children = st.slider("Children",0,5,0)

smoker = st.selectbox("Smoker",["No","Yes"])

region = st.selectbox(
    "Region",
    ["southwest","southeast","northwest","northeast"]
)

sex_value = 1 if sex=="Male" else 0
smoker_value = 1 if smoker=="Yes" else 0

region_value = {
    "southwest":0,
    "southeast":1,
    "northwest":2,
    "northeast":3
}[region]

input_data = pd.DataFrame({
    "age":[age],
    "sex":[sex_value],
    "bmi":[bmi],
    "children":[children],
    "smoker":[smoker_value],
    "region":[region_value]
})

if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Insurance Charge: ${prediction:,.2f}"
    )

st.markdown("---")
st.info("Machine Learning Model : Random Forest Regressor")
import streamlit as st
import pandas as pd

st.title("💡 Healthcare Insights")

df = pd.read_csv("insurance.csv")

st.subheader("Key Business Insights")

highest_region = df.groupby("region")["charges"].mean().idxmax()
highest_charge = df.groupby("region")["charges"].mean().max()

st.success(f"Highest average charges are in **{highest_region}** (${highest_charge:,.2f}).")

smoker_avg = df[df["smoker"]=="yes"]["charges"].mean()
nonsmoker_avg = df[df["smoker"]=="no"]["charges"].mean()

st.warning(f"Smokers spend about **${smoker_avg:,.2f}** on average.")

st.info(f"Non-smokers spend about **${nonsmoker_avg:,.2f}** on average.")

st.markdown("---")

st.subheader("Recommendations")

st.write("✅ Promote smoking cessation programs.")

st.write("✅ Encourage healthy BMI through wellness initiatives.")

st.write("✅ Focus preventive healthcare on high-risk groups.")

st.write("✅ Offer personalized insurance plans.")

st.write("✅ Use predictive analytics for better pricing.")

st.markdown("---")

st.subheader("Project Conclusion")

st.success("""
This project demonstrates how Healthcare Data Analytics can identify patterns in insurance costs and use Machine Learning to predict future medical expenses.
""")
import streamlit as st

st.title("👩‍💻 About This Project")

st.markdown("---")

st.header("🏥 Healthcare Data Analytics")

st.write("""
This project analyzes the Medical Insurance Dataset using Data Analytics and Machine Learning.

The dashboard provides:

✔ Patient Analysis

✔ Interactive Charts

✔ Business Insights

✔ Insurance Cost Prediction

✔ Healthcare Recommendations
""")

st.markdown("---")

st.header("🛠 Technologies Used")

st.write("""
🐍 Python

📊 Pandas

📈 Plotly

🤖 Scikit-Learn

🌐 Streamlit
""")

st.markdown("---")

st.header("🎓 Internship")

st.write("""
Organization : NIT Trichy Internship

Project : Healthcare Data Analytics

Title : Medical Insurance Cost Prediction
""")

st.markdown("---")

st.header("👩‍💻 Developed By")

st.success("""
Name : Aswitha

Department : B.Tech Computer Science & Bioscience

Role : Data Analytics Intern
""")

st.markdown("---")

st.balloons()