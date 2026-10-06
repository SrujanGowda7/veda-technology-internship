
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------

st.set_page_config(
    page_title="Veda Technology Customer Analytics",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

df = pd.read_csv("customer_data.csv")


# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.title("📊 Veda Technology")
st.header("Customer Segmentation & Service Recommendation System")

st.write(
    "This dashboard analyzes customer behavior, engagement, "
    "spending and interests to identify customer segments "
    "and recommend suitable Veda Technology services."
)


# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------

st.sidebar.title("Dashboard Filters")

segments = st.sidebar.multiselect(
    "Select Customer Segment",
    options=sorted(df["Customer_Segment"].unique()),
    default=sorted(df["Customer_Segment"].unique())
)

filtered_df = df[
    df["Customer_Segment"].isin(segments)
]


# ------------------------------------------------------------
# KPI SECTION
# ------------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Customer Segments",
        filtered_df["Customer_Segment"].nunique()
    )

with col3:
    st.metric(
        "Avg Engagement",
        round(
            filtered_df["Engagement_Score"].mean(),
            2
        )
    )

with col4:
    st.metric(
        "Avg Monthly Spending",
        f"₹{filtered_df['Monthly_Spending'].mean():,.0f}"
    )


st.divider()


# ------------------------------------------------------------
# SEGMENT DISTRIBUTION
# ------------------------------------------------------------

st.subheader("👥 Customer Segment Distribution")

segment_counts = filtered_df[
    "Customer_Segment"
].value_counts()

fig, ax = plt.subplots(figsize=(9, 5))

segment_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Customer Segment")
ax.set_ylabel("Number of Customers")
ax.set_title("Customers by Segment")

plt.xticks(rotation=30, ha="right")

st.pyplot(fig)


# ------------------------------------------------------------
# ENGAGEMENT BY SEGMENT
# ------------------------------------------------------------

st.subheader("📈 Average Engagement by Segment")

engagement = filtered_df.groupby(
    "Customer_Segment"
)["Engagement_Score"].mean().sort_values(
    ascending=False
)

fig, ax = plt.subplots(figsize=(9, 5))

engagement.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Customer Segment")
ax.set_ylabel("Average Engagement Score")
ax.set_title("Average Engagement by Customer Segment")

plt.xticks(rotation=30, ha="right")

st.pyplot(fig)


# ------------------------------------------------------------
# SPENDING BY SEGMENT
# ------------------------------------------------------------

st.subheader("💰 Average Spending by Segment")

spending = filtered_df.groupby(
    "Customer_Segment"
)["Monthly_Spending"].mean().sort_values(
    ascending=False
)

fig, ax = plt.subplots(figsize=(9, 5))

spending.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Customer Segment")
ax.set_ylabel("Average Monthly Spending")
ax.set_title("Average Spending by Customer Segment")

plt.xticks(rotation=30, ha="right")

st.pyplot(fig)


# ------------------------------------------------------------
# RECOMMENDED SERVICES
# ------------------------------------------------------------

st.subheader("🎯 Recommended Services")

recommendations = filtered_df[
    "Recommended_Service"
].value_counts()

fig, ax = plt.subplots(figsize=(9, 5))

recommendations.plot(
    kind="barh",
    ax=ax
)

ax.set_xlabel("Number of Customers")
ax.set_ylabel("Recommended Service")

st.pyplot(fig)


# ------------------------------------------------------------
# CUSTOMER LOOKUP
# ------------------------------------------------------------

st.subheader("🔎 Customer Recommendation Lookup")

customer_id = st.selectbox(
    "Select Customer",
    df["Customer_ID"].tolist()
)

customer = df[
    df["Customer_ID"] == customer_id
].iloc[0]

col1, col2 = st.columns(2)

with col1:

    st.write("### Customer Information")

    st.write(
        "**Customer ID:**",
        customer["Customer_ID"]
    )

    st.write(
        "**Age:**",
        int(customer["Age"])
    )

    st.write(
        "**Website Visits:**",
        int(customer["Website_Visits"])
    )

    st.write(
        "**Engagement Score:**",
        int(customer["Engagement_Score"])
    )

    st.write(
        "**Monthly Spending:**",
        f"₹{customer['Monthly_Spending']:,.0f}"
    )


with col2:

    st.write("### Personalized Recommendation")

    st.success(
        f"Segment: {customer['Customer_Segment']}"
    )

    st.info(
        f"Recommended Service: "
        f"{customer['Recommended_Service']}"
    )


# ------------------------------------------------------------
# SEGMENT PROFILE
# ------------------------------------------------------------

st.subheader("📋 Customer Segment Profile")

profile = filtered_df.groupby(
    "Customer_Segment"
).agg(
    Customers=("Customer_ID", "count"),
    Avg_Engagement=("Engagement_Score", "mean"),
    Avg_Spending=("Monthly_Spending", "mean"),
    Avg_Training_Interest=("Training_Interest", "mean"),
    Avg_Internship_Interest=("Internship_Interest", "mean"),
    Avg_Service_Inquiries=("Service_Inquiries", "mean")
).round(2)

st.dataframe(
    profile,
    use_container_width=True
)


# ------------------------------------------------------------
# BUSINESS RECOMMENDATIONS
# ------------------------------------------------------------

st.subheader("💡 Business Recommendations")

st.markdown("""
### 1. Highly Engaged Customers
Focus on premium IT and digital solutions and maintain strong customer relationships.

### 2. Training-Focused Customers
Promote Data Analytics, Python, Machine Learning and other learning programs.

### 3. Internship-Focused Customers
Promote internship opportunities and industry-oriented programs.

### 4. Occasional Customers
Use beginner programs, orientation sessions and targeted campaigns to increase engagement.

### 5. Personalized Marketing
Use customer segments to send relevant offers instead of using the same marketing strategy for everyone.
""")


# ------------------------------------------------------------
# DATA TABLE
# ------------------------------------------------------------

st.subheader("📄 Customer Data")

st.dataframe(
    filtered_df[
        [
            "Customer_ID",
            "Customer_Segment",
            "Engagement_Score",
            "Monthly_Spending",
            "Training_Interest",
            "Internship_Interest",
            "Recommended_Service"
        ]
    ],
    use_container_width=True
)


st.divider()

st.caption(
    "Veda Technology | Data Science Internship | Day 4 Project"
)
