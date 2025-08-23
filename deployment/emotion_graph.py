import streamlit as st
import pandas as pd
import altair as alt


df = pd.read_csv("diary_LLM3.csv")

st.title("📈 How are you feeling? (Graph)")
st.markdown("<p style='font-size:16px; color:gray;'>Track your students' emotions 🙌</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:14px; color:gray;'> This is a version for students who forget to record dates</p>", unsafe_allow_html=True)

# Select student
students = df["Name"].unique()
selected_student = st.selectbox("Select Student", students)

# Filter data for the selected student
student_data = df[df["Name"]==selected_student].copy()

# Exclude rows where 'Number' is empty
student_data = student_data[student_data["Number"].notnull()]

# Extract numeric part from 'Number' and sort
student_data["Number_int"] = student_data["Number"].str.extract("(\d+)").astype(int)
student_data = student_data.sort_values("Number_int").reset_index(drop=True)

# Map dominant_emotion to emoji
emotion_dict = {
    "joy": "😄",
    "sadness": "😢",
    "anger": "😠",
    "neutral": "😐",
    "worry": "😟",
    "happy": "😊"
}

student_data["Emoji"] = student_data["dominant_emotion"].map(emotion_dict)
student_data["Y"] = student_data["dominant_score"]

# Check for consecutive negative emotions (sadness, anger, worry)
negative_emotions = ["sadness", "anger", "worry"]
student_data["is_negative"] = student_data["dominant_emotion"].isin(negative_emotions).astype(int)

# Calculate the longest streak of consecutive negative emotions
max_streak = 0
current_streak = 0
for val in student_data["is_negative"]:
    if val == 1:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0

# Display warning if 3 or more consecutive negative days detected
if max_streak >= 3:
    st.warning(f"⚠️ Warning: {max_streak} consecutive days of negative emotions detected for {selected_student}!")

# Emoji layer
emoji_layer = alt.Chart(student_data).mark_text(fontSize=30).encode(
    x=alt.X("Number:N", title="Diary Entry", sort=student_data["Number"].tolist()),
    y=alt.Y("Y:Q", title="Dominant Score", scale=alt.Scale(domain=[0,1])),
    text="Emoji:N",
    color=alt.Color("dominant_emotion:N", legend=None),
    tooltip=["Number", "dominant_emotion", "dominant_score"]
)

# Text layer (below emoji)
text_layer = alt.Chart(student_data).mark_text(
    dy=15,  # below the emoji
    fontSize=12,
    color='black'
).encode(
    x=alt.X("Number:N", sort=student_data["Number"].tolist()),
    y="Y:Q",
    text="dominant_emotion:N"
)

# Combine layers
chart = alt.layer(emoji_layer, text_layer).interactive()

# Display chart
st.altair_chart(chart, use_container_width=True)
