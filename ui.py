import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("assets/osulogo.png")

with col2:
    st.header("A fun way to play osu with your hands")
    st.markdown(
        """
        <style>
        .custom-button {
            background-color: #f5a4d0; 
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Place the button inside the column context
    if st.markdown('<button class="custom-button">Start Osulation</button>', unsafe_allow_html=True):
        st.write(" ")
        # start_game()  # Uncomment this line to start the game