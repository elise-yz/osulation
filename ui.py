import streamlit as st
from inference6 import start_game
import plotly.graph_objects as go

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
page = st.sidebar.radio("Go to", ["Home", "About", "Team", "How to Play", "Data Visualization"])

if page == "Home":
    st.title("Welcome to Osulation!")
    
    # Animated and italicized subheader
    st.markdown("""
        <h2 class="animated-subheader">A fun way to play osu! with hand gestures</h2>
    """, unsafe_allow_html=True)

    st.write("---")  # Add a horizontal line for separation

    st.write("### Key Features")
    col1, col2, col3 = st.columns(3)

    # Define a common height for the feature containers
    feature_height = "300px"

    # Adding feature descriptions with animations
    with col1:
        st.markdown(f"""
            <div class="feature-container" style="height: {feature_height};">
                <h4>Intuitive Controls</h4>
                <p>Use hand movements to play without a controller</p>
                <img src="https://icons.veryicon.com/png/o/miscellaneous/icon-pack/hand-23.png" width="100" />
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="feature-container" style="height: {feature_height};">
                <h4>Real-time Tracking</h4>
                <p>Responsive and accurate gesture recognition</p>
                <img src="https://www.freeiconspng.com/thumbs/cursor-png/cursor-png-ico-icns-free-icon-download--icon100m-20.png" width="100" />
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="feature-container" style="height: {feature_height};">
                <h4>Beyond Osu</h4>
                <p>Control other apps and games using hand movements</p>
                <img src="https://cdn-icons-png.flaticon.com/512/181/181838.png" width="100" />
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    if st.button("Start Osulation", key="start_button", help="Click to start the game!"):
        start_game()
    st.markdown('</div>', unsafe_allow_html=True)

    # GitHub link with enhanced styling
    st.markdown(
        """
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://github.com/elise-yz/osulation" target="_blank" style="text-decoration: none; display: flex; align-items: center; transition: transform 0.3s;">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" style="vertical-align: middle; transition: transform 0.3s;">
                <span style="vertical-align: middle; margin-left: 10px; font-size: 18px; color: #333;">View on GitHub</span>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    # CSS for animations and styling
    st.markdown(
        """
        <style>
            .animated-subheader {
                font-style: italic;
                animation: fadeIn 2s ease-in-out;
            }

            @keyframes fadeIn {
                from {
                    opacity: 0;
                    transform: translateY(-10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            .feature-container {
                text-align: center;
                transition: transform 0.3s, box-shadow 0.3s;
                border-radius: 8px;
                padding: 10px;
                margin: 10px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                background-color: #ffffff;
                display: flex;
                flex-direction: column;
                justify-content: center;  /* Center content vertically */
                align-items: center;      /* Center content horizontally */
            }

            .feature-container:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
            }

            .center-content {
                display: flex;
                justify-content: center;
                margin: 20px 0;
            }

            footer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


elif page == "About":
    st.header("About Osulation")

    # Adding styles and structure
    st.markdown("""
    <div class="about-section">
        <h3>What is Osulation?</h3>
        <p>Osulation is an innovative project that combines the popular rhythm game osu! with hand gesture controls. 
        Our goal is to create a more immersive and physically engaging gaming experience.</p>
    </div>
    
    <div class="about-section">
        <h3>Key Features</h3>
        <ul class="feature-list">
            <li>🎮 Hand gesture recognition for gameplay</li>
            <li>⚡ Real-time tracking and responsiveness</li>
            <li>📚 Can be used with popular osu! beatmaps</li>
            <li>🌐 Applicable to other games and applications</li>
        </ul>
    </div>
    
    <div class="about-section">
        <h3>Technology Stack</h3>
        <ul class="feature-list">
            <li>🐍 Python for backend logic</li>
            <li>🖼️ OpenCV for image processing</li>
            <li>🤖 Roboflow for hand tracking</li>
            <li>🌍 Streamlit for the web interface</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Adding custom styles with vibrant colors and hover effects
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
            }

            .about-section {
                background: linear-gradient(135deg, #FF7E5F, #feb47b);
                border-radius: 8px;
                padding: 20px;
                margin: 20px 0;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
                transition: transform 0.3s, box-shadow 0.3s;
            }

            .about-section:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
            }

            .about-section h3 {
                font-size: 1.8rem;
                color: #fff;
                margin-bottom: 10px;
                text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
            }

            .about-section p {
                font-size: 1.2rem;
                color: #fff;
                line-height: 1.6;
            }

            .feature-list {
                list-style-type: none;
                padding-left: 0;
                margin: 10px 0;
            }

            .feature-list li {
                font-size: 1.2rem;
                color: #fff;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                transition: background-color 0.3s, transform 0.3s;
            }

            .feature-list li:hover {
                background-color: rgba(255, 255, 255, 0.2);
                transform: scale(1.03);
            }

            footer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

elif page == "Team":
    st.header("Meet the Team")

    st.markdown("""
    <style>
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            margin: 20px 0;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        .team-member {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 15px;
            text-align: center;
            background-color: white;
            border-radius: 10px;
            padding: 10px;
            width: 200px;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .team-member img {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            margin-bottom: 10px;
            border: 2px solid #4a90e2; /* Add a border color */
        }

        .team-member:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        h4 {
            color: #4a90e2; /* Team member name color */
            margin: 5px 0;
        }

        p {
            margin: 0;
            color: #555; /* Text color for descriptions */
        }
    </style>

    <div class="team-container">
        <div class="team-member">
            <img src="assets/cindyli_face.png" alt="Cindy Li">
            <div>
                <h4>Cindy Li</h4>
                <p>CS Sophomore @ Cornell</p>
                <p>Interests: Tennis, Guitar</p>
            </div>
        </div>
        <div class="team-member">
            <img src="assets/selina_face.jpeg" alt="Selina Sun">
            <div>
                <h4>Selina Sun</h4>
                <p>CS Sophomore @ Michigan</p>
                <p>Interests: Nice Life</p>
            </div>
        </div>
        <div class="team-member">
            <img src="assets/cindyyang_face.jpeg" alt="Cindy Yang">
            <div>
                <h4>Cindy Yang</h4>
                <p>Robotics Sophomore @ Michigan</p>
                <p>Interests: Sleep</p>
            </div>
        </div>
        <div class="team-member">
            <img src="assets/elise_face.jpeg" alt="Elise Zhu">
            <div>
                <h4>Elise Zhu</h4>
                <p>CS+Math Sophomore @ Georgetown</p>
                <p>Interests: Dance, Cat</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "How to Play":
    st.header("How to Play Osulation")

    # Adding styles and structure
    st.markdown("""
    <div class="how-to-play-section">
        <h3>Getting Started</h3>
        <ol class="step-list">
            <li>Ensure your webcam is connected and functioning.</li>
            <li>Click the "Start Osulation" button on the home page.</li>
            <li>Allow the application to access your camera.</li>
            <li>Position yourself so that your hands are clearly visible to the camera.</li>
        </ol>
    </div>
    
    <div class="how-to-play-section">
        <h3>Gameplay</h3>
        <ul class="step-list">
            <li>Use your right hand to control the gameplay.</li>
            <li>Move your hand with an open palm to move the cursor.</li>
            <li>Close your hand into a fist to tap each circle.</li>
            <li>Time your taps to the rhythm of the music for higher scores.</li>
        </ul>
    </div>
    
    <div class="how-to-play-section">
        <h3>Tips & Tricks</h3>
        <ul class="step-list">
            <li>Practice makes perfect! Start with easier beatmaps and work your way up.</li>
            <li>Ensure good lighting for better hand tracking.</li>
            <li>Make sure your camera is level and stable.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Adding custom styles with vibrant colors and hover effects
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
            }

            .how-to-play-section {
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                border-radius: 8px;
                padding: 20px;
                margin: 20px 0;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
                transition: transform 0.3s, box-shadow 0.3s;
            }

            .how-to-play-section:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
            }

            .how-to-play-section h3 {
                font-size: 1.8rem;
                color: #fff;
                margin-bottom: 10px;
                text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
            }

            .step-list {
                list-style-type: none;
                padding-left: 0;
                margin: 10px 0;
            }

            .step-list li {
                font-size: 1.2rem;
                color: #fff;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                transition: background-color 0.3s, transform 0.3s;
            }

            .step-list li:nth-child(odd) {
                background-color: rgba(255, 255, 255, 0.1);
            }

            .step-list li:nth-child(even) {
                background-color: rgba(255, 255, 255, 0.15);
            }

            .step-list li:hover {
                background-color: rgba(255, 255, 255, 0.3);
                transform: scale(1.03);
            }

            footer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

