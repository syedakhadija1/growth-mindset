import streamlit as st
import random
import time
from datetime import datetime
import plotly.graph_objects as go

# Set page config at the very beginning
st.set_page_config(page_title="Python Mastery", page_icon="🐍", layout="wide")

# Initialize session state for theme
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Custom Styling with Theme Toggle
def set_theme():
    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
                body {
                    background-color: #1E1E1E;
                    color: #E0E0E0;
                }
                .stButton > button {
                    background: linear-gradient(90deg, #FF69B4, #FFB6C1);
                    color: #FFFFFF;
                }
                .stTextArea > div > div > textarea {
                    background-color: #2D2D2D;
                    color: #E0E0E0;
                    border-color: #FF69B4;
                }
                .stCard {
                    background-color: #2D2D2D;
                    border: 2px solid #FF69B4;
                    color: #E0E0E0;
                }
                .stProgress > div > div > div > div {
                    background: linear-gradient(90deg, #FF69B4, #FFB6C1);
                }
                .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
                    color: #FF69B4;
                }
                .stRadio > div {
                    background-color: #2D2D2D;
                    color: #E0E0E0;
                }
                .sidebar-content {
                    background-color: #2D2D2D;
                    color: #E0E0E0;
                }
                .stSelectbox > div > div {
                    background-color: #2D2D2D;
                    color: #E0E0E0;
                }
                .stSelectbox > div > div > div {
                    background-color: #2D2D2D;
                    color: #E0E0E0;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
                body {
                    background-color: #FFFFFF;
                    color: #000000;
                }
                .stButton > button {
                    background: linear-gradient(90deg, #FF69B4, #FFB6C1);
                    color: #FFFFFF;
                }
                .stTextArea > div > div > textarea {
                    background-color: #FFB6C1;
                    color: #000000;
                }
                .stCard {
                    background-color: #FFB6C1;
                    border: 2px solid #FF69B4;
                }
                .stProgress > div > div > div > div {
                    background: linear-gradient(90deg, #FF69B4, #FFB6C1);
                }
            </style>
            """,
            unsafe_allow_html=True
        )

# Apply theme
set_theme()

# Custom Styling with White and Pink Theme
st.markdown(
"""
<style>
    /* Main Background Color */
    body {
        font-family: 'Arial', sans-serif;
    }

    /* Progress Bar Styling */
    .stProgress > div > div > div > div {
        border-radius: 12px;
        animation: progressBar 2s ease-in-out;
    }

    /* Button Styling */
    .stButton > button {
        border-radius: 12px;
        padding: 12px 24px;
        width: 100%;
        font-weight: bold;
        border: none;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        animation: fadeInUp 1s ease-in-out;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Text Area Styling */
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid #FF69B4;
        padding: 10px;
        transition: border-color 0.3s ease;
        animation: fadeInLeft 1s ease-in-out;
    }
    .stTextArea > div > div > textarea:focus {
        border-color: #FF69B4;
    }

    /* Radio Button Styling */
    .stRadio > div {
        padding: 15px;
        border-radius: 12px;
        border: 2px solid #FF69B4;
        animation: fadeInRight 1s ease-in-out;
    }

    /* Header Styling */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #FF69B4;
        margin-bottom: 10px;
        animation: fadeInDown 1s ease-in-out;
    }

    /* Card-like Styling for Sections */
    .stCard {
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        animation: fadeInUp 1s ease-in-out;
    }
    .stCard:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeInRight {
        from { opacity: 0; transform: translateX(20px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes progressBar {
        from { width: 0; }
        to { width: 100%; }
    }

    /* Badge Styling */
    .badge {
        background: linear-gradient(90deg, #FF69B4, #FFB6C1);
        color: white;
        padding: 5px 15px;
        border-radius: 25px;
        font-weight: bold;
        display: inline-block;
        margin: 5px;
        box-shadow: 0 4px 15px 0 rgba(255, 105, 180, 0.45);
    }
</style>
""",
unsafe_allow_html=True
)

# Initialize session state
if "progress" not in st.session_state:
    st.session_state.progress = random.randint(30, 90)
if "badges" not in st.session_state:
    st.session_state.badges = []
if "last_challenge_date" not in st.session_state:
    st.session_state.last_challenge_date = None
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "username" not in st.session_state:
    st.session_state.username = ""
if "profile_pic" not in st.session_state:
    st.session_state.profile_pic = None
if "feedback" not in st.session_state:
    st.session_state.feedback = []
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "level" not in st.session_state:
    st.session_state.level = 1

# Python Mastery Content
python_tips = [
    "✨ Python is versatile and beginner-friendly!",
    "🚀 Use list comprehensions for concise code.",
    "💡 Master Python libraries like NumPy and Pandas for data analysis.",
    "🎯 Practice coding daily to improve your skills.",
    "🔥 Debugging is a crucial skill for every Python developer."
]

python_challenges = [
    "✍️ Write a Python program to reverse a string.",
    "🧩 Solve a problem using recursion.",
    "🤝 Create a Python script to automate a task.",
    "🔄 Refactor your code to make it more efficient.",
    "🚀 Build a small project using Flask or Django."
]

# Important Python Functions
important_functions = [
    {"name": "print()", "description": "Outputs data to the console."},
    {"name": "len()", "description": "Returns the length of an object."},
    {"name": "type()", "description": "Returns the type of an object."},
    {"name": "str()", "description": "Converts an object to a string."},
    {"name": "int()", "description": "Converts an object to an integer."},
    {"name": "float()", "description": "Converts an object to a float."},
    {"name": "list()", "description": "Creates a list from an iterable."},
    {"name": "dict()", "description": "Creates a dictionary from key-value pairs."},
    {"name": "range()", "description": "Generates a sequence of numbers."},
    {"name": "sum()", "description": "Returns the sum of a sequence."}
]

# Python Quiz Questions
python_quiz = [
    {
        "question": "What is the output of `print(2 ** 3)`?",
        "options": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    # ... (other quiz questions)
]

st.title("🐍 Python Mastery: From Basic to Advanced")

# Sidebar
with st.sidebar:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.markdown("<h1>🌟 User Profile</h1>", unsafe_allow_html=True)
    
    # Theme toggle
    theme = st.selectbox("Choose Theme", ["light", "dark"], key="theme")
    set_theme()
    
    st.session_state.username = st.text_input("Enter your username:", value=st.session_state.username)
    st.session_state.profile_pic = st.file_uploader("Upload a profile picture:", type=["jpg", "png"])
    if st.session_state.profile_pic:
        st.image(st.session_state.profile_pic, width=100)

    st.markdown("---")
    st.markdown(f"🔥 **Current Streak:** {st.session_state.streak} days")
    st.markdown(f"✨ **XP:** {st.session_state.xp}")
    st.markdown(f"🏆 **Level:** {st.session_state.level}")

    # XP Progress Bar
    xp_to_next_level = 1000 * st.session_state.level
    xp_progress = (st.session_state.xp % xp_to_next_level) / xp_to_next_level
    st.progress(xp_progress)
    st.text(f"{st.session_state.xp % xp_to_next_level}/{xp_to_next_level} XP to next level")

    st.markdown("---")
    st.markdown("<h2>🏆 Leaderboard</h2>", unsafe_allow_html=True)
    leaderboard = {"User 1": 99, "User 2": 85, "User 3": 75}
    for user, score in leaderboard.items():
        medal = "🥇" if user == "User 1" else "🥈" if user == "User 2" else "🥉"
        st.write(f"{medal} {user}: {score}%")
    st.markdown("</div>", unsafe_allow_html=True)

# Main content
st.markdown(
"""
<div class="stCard">
    <h2>🚀 What is Python Mastery?</h2>
    <p>Python Mastery is about mastering Python programming from basic concepts to advanced techniques. This app will guide you through learning Python step-by-step.</p>
</div>
""",
unsafe_allow_html=True
)

# Important Python Functions
st.markdown(
"""
<div class="stCard">
    <h2>🔍 Important Python Functions</h2>
    <p>Here are some important Python functions you should know:</p>
    <ul>
""",
unsafe_allow_html=True
)

for func in important_functions:
    st.markdown(f"<li><b>{func['name']}</b>: {func['description']}</li>", unsafe_allow_html=True)

st.markdown(
"""
    </ul>
</div>
""",
unsafe_allow_html=True
)

# Python Tips
if st.button("🌟🤗 Get Python Tips"):
    st.info(random.choice(python_tips))
    st.session_state.xp += 10
    st.success("You earned 10 XP for seeking knowledge!")

# Python Quiz
st.markdown(
"""
<div class="stCard">
    <h2>🧠😇 Python Quiz</h2>
</div>
""",
unsafe_allow_html=True
)

if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

question_data = python_quiz[st.session_state.quiz_index]
st.write(f"**Question {st.session_state.quiz_index + 1}:** {question_data['question']}")
user_answer = st.radio("Select an option:", question_data["options"])

if st.button("Submit Answer"):
    if user_answer == question_data["answer"]:
        st.session_state.score += 1
        st.success("✅ Correct! Well done!")
        st.session_state.xp += 50
        st.success("You earned 50 XP for your correct answer!")
    else:
        st.warning(f"❌ Incorrect! The correct answer is: {question_data['answer']}")
        st.session_state.xp += 10
        st.info("You earned 10 XP for attempting. Keep learning!")
    st.session_state.quiz_index += 1
    if st.session_state.quiz_index >= len(python_quiz):
        st.session_state.quiz_index = 0
        st.balloons()  
        st.success(f"🎉🙌 Quiz Completed! Your final score is: {st.session_state.score}/{len(python_quiz)}")
        if st.session_state.score == len(python_quiz):
            st.session_state.xp += 500
            st.success("🏆 Perfect score! You earned a bonus 500 XP!")
        st.session_state.score = 0

# Progress
st.markdown(
"""
<div class="stCard">
    <h2>📊 Your Python Mastery Progress:</h2>
</div>
""",
unsafe_allow_html=True
)
st.progress(st.session_state.progress / 100)

# Skill Tree Visualization
st.markdown(
"""
<div class="stCard">
    <h2>🌳 Your Python Skill Tree</h2>
</div>
""",
unsafe_allow_html=True
)

skills = {
    "Basics": st.session_state.progress,
    "Data Structures": max(0, st.session_state.progress - 10),
    "Functions": max(0, st.session_state.progress - 20),
    "OOP": max(0, st.session_state.progress - 30),
    "Libraries": max(0, st.session_state.progress - 40),
    "Web Development": max(0, st.session_state.progress - 50),
    "Data Science": max(0, st.session_state.progress - 60),
    "Machine Learning": max(0, st.session_state.progress - 70),
}

fig = go.Figure(go.Scatterpolar(
    r=list(skills.values()),
    theta=list(skills.keys()),
    fill='toself',
    line_color='#FF69B4'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )),
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig)

# Daily Challenge
st.markdown(
"""
<div class="stCard">
    <h2>🎯 Daily Python Challenge</h2>
</div>
""",
unsafe_allow_html=True
)
if st.button("Give me a challenge!"):
    today = datetime.today().date()
    if st.session_state.last_challenge_date != today:
        challenge = random.choice(python_challenges)
        st.session_state.last_challenge_date = today
        st.warning(challenge)
        st.session_state.progress = min(100, st.session_state.progress + 10)  
        st.session_state.streak += 1
        st.session_state.xp += 100
        st.success(f"You've completed the daily challenge! You earned 100 XP and your streak is now {st.session_state.streak} days!")
        if st.session_state.progress % 20 == 0:  
            badge = f"🏆 {st.session_state.progress}% Progress Badge"
            st.session_state.badges.append(badge)
            st.balloons()  
            st.success(f"Badge Earned: {badge}")
    else:
        st.info("You've already completed today's challenge. Try again tomorrow!")

# Badges
if st.session_state.badges:
    st.markdown(
        """
        <div class="stCard">
            <h2>🏅 Your Badges</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    for badge in st.session_state.badges:
        st.markdown(f'<div class="badge">{badge}</div>', unsafe_allow_html=True)

# Feedback
st.markdown(
"""
<div class="stCard">
    <h2>📝 Feedback</h2>
</div>
""",
unsafe_allow_html=True
)
feedback = st.text_area("How can we improve this app?")
if st.button("Submit Feedback"):
    if feedback:
        st.session_state.feedback.append(feedback)
        st.success("Thank you! Your feedback is very valuable to us.")
        st.session_state.xp += 25
        st.info("You've earned 25 XP for providing feedback!")

# Personalized Learning Path
st.markdown(
"""
<div class="stCard">
    <h2>🗺️ Your Personalized Learning Path</h2>
</div>
""",
unsafe_allow_html=True
)
learning_path = [
    "Master Python Basics",
    "Dive into Data Structures",
    "Explore Advanced Functions",
    "Conquer Object-Oriented Programming",
    "Harness the Power of Python Libraries",
    "Build Web Applications with Django or Flask",
    "Analyze Data with Pandas and NumPy",
    "Implement Machine Learning with Scikit-learn"
]
current_step = min(len(learning_path) - 1, st.session_state.level - 1)
st.write(f"Your current focus: **{learning_path[current_step]}**")
st.progress((current_step + 1) / len(learning_path))

# Motivational Quote
if st.button("Boost Your Day❤️‍🔥❤️"):
    with st.spinner("Processing..."):
        time.sleep(1.5)
    st.markdown(
        """
        <style>
        .motivational-text {
            font-size: 24px;
            color: #FF6347;
            font-weight: bold;
            text-align: center;
            background-color: #2D2D2D;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(255, 255, 255, 0.1);
        }
        </style>
        <div class="motivational-text">
            🚀 **You are unstoppable!** Every challenge you face is just another opportunity to grow. Your hard work is the key to unlocking your success. Keep pushing and never stop believing in your potential. 🌟
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()

# Footer
st.markdown("---")
st.markdown(
"""
<p style='text-align: center; font-size: 18px; color: #808080;'>
    🔹 <b>Made by Khadija Abrar🎀🌸</b> 🔹
    <br>
    <a href='https://github.com/syedakhadija1' target='_blank' style='color: #FF69B4;'>
        <i class='fab fa-github github-icon'></i> GitHub Repository
    </a>
</p>
""",
unsafe_allow_html=True
)

