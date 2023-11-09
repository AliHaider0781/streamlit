import streamlit as st

st.set_page_config(page_title="ArkAsh.Services" , page_icon="💼", layout="wide")

def define_html(file_name):
    with open(file_name) as f:
        html_string = f.read()
    st.markdown(html_string, unsafe_allow_html=True)

def define_css(file_name):
    with open(file_name) as f:
        css_string = f.read()
    st.markdown(f"<style>{css_string}</style>", unsafe_allow_html=True)

def define_js(file_name):
    with open(file_name) as f:
        js_string = f.read()
    st.markdown(f"<script>{js_string}</script>", unsafe_allow_html=True)

st.title("Login")

# Define the HTML
define_html("structure/signup.html")

# Define the CSS
define_css("structure/login.css")

# Define the JS
define_js("structure/lo.js")

#css
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")