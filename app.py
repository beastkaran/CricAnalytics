import streamlit as st
import pandas as pd
import plotly.express as px
import time

# Custom CSS for visual appeal and animations
st.markdown("""
    <style>
    body {background-color: #e6ffe6;}
    .title {text-align: center; color: #006400; font-size: 48px; font-family: 'Arial', sans-serif;}
    .subtitle {text-align: center; color: #4682b4; font-size: 24px;}
    .dashboard {background-color: #006400; padding: 10px; border-radius: 10px; color: white; text-align: center;}
    .section {margin-top: 20px; padding: 15px; background-color: #f0fff0; border-radius: 10px; box-shadow: 2px 2px 5px grey;}
    .highlight {font-size: 20px; color: #ff4500; font-weight: bold;}
    .animate-spin {animation: spin 2s linear infinite;}
    @keyframes spin {0% {transform: rotate(0deg);} 100% {transform: rotate(360deg);}}
    .fade-in {animation: fadeIn 1s ease-in;}
    @keyframes fadeIn {0% {opacity: 0;} 100% {opacity: 1;}}
    </style>
""", unsafe_allow_html=True)

# Top Dashboard
st.markdown("<div class='dashboard'><h2>🏏 CricAIlytics Dashboard</h2><p>Analyze | Explore | Win</p></div>", unsafe_allow_html=True)

# Title and Subtitle
st.markdown("<h1 class='title fade-in'>CricAIlytics</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Your AI-Powered Cricket Companion</h3>", unsafe_allow_html=True)

# Mock Sign-In (Optional - Demo Only)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("### Sign In to Unlock Full Features")
    username = st.text_input("Username", "teamace")
    password = st.text_input("Password", "hackathon2025", type="password")
    if st.button("Login"):
        if username == "teamace" and password == "hackathon2025":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Wrong credentials!")
else:
    # Main App Content
    # Load data
    data = pd.read_csv("cricket_data.csv")

    # Player Selection
    st.markdown("<div class='section fade-in'>", unsafe_allow_html=True)
    st.write("### Analyze a Player")
    player = st.selectbox("Choose a player", data["Player Name"], help="Pick a cricketer to analyze!")
    if st.button("Analyze", key="analyze_btn"):
        with st.spinner("🏏 AI Analyzing..."):
            time.sleep(1)
            player_data = data[data["Player Name"] == player].iloc[0]
            
            # Analysis Section
            st.markdown(f"### Analyzing <span class='highlight'>{player}</span>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Strengths**")
                st.info(player_data["Strengths"])
            with col2:
                st.markdown("**Weaknesses**")
                st.warning(player_data["Weaknesses"])

            # Strategy Tip
            if player_data["Dismissals by Pace"] > player_data["Dismissals by Spin"]:
                strategy = "Deploy fast bowlers to exploit pace vulnerability!"
            elif player_data["Dismissals by Spin"] > player_data["Dismissals by Pace"]:
                strategy = "Bring in spinners to target spin weakness!"
            else:
                strategy = "Mix pace and spin for a balanced attack."
            st.markdown("**AI Strategy Tip**")
            st.success(strategy)

            # Chart
            chart_data = pd.DataFrame({
                "Bowling Type": ["Spin", "Pace"],
                "Runs": [player_data["Runs vs Spin"], player_data["Runs vs Pace"]]
            })
            fig = px.bar(chart_data, x="Bowling Type", y="Runs", 
                         title=f"{player}'s Performance", 
                         color="Bowling Type", color_discrete_map={"Spin": "#4682b4", "Pace": "#ff4500"})
            fig.update_layout(width=600, height=400)
            st.plotly_chart(fig)

            # Video Highlights
            st.markdown("### Highlight Videos")
            col3, col4 = st.columns(2)
            with col3:
                st.markdown("**Dismissal (Out)**")
                st.video(player_data["Out Video"], format="video/mp4")  # Google Drive link
            with col4:
                st.markdown("**Six**")
                st.video(player_data["Six Video"], format="video/mp4")  # Google Drive link
    st.markdown("</div>", unsafe_allow_html=True)

    # Scrollable About Section
    st.markdown("<div class='section fade-in'>", unsafe_allow_html=True)
    st.markdown("### About CricAIlyt千里cs")
    st.write("""
        Welcome to *CricAIlytics*—where cricket meets cutting-edge AI! We’re Team AceHackers, four beginners who built this in 24 hours for AceHack 4.0. Our mission? To help coaches win matches and fans feel the thrill with real-time insights and video highlights.

        **Cricket Fun Facts**:
        - Did you know? The fastest recorded delivery was 161.3 km/h by Shoaib Akhtar!
        - Virat Kohli has hit over 70 international centuries—talk about strength!
        - Spin bowling dismisses more batsmen in Test cricket than pace.

        **Why We’re Here**: We love cricket and tech. This dashboard analyzes players, suggests strategies, and shows epic moments—all powered by Python, Streamlit, and a dash of creativity. Scroll down for more!
    """)
    st.markdown("<p class='animate-spin' style='font-size: 30px;'>🏏</p>", unsafe_allow_html=True)  # Spinning cricket ball
    st.write("Built with 💪 by Team AceHackers - UEM Jaipur, March 2025")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #006400;'>CricAIlytics | AceHack 4.0 | Smarter Cricket, Smarter Wins</p>", unsafe_allow_html=True)