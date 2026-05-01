import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# Page config
# ---------------------------------------------------
st.set_page_config(
    page_title="Bank Deposit Subscription Predictor",
    page_icon="🏦",
    layout="wide"
)

# ---------------------------------------------------
# Load model
# ---------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load(r"C:\Users\name\Desktop\BIG FOLDER\PROJECTS\My_Projects\bank_deposit_prediction\model\tuned__rf.pkl")
model = load_model()

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.1rem;
    }

    .subtitle {
        font-size: 1rem;
        color: #9aa0a6;
        margin-bottom: 1.2rem;
    }

    .card {
        padding: 1rem 1.2rem;
        border-radius: 16px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1rem;
    }

    .result-success {
        padding: 1rem 1.2rem;
        border-radius: 14px;
        background-color: rgba(34, 197, 94, 0.12);
        border: 1px solid rgba(34, 197, 94, 0.35);
        font-weight: 600;
        font-size: 1.05rem;
    }

    .result-danger {
        padding: 1rem 1.2rem;
        border-radius: 14px;
        background-color: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.35);
        font-weight: 600;
        font-size: 1.05rem;
    }

    .small-note {
        color: #9aa0a6;
        font-size: 0.9rem;
    }

    .metric-label {
        font-size: 0.9rem;
        color: #9aa0a6;
    }

    .metric-value {
        font-size: 1.4rem;
        font-weight: 700;
    }

    .section-space {
        margin-top: 0.7rem;
        margin-bottom: 0.7rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Helper functions
# ---------------------------------------------------
def confidence_level(prob):
    if prob >= 0.80:
        return "High"
    elif prob >= 0.60:
        return "Moderate"
    return "Low"

def result_box(prediction):
    if prediction == 1:
        return """
        <div class="result-success">
            ✅ Prediction: This customer is likely to subscribe to the term deposit.
        </div>
        """
    return """
    <div class="result-danger">
        ❌ Prediction: This customer is unlikely to subscribe to the term deposit.
    </div>
    """

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:
    st.title("⚙️ Input Panel")
    st.caption("Fill in the customer and campaign information below.")

    with st.expander("👤 Customer Profile", expanded=True):
        age = st.number_input("Age", min_value=18, max_value=100, value=35)
        job = st.selectbox(
            "Job",
            ["admin.", "blue-collar", "entrepreneur", "housemaid", "management",
             "retired", "self-employed", "services", "student", "technician",
             "unemployed", "unknown"]
        )
        marital = st.selectbox("Marital Status", ["divorced", "married", "single"])
        education = st.selectbox("Education", ["primary", "secondary", "tertiary", "unknown"])

    with st.expander("💰 Financial Information", expanded=True):
        default = st.selectbox("Has Credit in Default?", ["no", "yes"])
        balance = st.number_input("Account Balance", value=1000)
        housing = st.selectbox("Housing Loan?", ["no", "yes"])
        loan = st.selectbox("Personal Loan?", ["no", "yes"])

    with st.expander("📞 Campaign Information", expanded=True):
        contact = st.selectbox("Contact Type", ["cellular", "telephone", "unknown"])
        month = st.selectbox(
            "Last Contact Month",
            ["jan", "feb", "mar", "apr", "may", "jun",
             "jul", "aug", "sep", "oct", "nov", "dec"]
        )
        duration = st.number_input("Last Contact Duration (seconds)", min_value=0, value=180)
        campaign = st.number_input("Number of Contacts During Campaign", min_value=1, value=2)
        previous = st.number_input("Number of Previous Contacts", min_value=0, value=0)
        poutcome = st.selectbox("Previous Campaign Outcome", ["failure", "other", "success", "unknown"])

    predict_button = st.button("🚀 Predict Subscription", use_container_width=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown('<div class="main-title">🏦 Bank Deposit Subscription Predictor</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Predict whether a customer is likely to subscribe to a term deposit using your trained Random Forest model.</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Top info cards
# ---------------------------------------------------
top1, top2, top3 = st.columns(3)

with top1:
    st.markdown("""
    <div class="card">
        <div class="metric-label">🎯 Model</div>
        <div class="metric-value">Random Forest</div>
        <div class="small-note">Current deployment model</div>
    </div>
    """, unsafe_allow_html=True)

with top2:
    st.markdown("""
    <div class="card">
        <div class="metric-label">📌 Task</div>
        <div class="metric-value">Binary Classification</div>
        <div class="small-note">Deposit subscription: Yes or No</div>
    </div>
    """, unsafe_allow_html=True)

with top3:
    st.markdown("""
    <div class="card">
        <div class="metric-label">🧾 Input Type</div>
        <div class="metric-value">Customer + Campaign</div>
        <div class="small-note">Interactive manual entry</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# Tabs
# ---------------------------------------------------
tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📋 Input Summary", "ℹ️ About"])

# ---------------------------------------------------
# Prepare input
# ---------------------------------------------------
input_data = pd.DataFrame([{
    "age": age,
    "job": job,
    "marital": marital,
    "education": education,
    "default": default,
    "balance": balance,
    "housing": housing,
    "loan": loan,
    "contact": contact,
    "month": month,
    "duration": duration,
    "campaign": campaign,
    "previous": previous,
    "poutcome": poutcome
}])

input_summary = pd.DataFrame(
    [
        ("Age", age),
        ("Job", job),
        ("Marital", marital),
        ("Education", education),
        ("Default", default),
        ("Balance", balance),
        ("Housing Loan", housing),
        ("Personal Loan", loan),
        ("Contact Type", contact),
        ("Month", month),
        ("Duration", duration),
        ("Campaign", campaign),
        ("Previous", previous),
        ("Poutcome", poutcome),
    ],
    columns=["Feature", "Value"]
)

# ---------------------------------------------------
# Prediction Tab
# ---------------------------------------------------
with tab1:
    left, right = st.columns([1.2, 0.8])

    with left:
        st.subheader("🔍 Live Prediction")
        st.write("Click the button in the sidebar to generate a prediction.")

        if predict_button:
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]
            confidence = confidence_level(probability)

            st.markdown(result_box(prediction), unsafe_allow_html=True)
            st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Predicted Class", "Yes" if prediction == 1 else "No")
            with m2:
                st.metric("Subscription Probability", f"{probability:.2%}")
            with m3:
                st.metric("Confidence", confidence)

            st.write("#### 📊 Probability Score")
            st.progress(float(probability))

            if confidence == "High":
                st.success("The model is highly confident in this prediction.")
            elif confidence == "Moderate":
                st.info("The model has moderate confidence in this prediction.")
            else:
                st.warning("The model has low confidence in this prediction.")

        else:
            st.info("Use the sidebar to fill the form, then click **Predict Subscription**.")

    with right:
        st.subheader("📌 Quick Notes")
        st.info(
            "This app predicts a customer's likelihood to subscribe to a term deposit.\n\n"
        )

        st.warning(
            "This is a decision-support tool. It should help guide campaign analysis, not replace business judgment."
        )

        st.success(
            "Useful outputs:\n"
            "- predicted class\n"
            "- probability score\n"
            "- confidence level"
        )

# ---------------------------------------------------
# Input Summary Tab
# ---------------------------------------------------
with tab2:
    col_a, col_b = st.columns([1.1, 0.9])

    with col_a:
        st.subheader("🧾 Customer and Campaign Summary")
        st.dataframe(input_summary, use_container_width=True, hide_index=True)

    with col_b:
        st.subheader("📈 Snapshot")
        st.markdown("""
        <div class="card">
            <b>Customer Profile</b><br><br>
            👤 Age: {age}<br>
            💼 Job: {job}<br>
            💍 Marital: {marital}<br>
            🎓 Education: {education}<br><br>

            <b>Financials</b><br><br>
            💰 Balance: {balance}<br>
            🏠 Housing Loan: {housing}<br>
            💳 Personal Loan: {loan}<br><br>

            <b>Campaign</b><br><br>
            📞 Contact: {contact}<br>
            🗓️ Month: {month}<br>
            ⏱️ Duration: {duration}<br>
            🔁 Campaign Contacts: {campaign}<br>
            📚 Previous: {previous}<br>
            🏁 Previous Outcome: {poutcome}
        </div>
        """.format(
            age=age, job=job, marital=marital, education=education,
            balance=balance, housing=housing, loan=loan,
            contact=contact, month=month, duration=duration,
            campaign=campaign, previous=previous, poutcome=poutcome
        ), unsafe_allow_html=True)

# ---------------------------------------------------
# About Tab
# ---------------------------------------------------
with tab3:
    st.subheader("ℹ️ About This App")
    st.write("""
    This Streamlit application deploys a **Random Forest classification model**
    trained on the bank marketing dataset to predict whether a customer will subscribe
    to a term deposit.

    ### What this app does
    - collects customer and campaign information
    - generates a prediction
    - shows the probability of subscription
    - provides a confidence label

    """)

    st.subheader("🛠️ Tech Stack")
    tech1, tech2, tech3 = st.columns(3)
    tech1.info("**Frontend**\n\nStreamlit")
    tech2.info("**ML Pipeline**\n\nScikit-learn")
    tech3.info("**Data Handling**\n\nPandas")

    st.subheader("📚 Model Features")
    st.code("""
age, job, marital, education, default, balance, housing, loan,
contact, day, month, duration, campaign, pdays, previous, poutcome
""")