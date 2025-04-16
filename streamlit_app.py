# streamlit_app.py
import streamlit as st
import datetime
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Step 1: Collect student data
st.title("🎓 Predict-My-Career-Personality")
st.subheader("Let's build your personality profile!")

min_dob = datetime.date(1925, 1, 1)
max_dob = datetime.date.today()

with st.form("student_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    whatsapp = st.text_input("WhatsApp Number")
    city = st.text_input("City")
    state = st.text_input("State")
    country = st.text_input("Country")
    dob = st.date_input("Date of Birth", value=datetime.date(2010, 1, 1), min_value=min_dob, max_value=max_dob)

    # Personality questions (expanded set)
    st.markdown("### Personality Discovery Questions:")
    mbti_q = st.radio("Do you enjoy spending time alone or with others?", ["Alone", "With others"])
    big5_q = st.radio("Do you prefer routines or flexibility?", ["Routines", "Flexibility"])
    disc_q = st.radio("When solving problems, do you prefer to lead or support?", ["Lead", "Support"])
    curiosity_q = st.radio("Do you often wonder how things work or ask 'what if' questions?", ["Yes", "No"])
    emotion_q = st.radio("When you're upset, do you prefer talking to someone or processing alone?", ["Talk to someone", "Alone"])
    goal_q = st.radio("Which is more satisfying to you: starting a new idea or finishing a task?", ["Starting a new idea", "Finishing a task"])

    submitted = st.form_submit_button("Generate Report")

# Store student name for session
if submitted:
    st.session_state["student_name"] = name
    st.session_state["student_age"] = datetime.date.today().year - dob.year
    st.session_state["student_city"] = city
    st.session_state["student_country"] = country

    # Basic logic for mock personality profiling
    mbti = "INFP" if mbti_q == "Alone" else "ENFP"
    conscientiousness = "Low" if big5_q == "Flexibility" else "High"
    disc = "High I" if disc_q == "Lead" else "High S"

    st.success("Awesome! Your data is saved. Now we will analyze your personality.")

    # Career recommendation logic (basic mapping)
    if mbti == "INFP":
        best_careers = ["Writer", "Therapist", "Graphic Designer"]
        avoid_careers = ["Corporate Sales", "Mechanical Engineering"]
    elif mbti == "ENFP":
        best_careers = ["Public Speaker", "Marketing Creative", "Content Creator"]
        avoid_careers = ["Data Entry", "Accounting"]
    else:
        best_careers = ["Teacher", "Social Worker"]
        avoid_careers = ["Technical Auditor"]

    report_text = f"""
    Career Direction Insight for {name}
    Location: {city}, {country}

    Personality Type: {mbti}
    DISC Profile: {disc}
    Conscientiousness: {conscientiousness}

    ✅ Most Aligned Careers:
    - {best_careers[0]}
    - {best_careers[1]}
    - {best_careers[2]}

    ❌ Careers You Might Not Enjoy:
    - {avoid_careers[0]}
    - {avoid_careers[1]}

    These are based on your natural energy, creativity, and how you prefer to interact with the world.
    """

    st.markdown(f"""
    ## 💼 Career Direction Insight
    Based on your personality profile (**{mbti}**, {disc}, Conscientiousness: {conscientiousness}):

    ### ✅ Most Aligned Careers:
    - {best_careers[0]}
    - {best_careers[1]}
    - {best_careers[2]}

    ### ❌ Careers You Might Not Enjoy:
    - {avoid_careers[0]}
    - {avoid_careers[1]}

    These are based on your natural energy, creativity, and how you prefer to interact with the world.
    """)

    # Generate PDF report
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    text = c.beginText(40, height - 50)
    text.setFont("Helvetica", 11)
    for line in report_text.strip().split("\n"):
        text.textLine(line)
    c.drawText(text)
    c.save()
    buffer.seek(0)

    # Download button
    st.download_button(
        label="📥 Download My Personality Career Report as PDF",
        data=buffer,
        file_name=f"{name.replace(' ', '_')}_career_report.pdf",
        mime ="application/pdf"
    )
