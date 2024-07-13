import streamlit as st

st.set_page_config(page_title="Legal Tools", page_icon="⚖️", layout="wide")

st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: space-around;
        margin-top: 50px;
    }
    .custom-button {
        width: 280px;
        height: 280px;
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

def home():
    st.title("Legal Tools ⚖️")
    st.write("Welcome to the Legal Tools application. Please select a tool below:")

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.markdown('<button class="custom-button">:frame_with_picture: Case Summarizer.img</button>', unsafe_allow_html=True):
            if st.button("Case Summarizer", key="summarizer"):
                st.session_state.page = "summarizer"
    with col2:
        if st.markdown('<button class="custom-button">:frame_with_picture: Case Search.img</button>', unsafe_allow_html=True):
            if st.button("Case Search", key="search"):
                st.session_state.page = "search"
    with col3:
        if st.markdown('<button class="custom-button">:frame_with_picture: Law Chatbot.img</button>', unsafe_allow_html=True):
            if st.button("Law Chatbot", key="chatbot"):
                st.session_state.page = "chatbot"
    st.markdown('</div>', unsafe_allow_html=True)

def run_script(script_name):
    exec(open(script_name).read(), globals())

def main():
    if st.session_state.page == "summarizer":
        run_script('case_summariser.py')
    elif st.session_state.page == "search":
        run_script('case_search.py')
    elif st.session_state.page == "chatbot":
        run_script('criminal_case_chatbot.py')
    else:
        home()

if __name__ == "__main__":
    main()
