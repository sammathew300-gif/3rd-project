import pandas as pd

# Load HR Job Placement dataset
df = pd.read_csv(
    r"C:/Users/Admin/Downloads/HR_Job_Placement_Dataset.csv"
)

print(df.head())




import streamlit as st

# Calculate KPIs
total_candidates = len(df)

placed_candidates = (df['status'] == 1).sum()

placement_rate = (
    placed_candidates / total_candidates
) * 100 if total_candidates > 0 else 0

job_acceptance_rate = placement_rate

average_interview_score = df[
    ['technical_score',
     'aptitude_score',
     'communication_score']
].mean(axis=1).mean()

average_skills_match = df[
    'skills_match_percentage'
].mean()

high_risk_candidates = (
    df['technical_score'] < 40
).sum()

high_risk_percentage = (
    high_risk_candidates / total_candidates
) * 100 if total_candidates > 0 else 0

# Dashboard title
st.title("HR Job Placement Analytics Dashboard")

# Display KPI metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Candidates", total_candidates)
col2.metric("Placement Rate", f"{placement_rate:.2f}%")
col3.metric("Job Acceptance Rate", f"{job_acceptance_rate:.2f}%")

col4, col5, col6 = st.columns(3)

col4.metric("Average Interview Score",
            f"{average_interview_score:.2f}")

col5.metric("Average Skills Match",
            f"{average_skills_match:.2f}%")

col6.metric("High-Risk Candidates",
            f"{high_risk_percentage:.2f}%")

# Offer dropout rate is unavailable
st.metric("Offer Dropout Rate", "N/A")