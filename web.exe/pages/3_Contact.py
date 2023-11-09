import streamlit as st

st.title("Contact")


#css
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#contact doc
contact_form = """
<form action="https://formsubmit.co/3c0abebf5155050cc5b2adf4fd03d2c4" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <textarea name="message" placeholder="Message" required></textarea>
    <button type="submit">Send</button>
</form>
"""

with st.container():
        #st.write("---")
        st.header("Get In Contact!")
        #st.write("##")
        st.markdown(contact_form, unsafe_allow_html=True)