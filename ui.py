import streamlit as st

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
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="vertical-center">', unsafe_allow_html=True)
        st.image("assets/osulogoblue.png", width=300)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.header("Welcome to Osulation!")
    st.markdown(
        "<p style='font-size: 16px;'>A fun way to play osu with your hands<p>",
        unsafe_allow_html=True
    )
    
    if st.markdown('<button class="custom-button">Start Osulation</button>', unsafe_allow_html=True):
        st.write(" ")
        # start_game()  # Uncomment this line to start the game

# Centered GitHub logo
st.markdown(
    '<div class="center"><a href="https://github.com/elise-yz/osulation"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" style="width: 50px;"/></a></div>',
    unsafe_allow_html=True
)