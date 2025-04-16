# streamlit_app.py
import streamlit as st
import datetime

# Step 1: Collect student data
st.title("🎓 Predict-My-Career-Personality")
st.subheader("Let's build your personality profile!")

with st.form("student_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    whatsapp = st.text_input("WhatsApp Number")
    city = st.text_input("City")
    state = st.text_input("State")
    country = st.text_input("Country")
    dob = st.date_input("Date of Birth", value=datetime.date(2010, 1, 1))

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

    # Fun coaching summary in extended report style with career guidance
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
