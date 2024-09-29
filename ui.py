import os
import re
import base64
from pathlib import Path
import streamlit as st
from inference6 import start_game
import plotly.graph_objects as go
import subprocess

def markdown_images(markdown):
    # example image markdown:
    images = re.findall(r'\<img src.*\>', markdown)
    return images


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path, img_alt):
    img_format = img_path.split(".")[-1]
    img_html = f'<img src="data:image/{img_format.lower()};base64,{img_to_bytes(img_path)}" alt="{img_alt}" style="max-width: 100%;">'

    return img_html


def markdown_insert_images(markdown):
    images = markdown_images(markdown)

    for image in images:
        split_info = image.split('\"')
        image_alt = split_info[-1]
        image_path = split_info[1]
        if os.path.exists(image_path):
            markdown = markdown.replace(image, img_to_html(image_path, image_alt))
    return markdown

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Aldrich', sans-serif;
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
        background-color: #0d4954;
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
    import streamlit as st

    .sidebar.sidebar-content {
        padding-left: 20px; 
    }

    /* Change background color of the sidebar */
    [data-testid="stSidebar"] {
        background-color: #f0f0f5;
        padding-left: 20px;
    }

    /* Style the sidebar header */
    [data-testid="stSidebar"] h3 {
        font-size: 22px;
        color: white;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Style the navigation menu (radio button group) */
    [data-testid="stSidebar"] .css-1d391kg .css-10trblm {
        background-color: transparent !important;
        color: white !important;
        padding: 10px;
        margin: 5px 0;
        border-radius: 8px;
        text-align: center;
    }

    /* Hover effect for menu items */
    [data-testid="stSidebar"] .css-1d391kg .css-10trblm:hover {
        background-color: #444 !important;
        color: #f0a500 !important;  /* Hover color */
    }

    /* Selected item in the navigation menu */
    [data-testid="stSidebar"] .css-1d391kg .css-10trblm:focus {
        background-color: #f0a500 !important;  /* Highlight selected item */
        color: black !important;  /* Text color for selected */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar with logo
st.sidebar.image("assets/osulogoblue.png", width=200)
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Home", "About", "Team", "How to Play", "Data Visualization"])

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
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" fill="white" viewBox="0 0 24 24">
<path d="M 9.5996094 2 L 9.5996094 18.5 L 13.689453 14.609375 L 16.900391 22 L 19.099609 21 L 15.791016 13.703125 L 15.800781 13.699219 L 21.599609 13.199219 L 9.5996094 2 z M 11.599609 6.5996094 L 16.900391 11.599609 L 15.599609 11.699219 L 15.300781 11.699219 L 15 11.800781 L 12.900391 12.699219 L 12.599609 12.800781 L 12.300781 13 L 11.599609 13.699219 L 11.599609 6.5996094 z"></path>
</svg>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="feature-container" style="height: {feature_height};">
                <h4>Real-time Tracking</h4>
                <p>Responsive and accurate gesture recognition</p>
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" fill="white" width="100" height="100" viewBox="0 0 24 24">
<path d="M 12 4 C 12 4 5.6992188 4.0003906 4.1992188 4.4003906 C 3.2992187 4.6003906 2.6003906 5.2992187 2.4003906 6.1992188 C 2.0003906 7.6992188 2 12 2 12 C 2 12 2.0003906 16.300781 2.4003906 17.800781 C 2.6003906 18.700781 3.2992187 19.299609 4.1992188 19.599609 C 5.6992188 19.999609 12 20 12 20 C 12 20 18.300781 19.999609 19.800781 19.599609 C 20.700781 19.399609 21.299609 18.700781 21.599609 17.800781 C 21.999609 16.300781 22 12 22 12 C 22 12 21.999609 7.6992187 21.599609 6.1992188 C 21.399609 5.2992187 20.700781 4.7003906 19.800781 4.4003906 C 18.300781 4.0003906 12 4 12 4 z M 12 6 C 14.9 6 18.500781 6.1007813 19.300781 6.3007812 C 19.500781 6.3007812 19.599219 6.4992187 19.699219 6.6992188 C 19.899219 7.5992187 20 10.3 20 12 C 20 13.7 19.899609 16.400781 19.599609 17.300781 C 19.599609 17.500781 19.399219 17.599219 19.199219 17.699219 C 18.499219 17.899219 14.9 18 12 18 C 9.1 18 5.4992187 17.899609 4.6992188 17.599609 C 4.4992187 17.599609 4.4007813 17.399219 4.3007812 17.199219 C 4.1007812 16.399219 4 13.7 4 12 C 4 10.3 4.1007813 7.5992187 4.3007812 6.6992188 C 4.3007812 6.4992187 4.4992187 6.4007813 4.6992188 6.3007812 C 5.4992187 6.1007812 9.1 6 12 6 z M 10 8.5 L 10 15.5 L 16 12 L 10 8.5 z"></path>
</svg>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="feature-container" style="height: {feature_height};">
                <h4>Beyond Osu</h4>
                <p>Control other apps and games using hand movements</p>
<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" fill="white" viewBox="0 0 24 24">
<path d="M 12 1 C 11.083334 1 10.268559 1.3797556 9.7519531 1.9609375 C 9.2353472 2.5421194 9 3.2777779 9 4 C 9 4.7222221 9.2353472 5.4578806 9.7519531 6.0390625 C 10.068447 6.3951184 10.504816 6.6623237 11 6.8261719 L 11 7.1054688 C 10.648795 7.1779342 10.303949 7.2874267 9.9707031 7.4375 L 2.1308594 10.966797 L 2.1289062 10.96875 C 1.2905581 11.348818 0.92431009 12.195958 1.0097656 13 L 1 13 L 1 17.615234 C 1 18.158177 1.3018416 18.667228 1.8027344 18.916016 L 8.2949219 22.130859 C 10.634021 23.288504 13.365979 23.288504 15.705078 22.130859 L 22.193359 18.919922 C 22.699054 18.672098 23 18.15705 23 17.615234 L 23 13 L 22.986328 13 C 23.071983 12.19402 22.706153 11.34521 21.865234 10.966797 L 14.025391 7.4375 C 13.693436 7.2880087 13.349798 7.1799055 13 7.1074219 L 13 6.8261719 C 13.495184 6.6623237 13.931553 6.3951184 14.248047 6.0390625 C 14.764653 5.4578806 15 4.7222221 15 4 C 15 3.2777779 14.764653 2.5421194 14.248047 1.9609375 C 13.731441 1.3797556 12.916666 1 12 1 z M 12 3 C 12.416666 3 12.601893 3.1202444 12.751953 3.2890625 C 12.902014 3.4578806 13 3.7222221 13 4 C 13 4.2777779 12.902014 4.5421194 12.751953 4.7109375 C 12.601893 4.8797556 12.416666 5 12 5 C 11.583334 5 11.398107 4.8797556 11.248047 4.7109375 C 11.097986 4.5421194 11 4.2777779 11 4 C 11 3.7222221 11.097986 3.4578806 11.248047 3.2890625 C 11.398107 3.1202444 11.583334 3 12 3 z M 11 9.1933594 L 11 13 L 13 13 L 13 9.1953125 C 13.067261 9.2201233 13.13667 9.2317917 13.203125 9.2617188 L 21.027344 12.783203 L 14.349609 16.394531 C 12.849518 17.205891 11.148529 17.205891 9.6484375 16.394531 L 2.9707031 12.783203 L 10.792969 9.2617188 C 10.860767 9.2311865 10.931364 9.2185665 11 9.1933594 z M 7.5 12 A 1.5 1 0 0 0 7.5 14 A 1.5 1 0 0 0 7.5 12 z M 3 15.072266 L 8.6972656 18.154297 C 10.769174 19.274937 13.228873 19.274937 15.300781 18.154297 L 15.302734 18.154297 L 21 15.072266 L 21 17.277344 L 14.818359 20.337891 C 13.031458 21.222246 10.968542 21.222246 9.1816406 20.337891 L 3 17.277344 L 3 15.072266 z"></path>
</svg>            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="center-content">', unsafe_allow_html=True)
    if st.button("Start Osulation", key="start_button", help="Click to start the game!"):
        st.markdown(
        """
        <script>
        window.open('', '_self', '');
        window.close();
        </script>
        """,
        unsafe_allow_html=True
        )
        start_game()
        subprocess.run(["open", "-a", "osu!"])
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
                color: white;
                transition: transform 0.3s, box-shadow 0.3s;
                border-radius: 8px;
                padding: 10px;
                margin: 10px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                background: linear-gradient(135deg, #1f8cba, #0fa5b6); 
                display: flex;
                flex-direction: column;
                justify-content: center;  /* Center content vertically */
                align-items: center;      /* Center content horizontally */
            }

            .feature-container:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
            }

            .feature-container h4 {
            color: white; 
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
        <ul class="feature-list">
        <li>Osulation is an innovative project that combines the popular rhythm game osu! with hand gesture controls.
        Our goal is to create a more immersive and physically engaging gaming experience.</li>
        </ul>
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
    # In the About section
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
            }

            .about-section {
                background: linear-gradient(135deg, #1f8cba, #0fa5b6); /* Darker gradient */
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

            .feature-list {
                list-style-type: none;
                padding-left: 0;
                margin: 10px 0;
            }

            .feature-list li {
                font-size: 1.2rem;
                color: #fff; /* Ensure text is white for contrast */
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                transition: background-color 0.3s, transform 0.3s;
            }

            .feature-list li:hover {
                background-color: rgba(255, 255, 255, 0.2);
                transform: scale(1.03);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

elif page == "Team":
    st.header("Meet the Team")

    st.markdown(markdown_insert_images("""
    <style>
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            margin: 20px 0;
            padding: 20px;
            background: linear-gradient(135deg, #1f8cba, #0fa5b6); 
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
        <a href="https://www.linkedin.com/in/2023cyang/">
        <div class="team-member">
            <img src="assets/cindyli_face.png" alt="Cindy Li">
            <div>
                <h4>Cindy Li</h4>
                <p>CS Sophomore @ Cornell</p>
                                <p>Interests: Tennis, Guitar</p>
            </div>
        </div>
        </a>
        <a href="https://www.linkedin.com/in/2023cyang/">
        <div class="team-member">
            <img src="assets/selina_face.jpeg" alt="Selina Sun">
            <div>
                <h4>Selina Sun</h4>
                <p>CS Sophomore @ Michigan</p>
                <p>Interests: Nice Life</p>
            </div>
        </div>
        </a>                    
        <a href="https://www.linkedin.com/in/2023cyang/">
        <div class="team-member">
            <img src="assets/cindyyang_face.jpeg" alt="Cindy Yang">
            <div>
                <h4>Cindy Yang</h4>
                <p>Robotics Sophomore @ Michigan</p>
                <p>Interests: Sleep</p>
            </div>
        </div>
        </a>
        <a href="https://www.linkedin.com/in/elise-yz/">
        <div class="team-member">
            <img src="assets/elise_face.jpeg" alt="Elise Zhu">
            <div>
                <h4>Elise Zhu</h4>
                <p>CS+Math Sophomore @ Georgetown</p>
                <p>Interests: Dance, Cat</p>
            </div>
        </div>
        </a>
    </div>
    """), unsafe_allow_html=True)

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
                background: linear-gradient(135deg, #1f8cba, #0fa5b6); /* Darker gradient */
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
