import streamlit as st
from inference6 import start_game

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f4f8;
        color: #333;
    }
    .custom-button {
        background-color: #0d4954; 
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        transition: background-color 0.3s, transform 0.3s;
    }
    .custom-button:hover {
        background-color: #1e6a7e;
        transform: translateY(-2px);
    }
    .section {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .team-member {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .team-member img {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        margin-right: 15px;
    }
    .center-content {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with logo
st.sidebar.image("assets/osulogoblue.png", width=200)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Team", "How to Play"])

if page == "Home":
    st.title("Welcome to Osulation!")
    st.subheader("A fun way to play osu! with hand gestures")
    
    st.write("### Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("#### Intuitive Controls")
        st.write("Use hand movements to play without a controller")
    
    with col2:
        st.write("#### Real-time Tracking")
        st.write("Responsive and accurate gesture recognition")
    
    with col3:
        st.write("#### Beyond Osu")
        st.write("Control other apps and games using hand movements")
    
    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    if st.button("Start Osulation", key="start_button"):
        start_game()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # GitHub link
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://github.com/elise-yz/osulation" target="_blank" style="text-decoration: none;">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" style="vertical-align: middle;">
                <span style="vertical-align: middle; margin-left: 10px;">View on GitHub</span>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

elif page == "About":
    st.header("About Osulation")
    
    st.markdown("""
    <div class="section">
        <h3>What is Osulation?</h3>
        <p>Osulation is an innovative project that combines the popular rhythm game osu! with hand gesture controls. 
        Our goal is to create a more immersive and physically engaging gaming experience.</p>
    </div>
    
    <div class="section">
        <h3>Key Features</h3>
        <ul>
            <li>Hand gesture recognition for gameplay</li>
            <li>Real-time tracking and responsiveness</li>
            <li>Can be used with popular osu! beatmaps</li>
            <li>Applicable to other games and applications</li>
        </ul>
    </div>
    
    <div class="section">
        <h3>Technology Stack</h3>
        <ul>
            <li>Python for backend logic</li>
            <li>OpenCV for image processing</li>
            <li>Roboflow for hand tracking</li>
            <li>Streamlit for the web interface</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "Team":
    st.header("Meet the Team")
    
    st.markdown("""
    <div class="section">
        <div class="team-member">
            <img src="https://via.placeholder.com/50" alt="Team Member 1">
            <div>
                <h4>Elise Zhang</h4>
                <p>Project Lead & Full-stack Developer</p>
            </div>
        </div>
        <div class="team-member">
            <img src="https://via.placeholder.com/50" alt="Team Member 2">
            <div>
                <h4>Alex Johnson</h4>
                <p>Computer Vision Specialist</p>
            </div>
        </div>
        <div class="team-member">
            <img src="https://via.placeholder.com/50" alt="Team Member 3">
            <div>
                <h4>Samantha Lee</h4>
                <p>UI/UX Designer</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "How to Play":
    st.header("How to Play Osulation")
    
    st.markdown("""
    <div class="section">
        <h3>Getting Started</h3>
        <ol>
            <li>Ensure your webcam is connected and functioning.</li>
            <li>Click the "Start Osulation" button on the home page.</li>
            <li>Allow the application to access your camera.</li>
            <li>Position yourself so that your hands are clearly visible to the camera.</li>
        </ol>
    </div>
    
    <div class="section">
        <h3>Gameplay</h3>
        <ul>
            <li>Use your right hand to control the gameplay.</li>
            <li>Move your hand with an open palm to move the cursor.<li>
            <li>Close your hand into a fist to tap each circle</li>
            <li>Time your taps to the rhythm of the music for higher scores.</li>
        </ul>
    </div>
    
    <div class="section">
        <h3>Tips & Tricks</h3>
        <ul>
            <li>Practice makes perfect! Start with easier beatmaps and work your way up.</li>
            <li>Ensure good lighting for better hand tracking.</li>
            <li>Make sure your camera is level and stable.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)