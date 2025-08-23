import streamlit as st
import pandas as pd
import calendar

# Drop rows with missing 'Date'
df = pd.read_csv("diary_LLM4.csv", parse_dates=['Date'])

st.title("📅 How are you feeling? (Calendar)")
st.markdown("<p style='font-size:16px; color:gray;'>Track your students' emotions 🙌</p>", unsafe_allow_html=True)

# Select student
students = df["Name"].unique()
selected_student = st.selectbox("Select Student", students)

# Select year/month
years = sorted(df["Date"].dt.year.unique(), reverse=True)
selected_year = st.selectbox("Select Year", years)
months = list(range(1, 13))
selected_month = st.selectbox("Select Month", months)

# Filter data for the selected student and month
student_data = df[(df["Name"]==selected_student) & 
                  (df["Date"].dt.year==selected_year) & 
                  (df["Date"].dt.month==selected_month)]

# Map emotions to emojis
emotion_dict = {
    "joy": "😄",
    "sadness": "😢",
    "anger": "😠",
    "neutral": "😐",
    "worry": "😟",
    "happy": "😊"
}

# Create HTML per date (date + emoji + text)
emoji_by_day = {}
for _, row in student_data.iterrows():
    emoji = emotion_dict.get(row["dominant_emotion"], "❓")
    size = int(row["dominant_score"] * 20)  # multiply by dominant_score for size
    text = row["dominant_emotion"]
    emoji_by_day[row["Date"].day] = f"""
    <div style='text-align:center;'>
        <div>{row['Date'].day}</div>
        <div style='font-size:{size}px'>{emoji}</div>
        <div style='font-size:12px; color:gray'>{text}</div>
    </div>
    """

# Create calendar
cal = calendar.Calendar(firstweekday=6)  # start with Sunday
month_days = cal.monthdayscalendar(selected_year, selected_month)

month_name = calendar.month_name[selected_month]
st.write(f"### {selected_student}'s Emotion Calendar ")

weekday_names = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

# Generate HTML table
table_html = "<table style='border-collapse: collapse; text-align:center; width:100%'>"

# Weekday header
table_html += "<tr>"
for wd in weekday_names:
    # Sunday red, Saturday blue, others black
    if wd == "Sun":
        color = "red"
    elif wd == "Sat":
        color = "blue"
    else:
        color = "black"
    table_html += f"<th style='padding:5px; background-color:#f0f0f0; color:{color};'>{wd}</th>"
table_html += "</tr>"

# Calendar rows
for week in month_days:
    table_html += "<tr>"
    for day in week:
        if day == 0:
            table_html += "<td></td>"
        else:
            if day in emoji_by_day:
                table_html += f"<td style='padding:5px; vertical-align:top'>{emoji_by_day[day]}</td>"
            else:
                table_html += f"<td style='padding:5px; vertical-align:top'>{day}</td>"
    table_html += "</tr>"

table_html += "</table>"

# Display table in Streamlit
st.markdown(table_html, unsafe_allow_html=True)