elif page == "Data Visualization":
    st.header("Data Visualization")

    # Data for different version models
    versions = ['Version 1', 'Version 2', 'Version 3', 'Version 4', 'Version 5', 'Version 6']
    accuracy_clicking = [0.60, 0.75, 0.78, 0.90, 0.76, 0.92]
    accuracy_holding = [0.55, 0.70, 0.72, 0.85, 0.74, 0.88]
    timing_to_register = [1.5, 1.2, 1.3, 0.8, 1.1, 0.7]

    # Create bar chart for accuracy
    fig = go.Figure()
    fig.add_trace(go.Bar(x=versions, y=accuracy_clicking, name='Accuracy Clicking', marker_color='royalblue'))
    fig.add_trace(go.Bar(x=versions, y=accuracy_holding, name='Accuracy Holding', marker_color='gold'))

    # Create layout for bar chart
    fig.update_layout(
        title='Accuracy Comparison by Version',
        xaxis_title='Version',
        yaxis_title='Accuracy',
        barmode='group',
        yaxis=dict(range=[0, 1]),
        template='plotly_white',
        plot_bgcolor='rgba(0, 0, 0, 0.05)',
        title_font=dict(size=24, color='darkblue', family='Arial'),
        xaxis_title_font=dict(size=16, color='black'),
        yaxis_title_font=dict(size=16, color='black'),
        legend=dict(font=dict(size=14))
    )

    st.plotly_chart(fig)

    # Create line chart for timing to register
    fig_timing = go.Figure()
    fig_timing.add_trace(go.Scatter(x=versions, y=timing_to_register, mode='lines+markers', name='Timing to Register', marker_color='mediumseagreen', line=dict(width=3)))

    # Create layout for timing chart
    fig_timing.update_layout(
        title='Timing to Register by Version',
        xaxis_title='Version',
        yaxis_title='Timing (seconds)',
        yaxis=dict(range=[0, 2]),
        template='plotly_white',
        plot_bgcolor='rgba(0, 0, 0, 0.05)',
        title_font=dict(size=24, color='darkgreen', family='Arial'),
        xaxis_title_font=dict(size=16, color='black'),
        yaxis_title_font=dict(size=16, color='black'),
        legend=dict(font=dict(size=14))
    )

    st.plotly_chart(fig_timing)

    # Adding some custom CSS for the charts
    st.markdown(
        """
        <style>
            .stPlotlyChart {
                margin: auto;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }
        </style>
        """,
        unsafe_allow_html=True
    )
